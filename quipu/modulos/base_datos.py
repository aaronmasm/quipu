import sqlite3

conexionDB = sqlite3.connect('database.db')

cursorObj = conexionDB.cursor()

cursorObj.execute('CREATE TABLE usuarios (ID INTEGER(11) PRIMARY KEY, usuario VARCHAR(50), password VARCHAR(200))')

conexionDB.close()
