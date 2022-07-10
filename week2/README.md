# Week 2 Outcome

## Level 1 - Results

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

## Level 2

```
~/fastText-0.9.2/fasttext skipgram -input /workspace/datasets/fasttext/titles.txt -output /workspace/datasets/fasttext/title_model -epoch 25 -minCount 20
```

```
Query word? iphone
4s 0.874447
3gs 0.802284
3g 0.787472
apple 0.768522
ifrogz 0.753789
silicone 0.716598
4 0.69116
incase 0.663071
hardshell 0.6532
luxe 0.649213
```

```
Query word? headphones
earbud 0.866009
overtheear 0.815393
bud 0.770524
onear 0.767648
ear 0.736812
akg 0.732723
2xl 0.718247
kicker 0.71139
sennheiser 0.707458
dre 0.66269
```

```
laptops 0.668478
notebook 0.619349
500gb 0.541539
netbook 0.540582
briefcase 0.538042
espresso 0.515991
processor 0.512284
macbook 0.492925
173 0.492313
sleeve 0.487464
```


```
Query word? freezer
bottommount 0.897419
topfreezer 0.874594
251 0.75484
water 0.721735
topmount 0.719372
smooth 0.716042
refrigerator 0.706214
thruthedoor 0.706137
252 0.700777
counterdepth 0.692601
```

```
Query word? nintendo
wii 0.767234
ds 0.751559
360 0.727301
xbox 0.695735
3ds 0.675139
playstation 0.670677
friends 0.661705
tournament 0.633885
windows 0.629398
macwindows 0.627823
```


```
Query word? whirlpool
biscuitonbiscuit 0.782388
maytag 0.772649
inglis 0.740305
biscuit 0.728945
kitchenaid 0.718616
whiteonwhite 0.664328
hotpoint 0.65435
frigidaire 0.649457
stainlesslook 0.647161
monochromatic 0.638465
```


```
Query word? kodak
easyshare 0.967669
m863 0.865458
m340 0.825929
fujifilm 0.719082
82mp 0.700006
finepix 0.694714
cybershot 0.680031
olympus 0.646122
frame 0.633592
polaroid 0.622508
```


```
Query word? ps2
psp 0.871288
ps3 0.852967
gba 0.794437
gamecube 0.777396
xbox 0.71912
cheats 0.696677
guide 0.684058
game 0.676346
trilogy 0.66351
360 0.66292
```


```
Query word? razr
radio 0.629875
tomb 0.625239
aftermarket 0.598871
nancy 0.593459
kia 0.590618
drew 0.589548
quickclean 0.588956
mazda 0.57812
indash 0.576807
selfcleaning 0.572975
```

```
Query word? stratocaster
telecaster 0.935873
fretboard 0.921337
strat 0.906959
fender 0.902676
squier 0.890609
maple 0.760003
standard 0.745043
american 0.730302
parker 0.708302
washburn 0.699071
```

```
Query word? holiday
thankyou 0.711171
congratulations 0.698123
day 0.665978
kwanzaa 0.664843
hanukkah 0.655596
chill 0.650711
out 0.649262
you 0.644657
wedding 0.644436
fathers 0.643337
```

```
Query word? plasma
600hz 0.833928
63 0.758233
42 0.710206
51 0.694506
hdtv 0.687339
50 0.677546
viera 0.675839
pioneer 0.671826
theater 0.665745
projection 0.6581
```

```
Query word? leather
255wt 0.610914
friction 0.588122
claiborne 0.584441
briefcase 0.574184
carry 0.574095
rubber 0.567523
pouch 0.563003
tote 0.559197
sleeve 0.550413
small 0.546948
```