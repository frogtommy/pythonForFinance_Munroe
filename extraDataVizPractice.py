import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import pandas_datareader as web

fromDate = '1989-07-15'
toDate = '2018-07-15'

priceIndex = web.DataReader('CPIAUCSL','fred',fromDate,toDate)
# print(priceIndex)

dollarin2018 = priceIndex['CPIAUCSL'][-1]
priceIndex['inflationMulti'] = priceIndex['CPIAUCSL']/dollarin2018
# print(priceIndex)

spx = pd.read_csv('^spx_d_reind.csv',index_col='Date',parse_dates=True)
# print(spx)

spx = spx[['Close']]
# print(spx)

spxJoin = spx.join(priceIndex,how='inner')
# print(spxJoin)

spxJoin["Inflation Adjusted SPX"] = spxJoin['Close']*priceIndex['inflationMulti']
spxJoin = spxJoin[['Close','Inflation Adjusted SPX']]
# print(spxJoin)

inflationSPXPct = spxJoin['Inflation Adjusted SPX'].pct_change()
inflationSPXPct = inflationSPXPct.dropna()
print(inflationSPXPct)


spxJoin.plot()
plt.show()
plt.hist(inflationSPXPct,bins=25)
plt.show()