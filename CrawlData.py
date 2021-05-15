
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
        
        self.datetime=self.data.index
        self.open_data=self.data['Open']
        self.high_data=self.data['High']
        self.low_data=self.data['Low']
        self.close_data=self.data['Close']
        self.volume_data=self.data['Volume']

    def create_csv(self):
        """"This function generates a csv file with cryptocurrency data's"""
        self.data.to_csv("CryptoData.csv")


# 모든 Datatime 데이터를 가져오는법
# print(data.index)

# 모든 Open 데이터를 가져오는법
# High,Low등을 가져오려면 괄호안의 Open대신 해당하는 인덱스 이름을 입력하면됨
# data['Open']

# 자세한 사항은 https://pandas.pydata.org/docs/reference/frame.html 참조
