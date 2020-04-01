import mysql.connector


"""
    Responsible for 'Customers' database access
"""
class Customers:
    #-----------------------------------------------------------------------
    #        Constructor
    #-----------------------------------------------------------------------
    def __init__(self):
        self.db = mysql.connector.connect(
            database="mvc",
            host="127.0.0.1",
            user="root",
            charset="utf8"
        )
        
        self.c = self.db.cursor()
    
    
    #-----------------------------------------------------------------------
    #        Methods
    #-----------------------------------------------------------------------
    """
        Adds a customer in database
        
        @param fields Data of the customer to be added
        @return Record of specified id
    """
    def add(self, fields):
        response = 0
        
        try:
            self.c.execute("INSERT INTO customers (first_name, last_name, zipcode, price_paid) VALUES (%s, %s, %s, %s)",
                       (fields[0].get(), fields[1].get(), fields[2].get(), fields[3].get()))
            response = self.c.rowcount
        except:
            pass
        
        return response
            
    """
        Returns all records in database
        
        @return List of all customers
    """
    def getAll(self):
        self.c.execute("SELECT * FROM customers")
        return self.c.fetchall()
    
    """
        Returns the record with a specific id
        
        @param int id Id of the record
        @return Record of specified id
    """
    def get(self, id):
        self.c.execute("SELECT * FROM customers WHERE id = %s", (id, ))
        return self.c.fetchone()
    
    """
        Updates a record in database
        
        @param fields Data of the customer to be updated
        @return List of affected database rows
    """
    def update(self, fields):
        self.c.execute("UPDATE customers SET first_name = %s, last_name = %s, zipcode = %s, price_paid = %s WHERE id = %s",
        (
            fields[1].get(),
            fields[2].get(),
            fields[3].get(),
            fields[4].get(),
            fields[0].get()
        ))
        self.db.commit()

        return self.c.rowcount
    
    """
        Delete a customer in database
        
        @param id_customer Id of the customer
    """
    def delete(self, id_customer):
        self.c.execute("DELETE FROM customers WHERE id = %s", (id_customer, ))
        return self.c.rowcount