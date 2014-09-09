import sqlite3

#using the 'with' keyword your changes to the db will automatically be added 
#without having to specify commit()

with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	#insert multiple records using a tuple
	cities = [
			('Boston', 'MA', 650039),
			('Chicago', 'IL', 270000),
			('Houston', 'TX', 5484897),
			('Phoenix', 'AZ', 5454999)
			]
#insert data into table using executemany()
#c.executemany('INSERT INTO population VALUES(?, ?, ?)', cities)
	c.executemany("INSERT INTO population VALUES(?, ?, ?)", cities)


