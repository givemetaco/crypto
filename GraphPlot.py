import matplotlib.pyplot as plt
import numpy as np
import CrawlData as cd
import matplotlib.gridspec as gridspec
from mpl_finance import candlestick_ohlc

bitcoin=cd.Coin('ETH-USD','24h','5m')


fig = plt.figure(figsize=(8, 5))
fig.set_facecolor('w')
gs = gridspec.GridSpec(2, 1, height_ratios=[3, 1])
axes = []
axes.append(plt.subplot(gs[0]))
axes.append(plt.subplot(gs[1], sharex=axes[0]))
axes[0].get_xaxis().set_visible(False)


x = np.arange(len(bitcoin.data.index))
ohlc = bitcoin.data[['Open', 'High', 'Low', 'Close']].astype(int).values
dohlc = np.hstack((np.reshape(x, (-1, 1)), ohlc))

# 봉차트
candlestick_ohlc(axes[0], dohlc, width=0.5, colorup='r', colordown='b')

# 거래량 차트
axes[1].bar(x, bitcoin.data.Volume, color='k', width=0.6, align='center')

plt.tight_layout()
plt.show()

# plt.show()