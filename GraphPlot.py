import matplotlib.pyplot as plt
import numpy as np
import CrawlData as cd

bitcoin=cd.Coin('ETH-USD','24h','5m')
fig, ax = plt.subplots()  # Create a figure and an axes.
ax.plot(bitcoin.datetime,bitcoin.open_data,label='Ethereum')

plt.show()