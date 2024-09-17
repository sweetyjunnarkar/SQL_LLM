import sqlite3

#connect to sqllite

connection=sqlite3.connect('student.db')

#crete cursor to execute the command

cursor=connection.cursor()

#create the table

table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS INT);
"""
cursor.execute(table_info)

#insert some more data

cursor.execute('''INSERT INTO STUDENT values('Sweety','AI','A',95)''')
cursor.execute('''INSERT INTO STUDENT values('Shubham','Testing','A',98)''')
cursor.execute('''INSERT INTO STUDENT values('Srisha','Data Science','A',99)''')
cursor.execute('''INSERT INTO STUDENT values('Chinmay','Maths','B',95)''')
cursor.execute('''INSERT INTO STUDENT values('Shashikant','Arts','A',100)''')
cursor.execute('''INSERT INTO STUDENT values('Anvi','Dance','C',85)''')

#display all the records 

print("The inserted records are: ")

data=cursor.execute('''Select * from STUDENT''')

for row in data:
    print(row)

#close the connection

connection.commit()
connection.close()