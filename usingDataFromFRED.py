import pandas_datareader as web
import datetime as date

##############
## STEP ONE ##
##############
fromDate = '02-01-2014'
toDate = '02-01-2016'

dfSixMo = web.DataReader('DGS6MO','fred',fromDate,toDate)
dfYearOne = web.DataReader('DGS1','fred',fromDate,toDate)
dfYearFive = web.DataReader('DGS5','fred',fromDate,toDate)
dfYearTen = web.DataReader('DGS10','fred',fromDate,toDate)
# print(dfSixMo,dfYearOne,dfYearFive,dfYearTen)
# dfSixMo.to_csv('SixMonth.csv')


##############
## STEP TWO ##
##############
sixMean = dfSixMo['DGS6MO'].mean()
sixStDv = dfSixMo['DGS6MO'].std()
print("Six month maturity mean is: ",sixMean,", and the standard deviation is: ",sixStDv)

oneYearMean = dfYearOne['DGS1'].mean()
oneYearStDv = dfYearOne['DGS1'].std()
print("One year maturity mean is: ",oneYearMean,", and the standard deviation is: ",oneYearStDv)

fiveYearMean = dfYearFive['DGS5'].mean()
fiveYearStDv = dfYearFive['DGS5'].std()
print("Five year maturity mean is: ",fiveYearMean,", and the standard deviation is: ",fiveYearStDv)

yearTenMean = dfYearTen['DGS10'].mean()
yearTenStDv = dfYearTen['DGS10'].std()
print("Ten year maturity mean is: ",yearTenMean,", and the standard deviation is: ",yearTenStDv)


################
## STEP THREE ##
################
dfSixMo = dfSixMo[  (dfSixMo["DGS6MO"] > (sixMean+sixStDv)) | (dfSixMo["DGS6MO"] < (sixMean-sixStDv)) ]
print(dfSixMo)

dfYearOne = dfYearOne[  (dfYearOne["DGS1"] > (oneYearMean+oneYearStDv)) | (dfYearOne["DGS1"] < (oneYearMean-oneYearStDv)) ]
print(dfYearOne)

dfYearFive = dfYearFive[  (dfYearFive["DGS5"] > (fiveYearMean+fiveYearStDv)) | (dfYearFive["DGS5"] < (fiveYearMean-fiveYearStDv)) ]
print(dfYearFive)

dfYearTen = dfYearTen[  (dfYearTen["DGS10"] > (yearTenMean+yearTenStDv)) | (dfYearTen["DGS10"] < (yearTenMean-yearTenStDv)) ]
print(dfYearTen)


###############
## STEP FOUR ##
###############
dfJoin = dfSixMo.join(dfYearOne,how='inner').join(dfYearFive,how='inner').join(dfYearTen,how='inner')
print(dfJoin)


###############
## STEP FIVE ##
###############
dfJoin.to_csv('sigma.csv') ##change to xlsx in excel?? Or do I use .to_xml? Or just write 'sigma.xlsx' after to.csv?
# dfJoin.to_excel('sigma.xlsx')
# dfJoin.to_excel()