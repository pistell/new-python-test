import sqlite3

conn = sqlite3.connect("new.db")
cursor = conn.cursor()

#insert data to db 
cursor.execute("INSERT INTO population VALUES('New York City', 'NY', '8200000')")
cursor.execute("INSERT INTO population VALUES('San Francisco', 'CA', '3440202')")

#commit the changes
conn.commit()

#close connection to db 
conn.close()