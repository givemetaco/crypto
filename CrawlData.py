
# Raw Package
import numpy as np
import pandas as pd

#Data Source
import yfinance as yf

# Get Bitcoin data
# 이전 24시간동안의 데이터를 15분간격으로 가져옴
data = yf.download(tickers='BTC-USD', period = '24h', interval = '5m')

#if you want get the csv file use the code below
# data.to_csv("CyrptoData.csv")


# 모든 Datatime 데이터를 가져오는법
# print(data.index)

# 모든 Open 데이터를 가져오는법
# High,Low등을 가져오려면 괄호안의 Open대신 해당하는 인덱스 이름을 입력하면됨
# data['Open']

# 자세한 사항은 https://pandas.pydata.org/docs/reference/frame.html 참조
