import os
import argparse
import re
import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np
import csv

# Useful if you want to perform stemming.
import nltk
stemmer = nltk.stem.PorterStemmer()

def normalize_query(query):
    # lowercase
    query = query.lower()
    query = re.sub(r'[^A-Za-z0-9_ ]+', '', query)
    query = re.sub("\s\s+" , " ", query)
    
    # query = " ".join(map(lambda t: stemmer.stem(t), query.split()))

    return query

categories_file_name = r'/workspace/datasets/product_data/categories/categories_0001_abcat0010000_to_pcmcat99300050000.xml'

queries_file_name = r'/workspace/datasets/train.csv'
output_file_name = r'/workspace/datasets/labeled_query_data.txt'

parser = argparse.ArgumentParser(description='Process arguments.')
general = parser.add_argument_group("general")
general.add_argument("--min_queries", default=1,  help="The minimum number of queries per category label (default is 1)")
general.add_argument("--output", default=output_file_name, help="the file to output to")

args = parser.parse_args()
output_file_name = args.output

min_queries = int(args.min_queries) if args.min_queries else 1

# The root category, named Best Buy with id cat00000, doesn't have a parent.
root_category_id = 'cat00000'

tree = ET.parse(categories_file_name)
root = tree.getroot()

# Parse the category XML file to map each category id to its parent category id in a dataframe.
categories = []
parents = []
for child in root:
    id = child.find('id').text
    cat_path = child.find('path')
    cat_path_ids = [cat.find('id').text for cat in cat_path]
    leaf_id = cat_path_ids[-1]
    if leaf_id != root_category_id:
        categories.append(leaf_id)
        parents.append(cat_path_ids[-2])
parents_df = pd.DataFrame(list(zip(categories, parents)), columns =['category', 'parent'])

# Read the training data into pandas, only keeping queries with non-root categories in our category tree.
df = pd.read_csv(queries_file_name)[['category', 'query']]
df = df[df['category'].isin(categories)]
df['query'] = df['query'].apply(normalize_query)

# IMPLEMENT ME: Roll up categories to ancestors to satisfy the minimum number of queries per category.
# Adopt Ilkcan Keles iterative solution
# Get category count by grouping by category.
category_counts_df = df.groupby('category').size().reset_index(name='cat_count')
# Merge with parent dataframe
df_merged = df.merge(category_counts_df, how='left', on='category').merge(parents_df, how='left', on='category')
# Apply threshold to category counts
num_of_subthreshold_categories = len(category_counts_df[category_counts_df.cat_count < min_queries])
print("Number of sub-threshold categories: " + str(num_of_subthreshold_categories))
# Rollup categories that is under the threshold.
while num_of_subthreshold_categories > 0:
    # Place parent category in the category field
    df_merged.loc[df_merged.cat_count < min_queries, 'category'] = df_merged['parent']
    # Get category for query
    df = df_merged[['category', 'query']]
    df = df[df.category.isin(categories)]
    # Update category counts
    category_counts_df = df.groupby('category').size().reset_index(name='cat_count')
    df_merged = df.merge(category_counts_df, how='left', on='category').merge(parents_df, how='left', on='category')
    # Update and then check threshold
    num_of_subthreshold_categories = len(category_counts_df[category_counts_df.cat_count < min_queries])
    print("Number of sub-threshold categories: " + str(num_of_subthreshold_categories))


# Create labels in fastText format.
df['label'] = '__label__' + df['category']

# Output labeled query data as a space-separated file, making sure that every category is in the taxonomy.
df = df[df['category'].isin(categories)]
df['output'] = df['label'] + ' ' + df['query']
df[['output']].to_csv(output_file_name, header=False, sep='|', escapechar='\\', quoting=csv.QUOTE_NONE, index=False)
