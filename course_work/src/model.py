import psycopg2
from psycopg2 import Error

class Classes:
    def __init__(self):
        self.id = 0  
        self.name = ""
        self.teacher = 0
     
    def create(self, id, name, teacher):
        if (id < 1):
            print('Error with input!')
            return 
        try:
            connection = psycopg2.connect(user="postgres",
                                        password="1",
                                        host="127.0.0.1",
                                        port="5432",
                                        database="school")
            cursor = connection.cursor()
            insert_query = """ INSERT INTO classes (id, name, teacher) VALUES (%s, %s, %s)"""
            item_tuple = (id, name, teacher)
            cursor.execute(insert_query, item_tuple)
            connection.commit()
            print("Entity inserted")

        except (Exception, Error) as error:
            print("Error with PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
    
    def update(self, id, name, teacher):
        if (id < 1):
            print('Error with input!')
            return  
        try:
            connection = psycopg2.connect(user="postgres",
                                        password="1",
                                        host="127.0.0.1",
                                        port="5432",
                                        database="school")
            cursor = connection.cursor()
            update_query = """Update classes SET name=%s, teacher=%s WHERE id = %s"""
            item_tuple = (name, teacher, id)
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
                                            database="school")
            cursor = connection.cursor()
            cursor.execute("Delete from classes WHERE id = %s;", [id])
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
                                            database="school")
            cursor = connection.cursor()
            selecr_query = """SELECT * from classes WHERE id = %s"""
            item_tuple = [id]
            cursor.execute(selecr_query, item_tuple)
            connection.commit()
            records = cursor.fetchall()
            print("Result:")
            for row in records:
                print("Id = ", row[0], "Name = ", row[1], "Teacher  = ", row[2])
        except (Exception, Error) as error:
            print("Error with PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
    

class Teachers:
    def __init__(self):
        self.id = 0  
        self.name = ""
        self.surname = ""

    def create(self, id, name, surname):
        if (id < 1):
            print('Error with input!')
            return 
        try:
            connection = psycopg2.connect(user="postgres",
                                        password="1",
                                        host="127.0.0.1",
                                        port="5432",
                                        database="school")
            cursor = connection.cursor()
            insert_query = """ INSERT INTO teachers (id, name, surname) VALUES (%s, %s, %s)"""
            item_tuple = (id, name, surname)
            cursor.execute(insert_query, item_tuple)
            connection.commit()
            print("Entity inserted")

        except (Exception, Error) as error:
            print("Error with PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
    
    def update(self, id, name, surname):
        if (id < 1):
            print('Error with input!')
            return  
        try:
            connection = psycopg2.connect(user="postgres",
                                        password="1",
                                        host="127.0.0.1",
                                        port="5432",
                                        database="school")
            cursor = connection.cursor()
            update_query = """Update teachers SET name=%s, surname=%s WHERE id = %s"""
            item_tuple = (name, surname, id)
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
                                            database="school")
            cursor = connection.cursor()
            cursor.execute("Delete from classes WHERE teacher = %s; Delete from groups WHERE teacher = %s; Delete from teachers WHERE id = %s;", [id, id, id])
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
                                            database="school")
            cursor = connection.cursor()
            selecr_query = ("SELECT * from teachers WHERE id = %s")
            item_tuple = [id]
            cursor.execute(selecr_query, item_tuple)
            connection.commit()
            records = cursor.fetchall()
            print("Result:")
            for row in records:
                print("Id = ", row[0], "Name = ", row[1], "Surname  = ", row[2])
        except (Exception, Error) as error:
            print("Error with PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
    

class Groups:
    def __init__(self):
        self.id = 0  
        self.name = ""
        self.year = 0
        self.num_of_exc = 0
        self.teacher = 0
    
    def create(self, id, name, year, num_of_exc, teacher):
        if (id < 1):
            print('Error with input!')
            return 
        try:
            connection = psycopg2.connect(user="postgres",
                                        password="1",
                                        host="127.0.0.1",
                                        port="5432",
                                        database="school")
            cursor = connection.cursor()
            insert_query = """ INSERT INTO groups (id, name, year, num_of_exc, teacher) VALUES (%s, %s, %s, %s, %s)"""
            item_tuple = (id, name, year, num_of_exc, teacher)
            cursor.execute(insert_query, item_tuple)
            connection.commit()
            print("Entity inserted")

        except (Exception, Error) as error:
            print("Error with PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
    
    def update(self, id, name, year, num_of_exc, teacher):
        if (id < 1):
            print('Error with input!')
            return  
        try:
            connection = psycopg2.connect(user="postgres",
                                        password="1",
                                        host="127.0.0.1",
                                        port="5432",
                                        database="school")
            cursor = connection.cursor()
            update_query = """Update groups SET name=%s, year=%s, num_of_exc=%s, teacher=%s WHERE id = %s"""
            item_tuple = (name, year, num_of_exc, teacher, id)
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
                                            database="school")
            cursor = connection.cursor()
            cursor.execute("Delete from groups WHERE id = %s;", [id])
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
                                            database="school")
            cursor = connection.cursor()
            selecr_query = """SELECT * from groups WHERE id = %s"""
            item_tuple = [id]
            cursor.execute(selecr_query, item_tuple)
            connection.commit()
            records = cursor.fetchall()
            print("Result:")
            for row in records:
                print("Id = ", row[0], "Name = ", row[1], "Year = ", row[2], "Number of excelent students = ", row[3], "Teacher  = ", row[4])
        except (Exception, Error) as error:
            print("Error with PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()