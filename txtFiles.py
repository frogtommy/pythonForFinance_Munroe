
#  Opens order_book_data.txt
#  Removes the order book lines. i.e. ***** Order Book: ###### *****
#  Gets rid empty lines
#  Gets rid of spaces
#  Notices that there are two currencies in the order book; USD and YEN. Converts both the Bid and Ask oilY to USD
#  Creates a header line ['Symbol,Date,Bid,Ask']
#  Saves the header line and propely formatted lines to a comma seperated value file called mktDataFormat.csv


data = []

orders = open("order_book_data.txt","r")

lines = orders.readlines()
for line in lines:
    line = line.strip() ##get rid of order book lines
    if '*' in line:
        continue
    if len(line) == 0: ##get rid of empty lines
        continue
    if ' ' in line: ##get rid of spaces
        line = line.replace(' ', '')

    columns = line.split(',')

    tickerCol = columns[0]
    dateCol = columns[1]
    bidCol = columns[2]
    askCol = columns[3]
    currencyCol = columns[4]

    if currencyCol == "YEN":
        currencyCol = currencyCol.replace("YEN","USD")
        bidCol = round(float(bidCol) * .0087,  2)
        askCol = round(float(askCol) * .0087, 2)

    data.append(tickerCol + ',')
    data.append(dateCol + ',')
    data.append(str(bidCol) + ',')
    data.append(str(askCol) + ',')
    data.append(currencyCol + '\n')

print(data)

orders.close()


header = ['Ticker,','Date,','Bid,','Ask,','Currency,', '\n']

results = open('new_order_book_data.csv','w')
results.writelines(header)
results.writelines(data)
results.close()



