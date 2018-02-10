import pyodbc
def rowToString(row):
    rowStr = ""
    for i in range(0, 9):
        rowStr = rowStr + str(row[i]) + " ";
    return rowStr

server = 'connextionopps.database.windows.net'
database = 'Opportunities'
username = 'connextion'
password = 'T1n4andEmm4andM1r4nd4!'
driver = '{ODBC Driver 13 for SQL Server}'
cnxn = cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("SELECT * FROM programs WHERE cost=0")
row = cursor.fetchone()
while row:
    print (rowToString(row))
    row = cursor.fetchone()
