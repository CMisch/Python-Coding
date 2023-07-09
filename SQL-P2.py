#Create a SELECT statement that contains only FirstName, LastName, and EmailAddress from the contacts table.
#Create an UPDATE statement that updates a contacts EmailAddress and PhoneNumber.
#Delete the information for the last contact added to the contacts table.
#Execute a SELECT statement to retrieve all the columns of data from your contacts table.

#Created by Chris Misch

import sqlite3 as sq

#Retrieve database and set cursor
conn = sq.connect('C:\\Users\\themi\Desktop\Desktop Tabs\Capella University\Course Classes\IT4079_Python Scripting\Contacts.db')
curs = conn.cursor()

#Use a select statment that contains only FirstName, LastName, and EmailAddress
curs.execute("SELECT FirstName, LastName, EmailAddress FROM contacts")
rows = curs.fetchall()
for row in rows:
    print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")

# Update data in the table
#curs.execute("UPDATE employees SET age = ? WHERE name = ?", (35, 'John Doe'))
#conn.commit()
#
## Delete data from the table
#curs.execute("DELETE FROM employees WHERE name = ?", ('Jane Smith',))
#conn.commit()
#
#
##close the connection
#curs.close()
#conn.close()
