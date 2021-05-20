
# Raw Package
import numpy as np
import pandas as pd
from pandas.core.frame import DataFrame

# Data Source
import yfinance as yf
from yfinance.multi import download

import requests

#빗썸 API사용을 위한 url정의 (추후 사용할것)
#url='https://api.bithumb.com/public/transaction_history/BTC_KRW?count=5'
#rep=requests.get(url).json()
#print(rep['data'][0])

class Coin:

    def __init__(self, tickers) -> None:
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
        self.info=yf.Ticker(tickers).info
        self.name=self.info['name']
        self.tickers = tickers
        self.data=yf.download(self.tickers,period='24',interval='1m')

    # try:
    #     self.data = yf.download(tickers=tickers, period=period, interval=interval)
    # except:
    #     print("error in fetching data")

    # 최근 24시간동안의 데이터를 1분 간격으로 표시한 데이터를 DataFrame 형태로 돌려주는 함수
    def get_day_data(self):
        return yf.download(self.tickers, period='1d', interval='1m')

    # 최근 1주동안의 데이터를 1시간 간격으로 표시한 데이터를 DataFrame 형태로 돌려주는 함수
    def get_weekly_data(self):
        return yf.download(self.tickers, period='1wk', interval='1h')

    # 최근 3달동안의 데이터를 1일 간격으로 표시한 데이터를 DataFrame 형태로 돌려주는 함수
    def get_yearly_data(self):
        return yf.download(self.tickers, period='3m', interval='1d')

    # 현재 코인 가격을 돌려주는 함수
    def get_current_data(self):
        return yf.Ticker(self.tickers).info['regularMarketPrice']

    # 데이터를 csv파일 형태로 만들어 저장하는 함수
    def create_csv(self):
        """"This function generates a csv file with cryptocurrency data's"""
        # self.data.to_csv("CryptoData.csv")


# 자세한 사항은 https://pandas.pydata.org/docs/reference/frame.html 참조
