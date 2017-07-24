import MySQLdb


db = MySQLdb.connect("localhost","prasad","modi","mysql" )


cursor = db.cursor()


cursor.execute("DROP TABLE IF EXISTS Customer")


sql = """CREATE TABLE Customer (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1) )"""

cursor.execute(sql)

sql2 = """INSERT INTO Customer(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M')"""
try:

   cursor.execute(sql2)

   db.commit()
except:

   db.rollback()

sql3 = """UPDATE Customer SET AGE = AGE + 1
                          WHERE SEX = '%c'" % ('M')"""
try:

   cursor.execute(sql3)

   db.commit()
except:

   db.rollback()

sql4 = "DELETE FROM Customer WHERE AGE > '%d'" % (20)
try:

   cursor.execute(sql4)

   db.commit()
except:

   db.rollback()

db.close()