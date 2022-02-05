#! python3
# testScraper.py - Parse HTML for property report webpage for deeded owner and their address.
import openpyxl
from openpyxl import load_workbook
from openpyxl import Workbook
import requests
from bs4 import BeautifulSoup
import re


# gets a list of last names from database Excel
def getLastNameList(wsName):
    x = 1
    cells = []
    for i in wsName:
        cord = wsName.cell(row=x, column=3).value
        cells.append(cord)
        x += 1
        if i is False: print(i)
    return cells


# get list of street address from database Excel
def getAddressLst1(wsAdr):
    x = 1
    cells = []
    for i in wsAdr:
        cell = wsAdr.cell(row=x, column=1).value
        cells.append(cell)
        x += 1
        if i is False: print(i)
    return cells


# get list of parcel IDs for database Excel
def getPID(wsID):
    x = 1
    cells = []
    for i in wsID:
        cell = wsID.cell(row=x, column=5).value
        cells.append(cell)
        x += 1
        if i is False: print(i)
    return cells


# extracts for webpage a string with deeded landowners full names including trusts if present
def extractOwner(stew):
    # id is different depending on whether landowner name is a
    # link or not. Only  char difference so a regular expression
    # will take care of it.
    x = stew.find(id=re.compile(r"ctlBodyPane_ctl01_ctl01_lstOwner_ctl01_lnkOwnerName_l..Search"))
    ownerA = x.text  # get any text out of html file
    return ownerA


# extracts from webpage a string with deeded landowners mailing address
def extractAddress(stew):
    tdLst = stew.find(id='ctlBodyPane_ctl01_ctl01_lstOwner_ctl01_lblOwnerAddress')
    addressFunc = tdLst.text
    return addressFunc


# checks if last name from website matches the one in Excel, returns a Boolean
def lastNameCheck(a, b, c):
    if a == b[c]:
        return True
    else:
        return False


# checks if address from webpage matches the one in Excel, returns a Boolean
def addressCheck(a, b, c):
    if a in b[c]:
        return True
    else:
        return False


def copyRow(sheet,):
    rowLst = []
    for row in sheet.values:
        rangeLst = []
        for value in row:
            rangeLst.append(value)
        rowLst.append(rangeLst)
    return rowLst

def excelWrite(sheet, data, count):
    for i in range(1, len(data)):
        sheet.cell(row=count, column=i).value = data[i]



xlFile = input('Enter .xlsx file to open: ')  # reference spreadsheet
try:
    wb1 = openpyxl.load_workbook(xlFile)  # open spreadsheet
    ws1 = wb1['Sheet1'] # active sheet database spreadsheet
except:
    print('Error: ' + xlFile + ' failed to open')
    quit()


xlFile2 = input('Enter name for new output .xlsx file: ')
try:
    wb2 = Workbook(xlFile2)
    ws2 = wb2.create_sheet('badData')  # active sheet new spreadsheet
except:
    print('Error: ' + xlFile2 + ' failed to open')
    quit()


databaseLastNames = getLastNameList(ws1)  # get list of last names from Excel document
addressLst1 = getAddressLst1(ws1)  # get list of address in column 1 (street address)
pID = getPID(ws1)


for p in range(1, ws1.max_row):
    url = 'https://beacon.schneidercorp.com/Application.aspx?AppID=129&' \
          'LayerID=1554&PageTypeID=4&PageID=817&KeyValue=' + str(pID[p])

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    owner = extractOwner(soup).split()[0]  # extracts deeded owners name from HTML, splits the string into component
    # works, and assigns the one at index[0], their last name.

    # extracts deeded owners mailing address from HTML, and splits at the end of street address.
    ad1 = extractAddress(soup)
    ad2 = re.split(r'\w*,\s', ad1)
    ad3 = ad2[0].strip()  # selects street address and strips whitespace

    lnCheck = lastNameCheck(owner, databaseLastNames, p)
    cnt = 0
    cnt += 1
    if lnCheck == False:
        orgRow = copyRow(ws1)
        badRow = orgRow
        excelWrite(ws2, badRow[p-1], cnt)
        wb2.save(xlFile2)

    # elif addressCheck(address, addressLst1, p) is False:

print('Done')
