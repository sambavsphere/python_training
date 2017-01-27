import sqlite3

con = sqlite3.connect('db1.db')

query = "create table users(id int,name varchar(20))"

cur = con.cursor()
#cur.execute(query)

query = ""
