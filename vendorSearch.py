import pandas as pd


# if __name__ == '__main__':
def search(searchResults):
    total = 0
    totalAvg = 0
    totalNumber = 0
    prunedResults = pd.DataFrame()
    transSearch = input('Vendor Name: ')
    for names in range(len(searchResults)):
        vendor = searchResults.iloc[names]['Vendor']
        if vendor.lower() == transSearch.lower():
            result = searchResults.iloc[names]
            prunedResults = prunedResults.append(result)
            total = total + searchResults.iloc[names]['Amount']
            totalNumber = totalNumber + 1
    # Write an illustration for total amount and number of transactions
    if prunedResults.empty or len(prunedResults) == 0:
        print("No transactions found for", transSearch, ".")
        return searchResults
    else:
        totalAvg = abs(round(total, 2)) / totalNumber
        print(prunedResults)
        print("Total: $", abs(round(total, 2)))
        print("Transactions: ", totalNumber)
        print("Average: $", round(totalAvg, 2))
        return prunedResults
