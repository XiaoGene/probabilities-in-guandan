# probabilities-in-guandan
Monte-carlo simulation to compute card type probabilities in Guandan.


### 同时抓到两张黑桃A的概率
``` python
python contain_two_spade_ones.py
```
理论概率是 `C_106^25 / C_108^27 = 0.06075`, 模拟100000次的实验概率是0.0611.

### 抓到同花顺的概率（不考虑百搭牌）
``` python
python straight_flush.py
```
理论概率未知，模拟1000000次的实验概率是0.3128.
