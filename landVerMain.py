#! python3
# testScraper.py - Parse HTML for property report webpage for deeded owner and their address.
import openpyxl
from openpyxl import load_workbook
from openpyxl import Workbook
import requests
from bs4 import BeautifulSoup


def extractOwner(stew):
    x = stew.find(id='ctlBodyPane_ctl01_ctl01_lstOwner_ctl01_lnkOwnerName_lnkSearch')  # id is associated with deeded owner in source code
    owner = x.text  # get any text out of html file
    return owner


def extractAddress(stew):
    tdLst = stew.find(id='ctlBodyPane_ctl01_ctl01_lstOwner_ctl01_lblOwnerAddress')
    addressFunc = tdLst.text
    return addressFunc


def getLastNameList(wsName):
    x = 1
    cells = []
    for i in wsName:
        cell = wsName.cell(row=x, column=3).value
        cells.append(cell)
        x += 1
        if i is False: print(i)
    return cells


def lastNameCheck(a, b):
    if a[0] in b:
        return True
    else:
        return False


url = 'https://beacon.schneidercorp.com/Application.aspx?AppID=129&LayerID=1554&PageType' \
      'ID=4&PageID=817&KeyValue=41-06-20-022-006.000-006'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# xlFile = input('Enter .xlsx file to open: ')  # reference spreadsheet
wb1 = openpyxl.load_workbook('johnsonCoExample.xlsx')  # open spreadsheet
ws1 = wb1.active

# xlFile2 = input('Enter name for new output .xlsx file: ')
wb2 = Workbook('johnsonCo2.xlsx')
ws2 = wb2.active

owner = extractOwner(soup)  # extracts deeded owners name from HTML
address = extractAddress(soup)  # extracts deeded owners mailing address from HTML

lastNames = getLastNameList(ws1)  # get list of last names from Excel document
ownerSplit = owner.split()  # split string 'owner' into component words

print(lastNameCheck(ownerSplit, lastNames))
