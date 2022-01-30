# landownerVerification
The goal of this project is to create a program that will:
1) Reference excel exported from a database
2) Copy value (parcel id) and enter it into search bar of county website
3) Get parse the current deeded landowner and their mailing address from webpage HTML
4) If they don't match or parcel search returns no result, copy landowner information
   from database spreadsheet to new file for manual lookup
5) [optional] Copy current landowner information to the new file along with the old.
   Will save from having to manually lookup
6) [optional] Use regular expressions to ensure that parcel id is in the proper format
   before searching.
