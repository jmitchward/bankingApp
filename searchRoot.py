import pandas as pd

bankingData = pd.read_pickle("./bankingData.pkl")
vendorList = pd.read_pickle("./vendorList.pkl")


def menu():
    print('Menu: ')
    print("1. View Banking Transactions.")
    print("2. View Vendor List.")
    print("3. Search Banking Transactions.")
    print("4. Edit Vendor List.")
    print("0. Exit")
    return input("Select: ")


def searchMenu(result):
    print("Enter 'Close' for a new search.")
    target = input("Would you like to further search by date, vendor or value?")
    if target.lower() == "date":
        import dateSearch
        dateSearch.search(result)
    elif target.lower() == "vendor":
        import vendorSearch
        vendorSearch.search(result)
    elif target.lower() == "value":
        import valueSearch
        valueSearch.search(result)
    elif target.lower() == "close":
        menu()
    else:
        print("Invalid choice.")
        searchMenu(result)


returnSearch = pd.DataFrame()
select = menu()

while select != 0:

    if select == "1":
        for each in range(len(bankingData)):
            print(bankingData.iloc[each])
        select = menu()

    elif select == "2":
        for each in range(len(vendorList)):
            print(vendorList.iloc[each][0])
        select = menu()

    elif select == "3":
        criterion = input("Search by date, name or amount? ")
        searchResults = pd.DataFrame()
        if criterion.lower() == "date":
            import dateSearch
            returnSearch = dateSearch.search(bankingData)
            prune = input("Would you like to get more specific?")
            if prune.lower() == 'yes':
                searchMenu(returnSearch)
            else:
                continue
        elif criterion.lower() == "name":
            import vendorSearch
            returnSearch = vendorSearch.search(bankingData)
            prune = input("Would you like to get more specific?")
            if prune.lower() == 'yes':
                searchMenu(returnSearch)
            else:
                continue
        elif criterion.lower() == "amount":
            import valueSearch
            returnSearch = valueSearch.search(bankingData)
            prune = input("Would you like to get more specific?")
            if prune.lower() == 'yes':
                searchMenu(returnSearch)
            else:
                continue
        elif criterion.lower() == "exit":
            select = 0
        else:
            print("Invalid selection!")
            continue
    # There is an issue with secondary searches using dates.
