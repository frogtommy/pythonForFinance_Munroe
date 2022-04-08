import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt
import yfinance as yf


#  1. REMOTELY downloads Tesla historical prices from exchange of your choice from Jan 1st, 2019 to Jan 2nd, 2022
#  2. Normalizes returns to day 0. I.e. value for Jan 1st, 2019 will be 1.00
#  3. Calculates the variance(standard deviation) for Tesla on the NORMALIZED data(from step 2)
#  4. Creates two columns for price plus and minus two standard deviations.
#  5. Loads data from BTC-USD.csv
#  6. Performs steps 2-4 for BTC data
#  7. Plots them together on the same graph
#  8. Adds horizontal line on graph at 0

##############
## STEP ONE ##
##############

fromDate = '2019-01-01' ##set your beginning date
toDate = '2022-01-01' ##set your end date

tesla = yf.download('TSLA',fromDate,toDate) ##download TESLA stock using yfinance
# print(tesla) ##check to see it downloaded


##############
## STEP TWO ##
##############

tesla = tesla[['Close']] ##isolate the column I need
tesla["Normalized"] = tesla['Close']/tesla['Close'][0] ##normalize TESLA stock to day zero
# print(tesla) ##check everything is looking good


################
## STEP THREE ##
################

# teslaMean = tesla['Normalized'].mean() ##find the mean
teslaSTD = tesla['Normalized'].std() ##find the standard deviation
# tesla['Norm + 2STD'] = tesla['Normalized'] + (teslaMean + (2*teslaSTD))
tesla['Tesla Norm + 2STD'] = tesla['Normalized'] + (2*teslaSTD)
# tesla['Norm - 2STD'] = tesla['Normalized'] - (teslaMean - (2*teslaSTD))
tesla['Tesla Norm - 2STD'] = tesla['Normalized'] - (2*teslaSTD)
print(tesla)

##I was trying out something similar to the HW7 where we included mean when sorting out data that was one standard
##deviation above and below the data we were looking at, but I was pretty sure this was wrong since the function
##could find the standard deviation by itself

##Also, we were specifically looking at 2 standard deviations above and below the PRICE on any day, so adding the mean
##wouldn't be necessary.

##Basic trial and error/logically trying to think my way through the problem


###############
## STEP FOUR ##
###############

bitcoin = pd.read_csv('BTC-USD.csv',index_col='Date',parse_dates=True) ##load bitcoin file
# print(bitcoin) ##check it

##############
## STEP SIX ##
##############

bitcoin = bitcoin[['Close']]
bitcoin['Normalized'] = bitcoin['Close']/bitcoin['Close'][0]
# print(bitcoin)
bitcoinSTD = bitcoin['Normalized'].std()
bitcoin['BTC Norm + 2STD'] = bitcoin['Normalized'] + (2*bitcoinSTD)
bitcoin['BTC Norm - 2STD'] = bitcoin['Normalized'] - (2*bitcoinSTD)
print(bitcoin)

################
## STEP SEVEN ##
################

tesla = tesla[['Tesla Norm + 2STD','Tesla Norm - 2STD']]
bitcoin = bitcoin[['BTC Norm + 2STD','BTC Norm - 2STD']]
print(tesla,bitcoin)

join = bitcoin.join(tesla,how='inner')
print(join) ##never had to fix the dates for bitcoin since joining auto dropped dates pre 01/01/2019

join.plot()
plt.axhline(0,color='pink')
plt.show()










