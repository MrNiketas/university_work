import sqlite3

conn = sqlite3.connect('accountant.db')
cursor = conn.cursor()

cursor.execute("insert into profile values (55, 'nick', 21, 'tmb', 'm', 'link', 'lox')")
conn.commit()

cursor.execute("select * from profile")
results=cursor.fetchall()
print(results)

conn.close()