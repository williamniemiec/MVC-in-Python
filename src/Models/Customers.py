import mysql.connector

class Customers:
    def __init__(self):
        self.db = mysql.connector.connect(
            database="mvc",
            host="127.0.0.1",
            user="root",
            charset="utf8"
        )
        
        self.c = self.db.cursor()
        
    def add(self, fields):
        response = 0
        
        try:
            self.c.execute("INSERT INTO customers (first_name, last_name, zipcode, price_paid) VALUES (%s, %s, %s, %s)",
                       (fields[0].get(), fields[1].get(), fields[2].get(), fields[3].get()))
            response = self.c.rowcount
        except:
            pass
        
        return response
            
        
        
    def getAll(self):
        self.c.execute("SELECT * FROM customers")
        return self.c.fetchall()
    
    def get(self, id):
        self.c.execute("SELECT * FROM customers WHERE id = %s", (id, ))
        return self.c.fetchone()
    
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
        
    def delete(self, id_customer):
        self.c.execute("DELETE FROM customers WHERE id = %s", (id_customer, ))
        return self.c.rowcount