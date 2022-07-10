import fasttext
import argparse


parser  = argparse.ArgumentParser(description='Generate synonyms for a word file.')
general = parser.add_argument_group("general")

general.add_argument('--model'    , default='/workspace/datasets/fasttext/title_model.bin', help='model file')
general.add_argument('--threshold', default=0.75, help='similarity')
general.add_argument("--input"    , default='/workspace/datasets/fasttext/top_words.txt', help='word list file path')
general.add_argument("--output"   , default='/workspace/datasets/fasttext/synonyms.csv', help='destination file path')

if __name__ == '__main__':

    args       = parser.parse_args()
    modelFile  = args.model
    threshold  = args.threshold
    inputFile  = args.input
    outputFile = args.output

    model = fasttext.load_model(modelFile)

    print("Writing results to %s" % outputFile)

    with open(inputFile, 'r') as words:
        with open(outputFile, 'w') as out:
            for word in words:
                line = word.strip()
                for similarity, synonym in filter(lambda vals: vals[0] > float(threshold), model.get_nearest_neighbors(word.strip())):
                    line += f', {synonym}'
                if line == word.strip():
                    print("No synonyms for %s" % line)
                    continue

                out.write(f'{line}\n')