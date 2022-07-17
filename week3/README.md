# Week 3 Outcome

## Project Assesment

### Category-Query Minimum - 1k, Train Sample 30k, Test Sample 8k

With wordNgrams


```
~/fastText-0.9.2/fasttext supervised -input catdata.train -output category_classifier -lr 0.5 -epoch 25 -wordNgrams 2
Read 0M words
Number of words:  6336
Number of labels: 387
Progress: 100.0% words/sec/thread:     820 lr:  0.000000 avg.loss:  2.197343 ETA:   0h 0m 0s
```

P@1
```
N       8000
P@1     0.502
R@1     0.502
```

P@3
```
N       8000
P@3     0.227
R@3     0.682
```

P@5
```
N       8000
P@5     0.15
R@5     0.748
```

### Category-Query Minimum - 3k, Train Sample 20k, Test Sample 30k

Without wordNgrams

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

### Category-Query Minimum - 10k, Train Sample 30k, Test Sample 8k

With wordNgrams

```
~/fastText-0.9.2/fasttext supervised -input catdata.train -output category_classifier -lr 0.5 -epoch 25 -wordNgrams 2
Read 0M words
Number of words:  6348
Number of labels: 69
Progress: 100.0% words/sec/thread:    4249 lr:  0.000000 avg.loss:  1.565534 ETA:   0h 0m 0s
```

P@1
```
N       8000
P@1     0.575
R@1     0.575
```

P@3
```
N       8000
P@3     0.256
R@3     0.768
```

P@5
```
N       8000
P@5     0.165
R@5     0.823
```

### Bonus - Category-Query Minimum - 1k, Train Sample 30k, Test Sample 8k

Without wordNgrams
Small uplift in P&R

```
~/fastText-0.9.2/fasttext supervised -input catdata.train -output category_classifier -lr 0.5 -epoch 25
Read 0M words
Number of words:  6336
Number of labels: 387
Progress: 100.0% words/sec/thread:     826 lr:  0.000000 avg.loss:  3.054265 ETA:   0h 0m 0s
```

P@1
```
N       8000
P@1     0.509
R@1     0.509
```

P@3
```
N       8000
P@3     0.228
R@3     0.682
```

P@5
```
N       8000
P@5     0.149
R@5     0.747
```

### Category Filters Test

#### Positive Examples
_ipad_ - pcmcat209000050007, more relevant products in top 10
_speakers_ - 'abcat0515039', 'abcat0208011', 'pcmcat144700050004', 'pcmcat223000050007' - ambiguous query brings more relevant products

#### Negative Examples
_window_ - misses window air conditioners and returns only windows products
_ps3_ - returns only games, while without filters it returns accessoires