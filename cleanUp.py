import pandas as pd

if __name__ == '__main__':
    print('Function call error.')


def encodeValue(data, column):
    # Reiterated function that replaces actual values in a column with numbers
    data[column] = data[column].astype('category')
    data[column] = data[column].cat.codes
    data[column] = data[column].astype('int')


def newData():
    # Pulls new data into the dataframe. Currently not viable.
    print('Retrieving new information')
    # Add additional input to allow user to coose the file path
    bankingData = pd.read_csv(r'./export.csv')
    bankingData = bankingData.drop('Memo', 1)
    # Drop the memo column, which is useless.
    return bankingData


def fixVendor(vendor, row):
    # Prompts the user to enter a vendor name that is not in the vendor name dataframe
    foundB = 'no'
    print(vendor)
    correctedVendor = input("Please enter a succinct vendor name: ")
    bankingData.at[row, 'Name'] = correctedVendor
    # correctSplit = correctedVendor.split(" ")
    for each in range(len(vendorList)):
        if vendorList.iloc[each][0] == correctedVendor:
            # Check 1
            print("Vendor already in database.")
            foundB = 'yes'
    if foundB == 'no':
        addVendor(correctedVendor)

def fixDate():
    for each in range(len(bankingData)):
        getDate = bankingData.iloc[each][0]
        dateSplit = getDate.split("/")
        newDate = dateSplit[2] + "/" + dateSplit[1] + "/"+dateSplit[0]
        bankingData.iloc[each][0] = newDate


def addVendor(vendor):
    dfLength = len(vendorList) + 1
    vendorList.loc[dfLength] = vendor
    vendorList.to_pickle("./vendorList.pkl")


# def vendorCheck(vendorFendor): #Check and see if the input vendor name is already stored in the vendor list,
# searching error implied. Add additional columns to appropriate row for alias vendor names for each in range(len(
# vendorList)): storedVendor = vendorList.iloc[each][0] if (vendorFendor == storedVendor): print("Vendor already in
# database.") found = 'yes' return changeVendor = addVendor(vendorFendor)

def dbCheck(vendor, currentRow):
    found = "no"
    splitLine = vendor.split(" ")
    if len(splitLine) > 2:
        del splitLine[0]
        del splitLine[0]
    # print(vendor)
    # Take the raw vendor name passed to this function, split it by spaces
    for each in splitLine:
        if found == "yes":
            break
        # for each element created by the vendor line split
        for all in range(len(vendorList)):
            if found == "yes":
                break
            # for each vendor stored in the vendor list
            dfVendor = vendorList.iloc[all][0]
            dfSplit = dfVendor.split(" ")
            # store the present iterated vendor
            # print(each.lower(), ",", dfVendor.lower())
            for everyVendor in dfSplit:
                searchFor = each.lower().find(everyVendor.lower())
                if each.lower() == everyVendor.lower():
                    # if they are the same on lower case, a match has been made & save it
                    # print("Match.")
                    bankingData.at[currentRow, 'Vendor'] = dfVendor
                    found = "yes"
                elif searchFor is not -1:
                    bankingData.at[currentRow, 'Vendor'] = dfVendor
                    found = "yes"
                if each.lower() == "amzn":
                    bankingData.at[currentRow, 'Vendor'] = "Amazon"
                    found = "yes"
    # Two breaks inserted to ensure a quick exit if a match is made
    # Otherwise, the vendor is not in the database and needs to be added.
    if found == "no":
        fixVendor(vendor, currentRow)


global bankingData
bankingData = pd.read_pickle("./bankingData.pkl")

print("Welcome to the transaction editor. Please correct each entry that was not fixed by the system. ")
global vendorList
vendorList = pd.read_pickle("./vendorList.pkl")
option = input("Would you like to reset the dataframe? ")
if option.lower() == 'yes':
    addData = newData()
    bankingData = addData
bankingData['Vendor'] = "Null"
for row in range(len(bankingData)):
    currentLine = bankingData.iloc[row][2]
    # print("Checking {}".format(currentLine), end="/r")
    # This ideally limits dispaly to one line for checks
    dbCheck(currentLine, row)

print("Saving dataset.")
bankingData.to_pickle("./bankingData.pkl")
bankingData.to_html("./bankingData.html")
bankingData.to_csv("./bankingData.csv")

# dataframe.iloc[row][column]

# bankingData.to_sql('test', con=engine)
