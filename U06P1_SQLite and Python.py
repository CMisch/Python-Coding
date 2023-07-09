#This program will use SQLite3 lib to perform common database tasks using Python
#Created by Chris Misch

#Import libraries 
import sqlite3 as sq

#Connect to the SQL database
conn = sq.connect('Contacts.db')

#Creates a cursor object to execute SQL queries
curs = conn.cursor()

#Create a contact table with the following columns
curs.execute(''' CREATE TABLE IF NOT EXISTS contact(
id INTEGER PRIMARY KEY AUTOINCREMENT,
FirstName TEXT CHECK(LENGTH(FirstName) <= 50),
LastName TEXT CHECK(LENGTH(LastName) <= 50),
PhoneNumber TEXT CHECK(LENGTH(PhoneNumber) <= 15),
EmailAddress TEXT CHECK(LENGTH(EmailAddress) <= 50)
)''')


#Create 5 fictitious contacts and insert data
curs.execute("INSERT INTO contacts (FirstName, LastName, PhoneNumber, EmailAddress) VALUES (?, ?, ?, ?)", ('John', 'Connor', '999-562-5241', 'jconnor@gmail.com'))
curs.execute("INSERT INTO contacts (FirstName, LastName, PhoneNumber, EmailAddress) VALUES (?, ?, ?, ?)", ('Mary', 'Smith', '999-883-1258', 'msmith@gmail.com'))
curs.execute("INSERT INTO contacts (FirstName, LastName, PhoneNumber, EmailAddress) VALUES (?, ?, ?, ?)", ('Ralph', 'Machio', '999-883-9874', 'rmachio@gmail.com'))
curs.execute("INSERT INTO contacts (FirstName, LastName, PhoneNumber, EmailAddress) VALUES (?, ?, ?, ?)", ('Peter', 'Filez', '999-562-7531', 'pfilez@gmail.com'))
curs.execute("INSERT INTO contacts (FirstName, LastName, PhoneNumber, EmailAddress) VALUES (?, ?, ?, ?)", ('Jane', 'Fonda', '999-562-1943', 'jfonda@gmail.com'))
#Saves any changes to the database
conn.commit()

#Execute a SELECT statment to retrieve all columns of data 
curs.execute("SELECT * FROM contact")

#Create a for loop to print out contents from contacts
rows = curs.fetchall()
for row in rows:
    print(f"ID: {row[0]}, First Name: {row[1]}, Last Name: {row[2]}, Phone Number: {row[3]}, Email Address: {row[4]} ")
    
#closes the connection and cursor
curs.close()
conn.close()
