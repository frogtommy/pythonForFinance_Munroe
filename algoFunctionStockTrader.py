# An "algorithmical" trader routine
# Sends certain commands to the function that will read the client's portfolio(clients.csv) and
# determine what action to take based on the command, stock and price.

def doAlgo(command, stock, price):
    file = open("clients.csv","r")
    dict = {}
    lines = file.readlines()
    for line in lines[1:]:
        line = line.strip()
        columns = line.split(',')
        colName = columns[0]
        colPosition = columns[1]
        colAmount = columns[2]
    ##instead of dictionary.get, use "if name column in dict, then do command, if not do this command
        if command == 'SELL':
            if colPosition == stock and colName in dict:
                dict[colName] += float(colAmount)
            if colPosition == stock and not(colName in dict):
                dict[colName] = float(colAmount)
            else:
                continue
        if command == 'BUY':
            if colPosition == "CASH":
                dict[colName] = int(int(colAmount)/int(price))
            else:
                continue
    return dict

print(doAlgo("SELL","BRDG",200))
#that should return {'Vlas Lezin': 232.0}

print(doAlgo("SELL","AAPL",200))
# that should return {'Elizabeth Jones': 295.0, 'Robert Williams': 125.0, 'William Brown': 286.0}

print(doAlgo("SELL","SNAP",2000))
#{'James Jones': 387.0, 'Barbara Johnson': 836.0, 'Barbara Brown': 271.0, 'James Williams': 114.0}

print(doAlgo("SELL","GZPRM",300))
#that should return empty dictionary

print(doAlgo("BUY","GZPRM",30))
#that should return
# {'John Brown': 1032, 'William Smith': 362, 'Robert Smith': 769, 'Marry Johnson': 286, 'Robert Williams': 378, 'Marry Williams': 603}

print(doAlgo("BUY","MSFT",300))
#{'John Brown': 103, 'William Smith': 36, 'Robert Smith': 76, 'Marry Johnson': 28, 'Robert Williams': 37, 'Marry Williams': 60}
