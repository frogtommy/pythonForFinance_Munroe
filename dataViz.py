import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import yfinance as yf


# Chose random dates, pretended I had $1000 to invest
# How much would the $1000 be today if I had invested on the first date
# remotely downloaded SPX Index with the specified dates
# loaded a CSV file (FTSE) and selected the specified dates
# Normalized the returns of each index for the "Close" column
# Now, invest the $1000 on specified start date so I can see my total gain/loss at every date
# Plotted my $1000 "investment" in SPX and FTSE showing USD returns and EUR returns on the same graph



##initialize variables
fromDate = '2017-12-10'
toDate = '2019-04-01'
wallet = 1000

##download/import data (^GSPC and FTM)
spx = yf.download('^GSPC',fromDate,toDate)
# print(spx)
ftm = pd.read_csv("^ftm_d.csv", index_col=["Date"],parse_dates=True)
# print(ftm)


##isolate close column
spx = spx[['Close']]
# print(spx)
ftm = ftm[['Close']]


##isolate desired dates
ftm = ftm.loc[fromDate:toDate]
# print(ftm)


##find % change since day 1
spx['Percent Change'] = spx['Close']/spx['Close'][0]
# print(spx)
ftm['Percent Change'] = ftm['Close']/ftm['Close'][0]
# print(ftm)


##invest $1000
spx['USD Returns'] = spx['Percent Change']*wallet
# print(spx)
ftm['EUR Returns'] = ftm['Percent Change']*wallet
# print(ftm)


##drop unnecessary columns
# spx = spx.drop('Percent Change',axis=1).drop('Close',axis=1) ##harder way
spx = spx[['USD Returns']] ##easier way
print(spx)
# ftm = ftm.drop('Percent Change',axis=1).drop('Close',axis=1) ##harder way
ftm = ftm[['EUR Returns']] ##easier way
print(ftm)


##merge SPX and FTM
joinDF = spx.join(ftm, how='inner')
print(joinDF)

##plot
joinDF.plot()
plt.show()


