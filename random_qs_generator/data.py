import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user = <add username>,
  passwd = <add your password>,
  database = <create a database, enter the name here>
)

mycursor = mydb.cursor()
## uncomment all lines to add data to your database ##
### THE ADDED DATA HAS BEEN COMMENTED... TO ADD MORE QUESTIONS ADD RESPECTIVE QUERIES ###
#### Tables created ####
#mycursor.execute("CREATE TABLE OOPS (questions TEXT)")
#mycursor.execute("CREATE TABLE DSA (questions TEXT)")
#mycursor.execute("CREATE TABLE COA (questions TEXT)")
#mycursor.execute("SHOW TABLES")
#for x in mycursor:
#    print(x)

### insert questions in OOPS Table ###
#sql = "INSERT INTO OOPS (questions) VALUES (%s)"
#val = ("What is a class?")
#mycursor.execute(sql, (val,))
#sql = "INSERT INTO OOPS (questions) VALUES (%s)"
#val = ("What is an object?")
#mycursor.execute(sql, (val,))
#sql = "INSERT INTO OOPS (questions) VALUES (%s)"
#val = ("What is a structure?")
#mycursor.execute(sql, (val,))
#sql = "INSERT INTO OOPS (questions) VALUES (%s)"
#val = ("What is inheritance?")
#mycursor.execute(sql, (val,))
#sql = "INSERT INTO OOPS (questions) VALUES (%s)"
#val = ("What is polymorphism?")
#mycursor.execute(sql, (val,))
#sql = "INSERT INTO OOPS (questions) VALUES (%s)"
#val = ("What is abstraction?")
#mycursor.execute(sql, (val,))
#sql = "INSERT INTO OOPS (questions) VALUES (%s)"
#val = ("What is a virtual function?")
#mycursor.execute(sql, (val,))
#sql = "INSERT INTO OOPS (questions) VALUES (%s)"
#val = ("What is abstract class?")
#mycursor.execute(sql, (val,))
#sql = "INSERT INTO OOPS (questions) VALUES (%s)"
#val = ("What is the difference between OOP and POP?")
#mycursor.execute(sql, (val,))
#sql = "INSERT INTO OOPS (questions) VALUES (%s)"
#val = ("What is VPTR and VTABLE?")
#mycursor.execute(sql, (val,))
#mydb.commit()
### insert questions in DSA table ###
#sql = "INSERT INTO DSA (questions) VALUES (%s)"
#val = ("What is a data structure?")
#mycursor.execute(sql, (val,))
#sql = "INSERT INTO DSA (questions) VALUES (%s)"
#val = ("Code and illustrate Shortest Path Algorithms.")
#mycursor.execute(sql, (val,))
#sql = "INSERT INTO DSA (questions) VALUES (%s)"
#val = ("What is a trie? Perform insert and search.")
#mycursor.execute(sql, (val,))
#sql = "INSERT INTO DSA (questions) VALUES (%s)"
#val = ("What is Binary Search?")
#mycursor.execute(sql, (val,))
#sql = "INSERT INTO DSA (questions) VALUES (%s)"
#val = ("What is a MST? Code Prim's Algorithm")
#mycursor.execute(sql, (val,))
#sql = "INSERT INTO DSA (questions) VALUES (%s)"
#val = ("Code LCS, 0-1 Knapsnack with space and time complexities.")
#mycursor.execute(sql, (val,))
#sql = "INSERT INTO DSA (questions) VALUES (%s)"
#val = ("What is a linkedlist? Write a code to reverse a linkedlist")
#mycursor.execute(sql, (val,))
#sql = "INSERT INTO DSA (questions) VALUES (%s)"
#val = ("What is a binary search tree? Perform insertion in the same")
#mycursor.execute(sql, (val,))
#sql = "INSERT INTO DSA (questions) VALUES (%s)"
#val = ("What is a Stack? Illustrate")
#mycursor.execute(sql, (val,))
#sql = "INSERT INTO DSA (questions) VALUES (%s)"
#val = ("What is recursion? Illustrate with a stack")
#mycursor.execute(sql, (val,))
#mydb.commit()
### insert questions in COA table ###
#sql = "INSERT INTO COA (questions) VALUES (%s)"
#val = ("What is ISA? Explain all it's types")
#mycursor.execute(sql, (val,))
#sql = "INSERT INTO COA (questions) VALUES (%s)"
#val = ("What is Caching? Explain with diagram")
#mycursor.execute(sql, (val,))
#sql = "INSERT INTO COA (questions) VALUES (%s)"
#val = ("What is TLB? Explain.")
#mycursor.execute(sql, (val,))
#sql = "INSERT INTO COA (questions) VALUES (%s)"
#val = ("What is LRU and FIFO mechanism")
#mycursor.execute(sql, (val,))
#sql = "INSERT INTO COA (questions) VALUES (%s)"
#val = ("What is the difference between primary memory and secondary memory?")
#mycursor.execute(sql, (val,))
#sql = "INSERT INTO COA (questions) VALUES (%s)"
#val = ("What is data path and control path?")
#mycursor.execute(sql, (val,))
#sql = "INSERT INTO COA (questions) VALUES (%s)"
#val = ("What is paging?")
#mycursor.execute(sql, (val,))
#sql = "INSERT INTO COA (questions) VALUES (%s)"
#val = ("What is stack based organisation?")
#mycursor.execute(sql, (val,))
#sql = "INSERT INTO COA (questions) VALUES (%s)"
#val = ("What are the different types of instruction sets?")
#mycursor.execute(sql, (val,))
#sql = "INSERT INTO COA (questions) VALUES (%s)"
#val = ("Briefly explain processor design.")
#mycursor.execute(sql, (val,))
#mydb.commit()
#mycursor.execute("SELECT * FROM COA AS Questions")
#mycursor.execute("SELECT * FROM DSA")
##mycursor.execute("SELECT * FROM COA")
#myresult=mycursor.fetchall()
#for x in myresult:
#    print(x)
