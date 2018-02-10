import pyodbc
server = 'connextionopps.database.windows.net'
database = 'opportunities'
username = 'connextion'
password = 'T1n4andEmm4andM1r4nd4!'
driver = '{ODBC Driver 13 for SQL Server}'
cnxn = cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("SELECT * FROM programs")
row = cursor.fetchone()
while row:
    print (str(row[0]) + " " + str(row[1]))
    row = cursor.fetchone()
