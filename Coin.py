# Raw Package
import numpy as np
import pandas as pd
from pandas.core.frame import DataFrame

# Data Source
import yfinance as yf
from yfinance import ticker
from yfinance.multi import download

import requests

from pybithumb import Bithumb


class Coin:

    def __init__(self, tickers) -> None:
        """
        ==========================
        About tickers
        ==========================
        Bitcoin -> BTC
        Ethereum -> ETH
        Dogecoin -> DOGE
        Cardano -> ADA
        XRP -> XRP
        Ethereum_Classic -> ETC
        EOS -> EOS
        Chainlink -> LINK
        Litecoin -> LTC
        Bitcoin Cash -> BCH
        ==========================
        About period & interval
        ==========================
        https://medium.com/analytics-vidhya/python-how-to-get-bitcoin-data-in-real-time-less-than-1-second-lag-38772da43740
        """
        self.tickers = tickers
        # self.info=yf.Ticker(self.tickers+'-USD').info
        # self.data=yf.download(self.tickers+'-USD',period='3mo',interval='1d')

    # 최근 24시간동안의 데이터를 1분 간격으로 표시한 데이터를 DataFrame 형태로 돌려주는 함수
    def get_day_data(self):
        return yf.download(self.tickers + '-USD', period='1d', interval='1m')

    # 최근 1주동안의 데이터를 1시간 간격으로 표시한 데이터를 DataFrame 형태로 돌려주는 함수
    def get_weekly_data(self):
        return yf.download(self.tickers + '-USD', period='1wk', interval='1h')

    # 최근 3달동안의 데이터를 1일 간격으로 표시한 데이터를 DataFrame 형태로 돌려주는 함수
    def get_monthly_data(self):
        return yf.download(self.tickers + '-USD', period='3mo', interval='1d')

    # 현재 코인 가격을 돌려주는 함수
    def get_current_data(self):
        return Bithumb.get_market_detail(self.tickers)[3]

    # 데이터를 csv파일 형태로 만들어 저장하는 함수
    def create_csv(self):
        """"This function generates a csv file with cryptocurrency data's"""
        # self.data.to_csv("CryptoData.csv")

    def get_transaction(self):
        # 빗썸 API사용을 위한 url정의
        url = 'https://api.bithumb.com/public/transaction_history/' + self.tickers + '_KRW?count=6'
        request = requests.get(url).json()
        transaction = request['data']  # 최근 5개 거래내역을 가지고 있는 list
        return transaction

# 자세한 사항은 https://pandas.pydata.org/docs/reference/frame.html 참조
