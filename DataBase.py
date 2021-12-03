import sqlite3

con = sqlite3.connect("login.db")

cursor = con.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users
(Id INTEGER NOT NULL PRIMARY KEY,
Usuario TEXT NOT NULL,
Senha TEXT NOT NULL);
""")
