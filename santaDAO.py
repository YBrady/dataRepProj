import mysql.connector
import dbconfig as cfg

class SantaDAO:
    # Setting the database to null at the start
    db = ""
    def __init__(self):
        # Make the connection - here we are specifying the datatbase (datarepresentation)
        self.db = mysql.connector.connect(
            host=cfg.mysql["host"],
            user=cfg.mysql["user"],
            password=cfg.mysql["password"],
            database=cfg.mysql["database"]
        )

    # The function to create a student (a row in a database table) - 
    # expecting values to be written in when this function is called
    def createPerson(self, values):
        # Create the cursor
        cursor = self.db.cursor()
        # The SQL statement - without actual values
        sql = "insert into people (name, gender, age, nice, toy, chimney) values (%s,%s, %s,%s, %s, %s)"
        # Putting the SQL statement and the values together for execution
        cursor.execute(sql, values)
        # Commit changes to db
        self.db.commit()
        # Return the id number of the new person created
        return cursor.lastrowid

    def createStock(self, values):
        # Create the cursor
        cursor = self.db.cursor()
        # The SQL statement - without actual values
        sql = "insert into toys (item, stock) values (%s,%s)"
        # Putting the SQL statement and the values together for execution
        cursor.execute(sql, values)
        # Commit changes to db
        self.db.commit()
        # Return the id number of the new person created
        return cursor.lastrowid

    # Function to return all rows
    def getAllPeople(self):
        # Create the cursor
        cursor = self.db.cursor()
        # Make the select statment
        sql = "select * from people"
        # Execute the statement
        cursor.execute(sql)
        # Write the results to the results variable
        results = cursor.fetchall()
        # Create a blank array to house the converted results
        returnArray = []
        # One by one, for the results
        for result in results:
            # Turn each result into a dictionary object
            returnArray.append(self.convertToPeopleDictionary(result))
        # Return the converted results
        return returnArray


    # Function to return all rows
    def getAllStock(self):
        # Create the cursor
        cursor = self.db.cursor()
        # Make the select statment
        sql = "select * from toys"
        # Execute the statement
        cursor.execute(sql)
        # Write the results to the results variable
        results = cursor.fetchall()
        # Create a blank array to house the converted results
        returnArray = []
        # One by one, for the results
        for result in results:
            # Turn each result into a dictionary object
            returnArray.append(self.convertToStockDictionary(result))
        # Return the converted results
        return returnArray

    # Find a person by their id number
    def findPersonByID(self, id):
        # Create the cursor
        cursor = self.db.cursor()
        # The SQL statement
        sql = "select * from people where id = %s"
        # Add the values (has to be in brackets with a comma as a tuple is expected)
        values = (id,)
        # Perform the SQL statement
        cursor.execute(sql, values)
        # Collect the results - fetchOne = 1 result
        result = cursor.fetchone()
        # Return the dictionary converted result
        return self.convertToPeopleDictionary(result)

    # Find an item by their id number
    def findStockByID(self, id):
        # Create the cursor
        cursor = self.db.cursor()
        # The SQL statement
        sql = "select * from toys where itenId = %s"
        # Add the values (has to be in brackets with a comma as a tuple is expected)
        values = (id,)
        # Perform the SQL statement
        cursor.execute(sql, values)
        # Collect the results - fetchOne = 1 result
        result = cursor.fetchone()
        # Return the dictionary converted result
        return self.convertToStockDictionary(result)

    # Function to update a row - assumed new values are entered when calling the function
    def updatePeople(self, values):
        # Create the cursor
        cursor = self.db.cursor()
        # Write the SQL statement without the values
        sql = "update people set name= %s, gender = %s, age=%s, nice = %s, toy=%s, chimney=%s, toyok=%s where id = %s"
        # Perform the update
        cursor.execute(sql, values)
        # Commit to database
        self.db.commit()

    # Function to update a row - assumed new values are entered when calling the function
    def updateStock(self, values):
        # Create the cursor
        cursor = self.db.cursor()
        # Write the SQL statement without the values
        sql = "update toys set item= %s, stock = %s where id = %s"
        # Perform the update
        cursor.execute(sql, values)
        # Commit to database
        self.db.commit()


    # Function to delete a row - assuming id is enered when function is called
    def deletePerson(self, id):
        # Create the cursror
        cursor = self.db.cursor()
        # Make the SQL statement without values
        sql = "delete from people where id = %s"
        # Add the values
        values = (id,)
        # Execute the SQL statement
        cursor.execute(sql, values)
        # Commit the changes
        self.db.commit()
        # Print as a feedback that the code has executed
        print("delete done")

    # Function to delete a row - assuming id is enered when function is called
    def deleteStock(self, id):
        # Create the cursror
        cursor = self.db.cursor()
        # Make the SQL statement without values
        sql = "delete from toys where id = %s"
        # Add the values
        values = (id,)
        # Execute the SQL statement
        cursor.execute(sql, values)
        # Commit the changes
        self.db.commit()
        # Print as a feedback that the code has executed
        print("delete done")

    # Function to convert the return values to dictionary items
    def convertToPeopleDictionary(self, result):
        # Create the column names
        colnames = ["id", "name", "gender", "age", "nice", "toy", "chimney", "toyok"]
        item = {}  # blank dictionary object
        # Execute only if the result has something in it
        if result:
            # For every column name
            for i, colName in enumerate(colnames):
                # Match the column name with the result based on location in tuple
                item[colName] = result[i]
        # Return the dictionary-ise item
        return item

    # Function to convert the return values to dictionary items
    def convertToStockDictionary(self, result):
        # Create the column names
        colnames = ["itenId", "Item", "Stock"]
        item = {}  # blank dictionary object
        # Execute only if the result has something in it
        if result:
            # For every column name
            for i, colName in enumerate(colnames):
                # Match the column name with the result based on location in tuple
                item[colName] = result[i]
        # Return the dictionary-ise item
        return item

bookDAO = BookDAO()
