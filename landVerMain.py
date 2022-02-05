#! python3
# testScraper.py - Parse HTML for property report webpage for deeded owner and their address.
import openpyxl
from openpyxl import load_workbook
from openpyxl import Workbook
import requests
from bs4 import BeautifulSoup
import re


def getLastNameList(wsName):
    x = 1
    cells = []
    for i in wsName:
        cell = wsName.cell(row=x, column=3).value
        cells.append(cell)
        x += 1
        if i is False: print(i)
    return cells


def getAddressLst1(wsAdr):
    x = 1
    cells = []
    for i in wsAdr:
        cell = wsAdr.cell(row=x, column=1).value
        cells.append(cell)
        x += 1
        if i is False: print(i)
    return cells


def extractOwner(stew):
    # id is different depending on whether landowner name is a
    # link or not. Only  char difference so a regular expression
    # will take care of it.
    x = stew.find(id=re.compile('ctlBodyPane_ctl01_ctl01_lstOwner_ctl01_lnkOwnerName_l..Search'))
    owner = x.text  # get any text out of html file
    return owner


def extractAddress(stew):
    tdLst = stew.find(id='ctlBodyPane_ctl01_ctl01_lstOwner_ctl01_lblOwnerAddress')
    addressFunc = tdLst.text
    return addressFunc


def lastNameCheck(a, b):
    if a in b:
        return True
    else:
        return False


def addressCheck(a, b):
    if a in b:
        return True
    else:
        return False


# xlFile = input('Enter .xlsx file to open: ')  # reference spreadsheet
# try:
wb1 = openpyxl.load_workbook('johnsonCoExample.xlsx')  # open spreadsheet
# except:
#    print('Error: ' + xlFile + ' failed to open')
#    quit()
ws1 = wb1.active  # active sheet database spreadsheet

# xlFile2 = input('Enter name for new output .xlsx file: ')
#try:
wb2 = Workbook('johnsonCo2.xlsx')
# except:
#    print('Error: ' + xlFile + ' failed to open')
#    quit()
ws2 = wb2.active  # active sheet new spreadsheet

databaseLastNames = getLastNameList(ws1)  # get list of last names from Excel document
addressLst1 = getAddressLst1(ws1)  # get list of address in column 1 (street address)

url = 'https://beacon.schneidercorp.com/Application.aspx?AppID=129&' \
    'LayerID=1554&PageTypeID=4&PageID=817&KeyValue=41-09-32-043-001.000-034'
#  main(url)
###################################################
# for i in range(ws1.max_row): ?
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

owner = extractOwner(soup).split()[0]  # extracts deeded owners name from HTML, splits
# the string into compenent works, and assigns the one at index[0], their last name.

# extracts deeded owners mailing address from HTML, and splits at the end of street address.
address = re.split('\w+,\s', extractAddress(soup))
address = address[0].strip()  # selects street address and strips whitespace

#if lastNameCheck(owner, databaseLastNames) is False:




#if
