import pandas as pd


# if __name__ == '__main__':
def search(searchResults):
    total = 0
    totalAvg = 0
    totalNumber = 0
    prunedResults = pd.DataFrame()
    print("Enter the target date.")
    transSearch = input("Date (MM/DD/YYYY): ")
    transSearch = transSearch[:5].replace('0', '') + transSearch[5:]
    for each in range(len(searchResults)):
        dbDate = searchResults.iloc[each]['Date']
        print("Comparing ", dbDate, " to ", transSearch)
        if transSearch == dbDate:
            result = searchResults.iloc[each]
            total = total + searchResults.iloc[each]['Amount']
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
