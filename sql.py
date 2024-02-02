import sqlite3

## Connect to sqlite
connection = sqlite3.connect("student.db")

## Create a cursor object to insert record,create table, retrieve
cursor = connection.cursor()

## Create the table
table_info = """
    Create table STUDENT(Name varchar(25), Class varchar(25),
    Section varchar(25), Marks int
    );
"""

cursor.execute(table_info)

## Insert some records

cursor.execute('''Insert Into Student values('Shubham','Platform engineering','C','60')''')
cursor.execute('''Insert Into Student values('Singh','Platform engineering','B','65')''')
cursor.execute('''Insert Into Student values('Kunal','Platform engineering','C','69')''')
cursor.execute('''Insert Into Student values('Preetam','Devops','A','70')''')
cursor.execute('''Insert Into Student values('Prem','Devops','A','80')''')

## Display all the records

print("The inserted records are")
data = cursor.execute('''Select * from Student''')

for row in data:
    print(row)


## Close the conenction
connection.commit()
connection.close()