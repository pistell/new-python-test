import sqlite3
with sqlite3.connect("new.db") as connection:
	c = connection.cursor()

	#update data
	c.execute("UPDATE population SET population = 9001 WHERE city='New York City'")
	#delete data
	c.execute("DELETE FROM population WHERE city='Boston'")

	print "\nNEW DATA: \n"

	c.execute("SELECT * FROM population")

	rows = c.fetchall()

	for r in rows:
		print r[0], r[1], r[2]









	#c.execute("SELECT city, state, population from population")
	#fetchall() retreives all records from the query
	#rows = c.fetchall()
	#output rows on screen, row by fucking row
	#for r in rows:
	#	print r[0], r[1], r[2]


	#use a for loop to iterate through the db and print results by line
	#for row in c.execute("SELECT city, state, population from population"):
	#	print row