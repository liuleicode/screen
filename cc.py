import numpy as np
import pandas as pd
import pandas_datareader.data as web


sp500 = web.DataReader('BZZ', data_source='yahoo',
                       start='1/1/2016', end='4/14/2016')
sp500.info()

sp500['Close'].plot(grid=True,figsize=(8,5))
