import psycopg2
from psycopg2 import Error

class curators:

    def __init__(self):  
        self.id = 0  
        self.name = ""
        self.surname = ""
        self.phone = ""

    def create(self, id, name, surname, phone):
        if (id < 1):
            print('Error with input!')
            return 
        try:
            connection = psycopg2.connect(user="postgres",
                                        password="1",
                                        host="127.0.0.1",
                                        port="5432",
                                        database="university")
            cursor = connection.cursor()
            insert_query = """ INSERT INTO curators (id, name, surname, phone) VALUES (%s, %s, %s, %s)"""
            item_tuple = (id, name, surname, phone)
            cursor.execute(insert_query, item_tuple)
            connection.commit()
            print("Entity inserted")

        except (Exception, Error) as error:
            print("Error with PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
    
    def update(self, id, name, surname, phone):
        if (id < 1):
            print('Error with input!')
            return  
        try:
            connection = psycopg2.connect(user="postgres",
                                        password="1",
                                        host="127.0.0.1",
                                        port="5432",
                                        database="university")
            cursor = connection.cursor()
            update_query = """Update curators set VALUES (%s, %s, %s, %s)"""
            item_tuple = (id, name, surname, phone)
            cursor.execute(update_query, item_tuple)
            connection.commit()
            count = cursor.rowcount
            print(count, "Entity updated")
        except (Exception, Error) as error:
            print("Error with PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()


    def delete(self, id):
        if (id < 1):
            print('Error with input!')
            return 
        try:
            connection = psycopg2.connect(user="postgres",
                                            password="1",
                                            host="127.0.0.1",
                                            port="5432",
                                            database="university")
            cursor = connection.cursor()
            cursor.execute("Delete from curators WHERE id = %s", [id])
            connection.commit()
            count = cursor.rowcount
            print(count, "Entity deleted")
        except (Exception, Error) as error:
            print("Error with PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
        
    def read(self, id):
        if (id < 1):
            print('Error with input!')
            return 
        try:
            connection = psycopg2.connect(user="postgres",
                                            password="1",
                                            host="127.0.0.1",
                                            port="5432",
                                            database="university")
            cursor = connection.cursor()
            selecr_query = """SELECT * from curators WHERE id = %s"""
            item_tuple = (id,)
            cursor.execute(selecr_query, item_tuple)
            connection.commit()
            print("Result", cursor.fetchall())
        except (Exception, Error) as error:
            print("Error with PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

class groups:

    def __init__(self):  
        self.id = 0  
        self.code = ""  
        self.curator_id = 0  

        
class students:

    def __init__(self):  
        self.id = 0  
        self.name = ""
        self.surname = ""
        self.group_id = 0  

        
class subjects:

    def __init__(self):  
        self.id = 0  
        self.name = ""  
        self.curator_id = 0 