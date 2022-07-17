# Week 3 Outcome

## Level 1 - Results

Threshold - 3000
Test data size - 20000

```
~/fastText-0.9.2/fasttext supervised -input catdata.train -output category_classifier -lr 0.5 -epoch 25
Read 0M words
Number of words:  5142
Number of labels: 183
Progress: 100.0% words/sec/thread:    1387 lr:  0.000000 avg.loss:  2.661691 ETA:   0h 0m 0s

```

P@1
```
N       3000
P@1     0.502
R@1     0.502
```

P@3
```
N       3000
P@3     0.224
R@3     0.672
```

P@5
```
N       3000
P@5     0.146
R@5     0.73
```

