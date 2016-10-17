import pandas as pd
import datetime
from pandas_datareader import data
import matplotlib.pyplot as plt
from matplotlib import style


start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2015, 8, 22)

df = data.DataReader("XOM", "yahoo", start, end)
style.use('fivethirtyeight')

print(df.head())

df['High'].plot()
plt.legend()
plt.show()