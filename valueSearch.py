import pandas as pd


# if __name__ == '__main__':
def search(searchResults):
    total = 0
    totalAvg = 0
    totalNumber = 0
    prunedResults = pd.DataFrame()
    print('Examples: <50.00, >100.00 or =10.00')
    transSearch = input('Enter an amount: ')
    if transSearch[0] == ">":
        searchAmount = transSearch[1:]
        for transactions in range(len(searchResults)):
            if abs(float(searchResults.iloc[transactions]['Amount'])) > float(searchAmount):
                result = searchResults.iloc[transactions]
                total = total + searchResults.iloc[transactions]['Amount']
                totalNumber = totalNumber + 1
                prunedResults = prunedResults.append(result)
    elif transSearch[0] == "<":
        searchAmount = transSearch[1:]
        for transactions in range(len(searchResults)):
            if abs(float(searchResults.iloc[transactions]['Amount'])) < float(searchAmount):
                result = searchResults.iloc[transactions]
                total = total + searchResults.iloc[transactions]['Amount']
                totalNumber = totalNumber + 1
                prunedResults = prunedResults.append(result)
    elif transSearch[0] == "=":
        searchAmount = transSearch[1:]
        for transactions in range(len(searchResults)):
            if abs(float(searchResults.iloc[transactions]['Amount'])) == float(searchAmount):
                result = searchResults.iloc[transactions]
                total = total + searchResults.iloc[transactions]['Amount']
                totalNumber = totalNumber + 1
                prunedResults = prunedResults.append(result)
    if prunedResults.empty:
        print("No transactions on that date.")
        return searchResults
    else:
        totalAvg = abs(round(total, 2)) / totalNumber
        print(prunedResults)
        print("Total: $", abs(round(total, 2)))
        print("Transactions: ", totalNumber)
        print("Average: $", round(totalAvg, 2))
        return prunedResults
