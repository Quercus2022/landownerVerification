# landownerVerification
The goal of this project is to create a program that will:
1) Reference excel exported from a database
2) Copy value (parcel id) and enter it into search bar of county website
3) Parse the current deeded landowner and their mailing address from webpage HTML and check against our records for landownership
4) If they don't match or parcel search returns no result, copy landowner information
   from database spreadsheet to new file for manual lookup
---------------------------------------------------------------------------------------------------------------
I decided to keep things simple and instead of copying the landowner information to a new file it highlights erronious rows in red and rows with correct info in green, then saves the output as a new file.

Formatting differences between our datatbase and how deed landowners are recorded on the Beacon website lead to a significant number of false negatives (indicating that land ownership or mailing address had changed when it hadn't).

However, I haven't found a single false positive yet. That means that the program as is can still be a useful tool when doing landowner verification as you can trust that the green rows are verified. This cuts down on how many property records you need to investigate.
