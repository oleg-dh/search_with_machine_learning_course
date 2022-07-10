# Level 1 - Results

```
~/fastText-0.9.2/fasttext supervised -input data.train -output model_product_classifier -lr 1.0 -epoch 25
Read 0M words
Number of words:  6112
Number of labels: 32
Progress: 100.0% words/sec/thread:    6972 lr:  0.000000 avg.loss:  0.035073 ETA:   0h 0m 0s

```

P@1
```
N       3000
P@1     0.974
R@1     0.974
```

P@5
```
N       3000
P@5     0.2
R@5     0.998
```

P@10
```
N       3000
P@10    0.0999
R@10    0.999
```