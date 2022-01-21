import sqlite3

 


#QAuery the DB and return all records
def show_all():
	#connect to the database 
	conn=sqlite3.connect('student.db')
	#creat a cursor
	c = conn.cursor()
	

	#Query the database
	c.execute("SELECT rowid, * FROM students")
	items = c.fetchall()

	for item in items:
		print(item)

	# commit our connection
	conn.commit()
	# closeour connection
	conn.close()


def add_one(student_id,first_name,last_name,phone_number,email,adress):
	conn=sqlite3.connect('student.db')
	# creat a cursor
	c = conn.cursor()
	c.execute("INSERT INTO students VALUES (?,?,?,?,?,?)" , (student_id,first_name,last_name,phone_number,email,adress))
	# commit our command
	conn.commit()
	# close our command
	conn.close()
	

# Supprimer Un Contact
def delete_one(id):
	conn=sqlite3.connect('student.db')
	# creat a cursor
	c = conn.cursor()
	c.execute("DELETE from students WHERE rowid = (?)", id)
	# commit our command and close connection
	conn.commit()
	conn.close()



	# Rechercher un contact par son numéro de téléphone
def phone_lookup(phone_number):
	conn=sqlite3.connect('student.db')
	# creat a cursor
	c = conn.cursor()
	c.execute("SELECT * from students WHERE phone_number = (?)", (phone_number,))
	items = c.fetchall()

	for item in items:
		print(item)


	# commit our command and close connection
	conn.commit()
	conn.close()
	
def update_one(last_name):
	conn=sqlite3.connect('student.db')
	# creat a cursor
	c = conn.cursor()
	c.execute("UPDATE students SET last_name=('Diop') WHERE rowid=14")
	# commit our command and close connection
	conn.commit()
	conn.close()