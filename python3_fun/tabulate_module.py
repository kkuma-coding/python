from tabulate import tabulate

# filling a table
table = [("harry","92389329365905","12.05.1999"),
         ("jimmy","75029364948203","07.11.2001"),
         ("elena","65936583368493","14.10.1995"),
         ("maria","21823749184648","30.02.1999")]


header = ["Name", "Phone Number", "Birth Date"]

print(tabulate(table, headers=header, tablefmt="grid"))

table = [["spam",42],["eggs",451],["bacon",0]]
headers = ["item", "qty"]
print(tabulate(table, headers, tablefmt="plain"))