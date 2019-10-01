import pyodbc

DBfile = r"D:\accessFile\test1.accdb"

conn = pyodbc.connect(r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=" + DBfile + ";Uid=;Pwd=;")

cursor = conn.cursor()
SQL = "SELECT * FROM USER;"
for row in cursor.execute(SQL):
    print(row)
cursor.close()
conn.close()