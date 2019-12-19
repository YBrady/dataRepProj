import mysql.connector
import dbconfig as cfg

# Connect to mySQL
mydb = mysql.connector.connect(
    host=cfg.mysql["host"],
    user=cfg.mysql["user"],
    password=cfg.mysql["password"]
)

# Create the cursor
mycursor = mydb.cursor()
#mycursor.execute("DROP DATABASE drproject;")

# Create it again
#mycursor.execute("CREATE DATABASE drproject;")

mycursor.execute("use drproject;")
'''
# Create the tables
# People Table
# Write SQL create statement
sql = "create table people(id int NOT NULL AUTO_INCREMENT, name varchar(250), gender ENUM(\"boy\", \"girl\"), age int, nice ENUM(\"naughty\", \"nice\"), toy varchar(250), chimney ENUM(\"no\", \"yes\"), toyok ENUM(\"not ready\", \"ready\"), PRIMARY KEY(id));"

# Execute
mycursor.execute(sql)

# Toys Table
# Write SQL create statement
sql = "create table toys(itemId int NOT NULL AUTO_INCREMENT, item varchar(250), stock int, PRIMARY KEY(itemId));"

# Execute
mycursor.execute(sql)
'''

# Insert some data into People Table
# Write SQL statement
ins = "insert into people(name, gender, age, nice, toy, chimney) values"
insql = [ins + "(\"John\", \"boy\", 10, \"nice\", \"bike\", \"yes\");"]
insql.append(ins + "(\"Mary\", \"girl\", 8, \"nice\", \"dolls house\", \"yes\");")
insql.append(ins + "(\"Peter\", \"boy\", 6, \"naughty\", \"bb gun\", \"yes\");")
insql.append(ins + "(\"Anne\", \"girl\", 11, \"nice\", \"x-box\", \"no\");")
insql.append(ins + "(\"Emily\", \"girl\", 7, \"naughty\", \"new teacher\", \"no\");")
# Execute
for ins in insql:
    mycursor.execute(ins)
'''
# Insert some data into Toys Table
# Write SQL statement
ins = "insert into toys (item, stock) values"
insql = [ins + "(\"bike\", 20);"]
insql.append(ins + "(\"doll\", 17);")
insql.append(ins + "(\"playstation\", 25);")
insql.append(ins + "(\"hula hoop\", 5);")
insql.append(ins + "(\"jigsaw\", 15);")
insql.append(ins + "(\"book\", 110);")
insql.append(ins + "(\"new baby brother\", 3);")
insql.append(ins + "(\"diamond necklace\", 1);")
insql.append(ins + "(\"hurley\", 13);")
insql.append(ins + "(\"x-box\", 0);")

# Execute
for ins in insql:
    mycursor.execute(ins)
'''