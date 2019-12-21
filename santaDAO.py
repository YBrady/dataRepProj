import mysql.connector # for sql connections
import dbconfig as cfg # for the connection details

class SantaDAO:
    # Setting the database to null at the start
    db = ""

    # The mySQL connection - taken from the dbconfig file
    def connectToDB(self):
        self.db = mysql.connector.connect(
            host=cfg.mysql['host'],
            user=cfg.mysql['user'],
            password=cfg.mysql['password'],
            database=cfg.mysql['database']
        )

    def __init__(self):
        # Make the connection - here we are specifying the datatbase (datarepresentation)
        self.connectToDB()

    # Creates the cursor
    def getCursor(self):
        # Connect if not already connected
        if not self.db.is_connected():
            self.connectToDB()
        # Return the cursor
        return self.db.cursor()

    # The function to create a student (a row in a database table) - 
    # expecting values to be written in when this function is called
    def createPerson(self, values):
        # Create the cursor
        cursor = self.getCursor()
        # The SQL statement - without actual values
        sql = "insert into people (name, gender, age, nice, toy, chimney) values (%s,%s,%s, %s, %s, %s)"
        # Putting the SQL statement and the values together for execution
        cursor.execute(sql, values)
        # Commit changes to db
        self.db.commit()
        # Record the last row id
        lastRowId = cursor.lastrowid
        # Close the cursor
        cursor.close()
        # Return the id number of the new person created
        return lastRowId


    def createToy(self, values):
        # Create the cursor
        cursor = self.getCursor()
        # The SQL statement - without actual values
        sql = "insert into toys (item, stock) values (%s,%s)"
        # Putting the SQL statement and the values together for execution
        cursor.execute(sql, values)
        # Commit changes to db
        self.db.commit()
        lastRowId = cursor.lastrowid
        # Close the cursor
        cursor.close()
        # Return the id number of the new person created
        return lastRowId
        # Close the cursor

    # Function to return all rows
    def getAllPeople(self):
        # Create the cursor
        cursor = self.getCursor()
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
        # Close the cursor
        cursor.close()
        # Return the converted results
        return returnArray

    def getWorkshop(self, what):
        if what == "both":
            # Create the cursor
            cursor = self.getCursor()
            # Make the select statment
            sql = "select * from toys"
            # Execute the statement
            cursor.execute(sql)
            # Write the results to the results variable
            results = cursor.fetchall()
            # Create a blank array to house the converted results
            returnArray1 = []
            # One by one, for the results
            for result in results:
                # Turn each result into a dictionary object
                returnArray1.append(self.convertToToysDictionary(result))
                
            # The second query
            # Make the select statment - using upper here to negate case sensiivity
            sql = "select id, upper(toy) from people where upper(toy) not in (select upper(item) from toys)"
            # Execute the statement
            cursor.execute(sql)
            # Write the results to the results variable
            results = cursor.fetchall()
            returnArray2 = []
            print(results)
            # One by one, for the results
            for result in results:
                # Turn each result into a dictionary object
                returnArray2.append(self.convertToFakeDictionary(result))
            # Close the cursor
            cursor.close()
            returnArray = {"stock": returnArray1, "make":returnArray2}
            # Return the converted results
            return returnArray

        elif what == "stock":
            # Create the cursor
            cursor = self.getCursor()
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
                returnArray.append(self.convertToToysDictionary(result))
            # Close the cursor
            cursor.close()
            # Return the converted results
            return returnArray
        elif what == "make":
            # Create the cursor
            cursor = self.getCursor()
            # Make the select statment - using upper here to negate case sensiivity
            sql = "select id, upper(toy) from people where upper(toy) not in (select upper(item) from toys)"
            # Execute the statement
            cursor.execute(sql)
            # Write the results to the results variable
            results = cursor.fetchall()
            returnArray = []
            print(results)
            # One by one, for the results
            for result in results:
                # Turn each result into a dictionary object
                returnArray.append(self.convertToFakeDictionary(result))
            # Close the cursor
            cursor.close()
            # Return the converted results
            return returnArray


    # Function to return all rows
    def getAllToys(self):
        # Create the cursor
        cursor = self.getCursor()
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
            returnArray.append(self.convertToToysDictionary(result))
        # Close the cursor
        cursor.close()
        # Return the converted results
        return returnArray

    # Function to determine which toys are not even in production
    def toysToMake(self):
        # Create the cursor
        cursor = self.getCursor()
        # Make the select statment - using upper here to negate case sensiivity
        sql = "select id, upper(toy) from people where upper(toy) not in (select upper(item) from toys)"
        # Execute the statement
        cursor.execute(sql)
        # Write the results to the results variable
        results = cursor.fetchall()
        returnArray = []
        print(results)
        # One by one, for the results
        for result in results:
            # Turn each result into a dictionary object
            returnArray.append(self.convertToFakeDictionary(result))
        # Close the cursor
        cursor.close()
        # Return the converted results
        return returnArray

    # Find a person by their name - will only brng back first if multiple
    def checkPersonByName(self, name):
        # Create the cursor
        cursor = self.getCursor()
        # The SQL statement
        sql = "select * from people where name like %s"
        # Add the values (has to be in brackets with a comma as a tuple is expected)
        values = (name,)
        # Perform the SQL statement
        cursor.execute(sql, values)
        # Collect the results - fetchOne = 1 result
        result = (cursor.fetchone())
        # Close the cursor
        cursor.close()
        # Return the dictionary converted result
        return self.convertToPeopleDictionary(result)


    # Find a person by their id number
    def findPersonByID(self, id):
        # Create the cursor
        cursor = self.getCursor()
        # The SQL statement
        sql = "select * from people where id = %s"
        # Add the values (has to be in brackets with a comma as a tuple is expected)
        values = (id,)
        # Perform the SQL statement
        cursor.execute(sql, values)
        # Collect the results - fetchOne = 1 result
        result = cursor.fetchone()
        # Close the cursor
        cursor.close()
        # Return the dictionary converted result
        return self.convertToPeopleDictionary(result)

    # Find an item by their id number
    def findToysByID(self, itemId):
        # Create the cursor
        cursor = self.getCursor()
        # The SQL statement
        sql = "select * from toys where itemId = %s"
        # Add the values (has to be in brackets with a comma as a tuple is expected)
        values = (itemId,)
        # Perform the SQL statement
        cursor.execute(sql, values)
        # Collect the results - fetchOne = 1 result
        result = cursor.fetchone()
        cursor.close()
        # Return the dictionary converted result
        return self.convertToToysDictionary(result)

    # Function to update a row - assumed new values are entered when calling the function
    def updatePeople(self, values):
        # Create the cursor
        cursor = self.getCursor()
        # Write the SQL statement without the values
        sql = "update people set name= %s, gender = %s, age=%s, nice = %s, toy=%s, chimney=%s where id = %s"
        # Perform the update
        cursor.execute(sql, values)
        # Commit to database
        self.db.commit()
        cursor.close()

    # Function to update a row - assumed new values are entered when calling the function
    def updateToys(self, values):
        # Create the cursor
        cursor = self.getCursor()
        # Write the SQL statement without the values
        sql = "update toys set item= %s, stock = %s where itemId = %s"
        # Perform the update
        cursor.execute(sql, values)
        # Commit to database
        self.db.commit()
        cursor.close()

    # Function to delete a row - assuming id is enered when function is called
    def deletePerson(self, id):
        # Create the cursror
        cursor = self.getCursor()
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
        cursor.close()

    # Function to delete a row - assuming id is enered when function is called
    def deleteToys(self, itemId):
        # Create the cursror
        cursor = self.getCursor()
        # Make the SQL statement without values
        sql = "delete from toys where itemId = %s"
        # Add the values
        values = (itemId,)
        # Execute the SQL statement
        cursor.execute(sql, values)
        # Commit the changes
        self.db.commit()
        # Print as a feedback that the code has executed
        print("delete done")
        cursor.close()


    # Function to convert the return values to dictionary items
    def convertToFakeDictionary(self, result):
        # Create the column names
        colnames = ["id", "toy"]
        item = {}  # blank dictionary object
        # Execute only if the result has something in it
        if result:
            # For every column name
            for i, colName in enumerate(colnames):
                if result[i] is None:
                    item[colName] = ""
                else:
                    # Match the column name with the result based on location in tuple
                    item[colName] = result[i]
        # Return the dictionary-ise item
        return item


    # Function to convert the return values to dictionary items
    def convertToPeopleDictionary(self, result):
        # Create the column names
        colnames = ["id", "name", "gender", "age", "nice", "toy", "chimney"]
        item = {}  # blank dictionary object
        # Execute only if the result has something in it
        if result:
            # For every column name
            for i, colName in enumerate(colnames):
                if result[i] is None:
                    item[colName] = ""
                else:
                    # Match the column name with the result based on location in tuple
                    item[colName] = result[i]
        # Return the dictionary-ise item
        return item

    # Function to convert the return values to dictionary items
    def convertToToysDictionary(self, result):
        # Create the column names
        tcolnames = ["itemId", "item", "stock"]
        item = {}  # blank dictionary object
        # Execute only if the result has something in it
        if result:
            # For every column name
            for i, colName in enumerate(tcolnames):
                # Match the column name with the result based on location in tuple
                item[colName] = result[i]
        # Return the dictionary-ise item
        return item

santaDAO = SantaDAO()
