
# Raw Package
import numpy as np
import pandas as pd
from pandas.core.frame import DataFrame

# Data Source
import yfinance as yf

# Get Bitcoin data
# 이전 24시간동안의 데이터를 15분간격으로 가져옴
#data = yf.download(tickers='BTC-USD', period='24h', interval='5m')

class Coin:
    def __init__(self,tickers,period,interval) -> DataFrame:
        """
        ==========================
        About tickers
        ==========================
        Bitcoin -> BTC
        Ethereum -> ETH
        Binanace Coin -> BNB
        Dogecoin -> DOGE
        Cardano -> ADA
        Tether ->  USDT
        XRP -> XRP
        Polkadot -> DOT
        Internet Computer -> ICP
        Bitcoin Cash -> BCH
        ==========================
        About period & interval
        ==========================
        https://medium.com/analytics-vidhya/python-how-to-get-bitcoin-data-in-real-time-less-than-1-second-lag-38772da43740
        """
        try:
            self.data = yf.download(tickers=tickers, period=period, interval=interval)
        except:
            print("error in fetching data")

    def create_csv(self):
        """"This function generates a csv file with cryptocurrency data's"""
        self.data.to_csv("CryptoData.csv")


# 자세한 사항은 https://pandas.pydata.org/docs/reference/frame.html 참조
