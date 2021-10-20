import timeit
import psycopg2
from psycopg2 import Error

class curators:

    def __init__(self):  
        self.id = 0  
        self.name = ""
        self.surname = ""
        self.phone = ""

    def readGroup(self, c, code):
        start = timeit.timeit()
        if (c < 1):
            print('Error with input!')
            return 
        try:
            connection = psycopg2.connect(user="postgres",
                                            password="1",
                                            host="127.0.0.1",
                                            port="5432",
                                            database="university")
            cursor = connection.cursor()
            selecr_query = """SELECT curators.name, curators.surname, groups.code from curators, groups WHERE curators.id = %s AND groups.curator_id = %s AND groups.code LIKE %s"""
            item_tuple = (c, c, code + "%")
            cursor.execute(selecr_query, item_tuple)
            connection.commit()
            print("Result", cursor.fetchall())
        except (Exception, Error) as error:
            print("Error with PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
                end = timeit.timeit()
                print("Time for operation " + str(end - start))

    def readSubject(self, c, surname):
        start = timeit.timeit()
        if (c < 1):
            print('Error with input!')
            return 
        try:
            connection = psycopg2.connect(user="postgres",
                                            password="1",
                                            host="127.0.0.1",
                                            port="5432",
                                            database="university")
            cursor = connection.cursor()
            selecr_query = """SELECT curators.name, curators.surname, subjects.name from curators, subjects WHERE curators.id = %s AND subjects.curator_id = %s AND curators.surname LIKE %s"""
            item_tuple = (c, c, surname + "%")
            cursor.execute(selecr_query, item_tuple)
            connection.commit()
            print("Result", cursor.fetchall())
        except (Exception, Error) as error:
            print("Error with PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
                end = timeit.timeit()
                print("Time for operation " + str(end - start))

    def readStudent(self, c, s):
        start = timeit.timeit()
        if (c < 1):
            print('Error with input!')
            return 
        try:
            connection = psycopg2.connect(user="postgres",
                                            password="1",
                                            host="127.0.0.1",
                                            port="5432",
                                            database="university")
            cursor = connection.cursor()
            selecr_query = """SELECT curators.name, curators.surname, groups.code, students.name, students.surname from curators, groups, students WHERE curators.id = %s AND groups.curator_id = %s AND students.surname LIKE %s"""
            item_tuple = (c, c, s + "%")
            cursor.execute(selecr_query, item_tuple)
            connection.commit()
            print("Result", cursor.fetchall())
        except (Exception, Error) as error:
            print("Error with PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
                end = timeit.timeit()
                print("Time for operation " + str(end - start))

    def random(self, n):
        res = n
        for i in range(n):
            try:
                connection = psycopg2.connect(user="postgres",
                                            password="1",
                                            host="127.0.0.1",
                                            port="5432",
                                            database="university")
                cursor = connection.cursor()
                try:
                    cursor.execute("INSERT INTO curators (id, name, surname, phone) VALUES ((SELECT trunc(random() * %s + 1)::int), (SELECT chr(trunc(random() * 25 + 65)::int) || chr(trunc(random() * 25 + 97)::int) || chr(trunc(random() * 25 + 97)::int)), (SELECT chr(trunc(random() * 25 + 65)::int) || chr(trunc(random() * 25 + 97)::int) || chr(trunc(random() * 25 + 97)::int)), (SELECT trunc(random() * 999999 + 1)::int))", [n])
                except:
                    res-=1
                connection.commit()
            except (Exception, Error) as error:
                print("Error with PostgreSQL", error)
            finally:
                if connection:
                    cursor.close()
                    connection.close()
        print(str(res) + " Entities added.")

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
            update_query = """Update curators SET name=%s, surname=%s, phone=%s WHERE id = %s"""
            item_tuple = (name, surname, phone, id)
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
            cursor.execute("Delete from subjects WHERE curator_id = %s; Delete from groups WHERE curator_id = %s; Delete from curators WHERE id = %s", [id, id, id])
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
            item_tuple = (id)
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

    def random(self, n):
        res = n
        for i in range(n):
            try:
                connection = psycopg2.connect(user="postgres",
                                            password="1",
                                            host="127.0.0.1",
                                            port="5432",
                                            database="university")
                cursor = connection.cursor()
                try:
                    cursor.execute("INSERT INTO groups (id, code, curator_id) VALUES ((SELECT trunc(random() * %s + 1)::int), (SELECT chr(trunc(random() * 25 + 65)::int) || chr(trunc(random() * 25 + 65)::int) || chr(trunc(random() + 45)::int) || chr(trunc(random() * 10 + 48)::int) || chr(trunc(random() * 10 + 48)::int)), (SELECT trunc(random() * %s + 1)::int))", [n, n])
                except:
                    res-=1
                connection.commit()
            except (Exception, Error) as error:
                print("Error with PostgreSQL", error)
            finally:
                if connection:
                    cursor.close()
                    connection.close()
        print(str(res) + " Entities added.")

    def create(self, id, code, c_id):
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
            insert_query = """ INSERT INTO groups (id, code, curator_id) VALUES (%s, %s, %s)"""
            item_tuple = (id, code, c_id)
            cursor.execute(insert_query, item_tuple)
            connection.commit()
            print("Entity inserted")

        except (Exception, Error) as error:
            print("Error with PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
    
    def update(self, id, code, c_id):
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
            update_query = """Update groups SET code=%s, curator_id=%s WHERE id = %s"""
            item_tuple = (code, c_id, id)
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
            cursor.execute("Delete from students WHERE group_id = %s; Delete from groups WHERE id = %s", [id, id])
            connection.commit()
            count = cursor.rowcount
            print(count, "Entity deleted")
        except (Exception, Error) as error:
            print("Error with PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
        
class students:

    def __init__(self):  
        self.id = 0  
        self.name = ""
        self.surname = ""
        self.group_id = 0  

    def random(self, n):
        res = n
        for i in range(n):
            try:
                connection = psycopg2.connect(user="postgres",
                                            password="1",
                                            host="127.0.0.1",
                                            port="5432",
                                            database="university")
                cursor = connection.cursor()
                try:
                    cursor.execute("INSERT INTO students (id, name, surname, group_id) VALUES ((SELECT trunc(random() * %s + 1)::int), (SELECT chr(trunc(random() * 25 + 65)::int) || chr(trunc(random() * 25 + 97)::int) || chr(trunc(random() * 25 + 97)::int)), (SELECT chr(trunc(random() * 25 + 65)::int) || chr(trunc(random() * 25 + 97)::int) || chr(trunc(random() * 25 + 97)::int)), (SELECT trunc(random() * %s + 1)::int))", [n, n])
                except:
                    res-=1
                connection.commit()
            except (Exception, Error) as error:
                print("Error with PostgreSQL", error)
            finally:
                if connection:
                    cursor.close()
                    connection.close()
        print(str(res) + " Entities added.")

    def create(self, id, name, surname, group_id):
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
            insert_query = """ INSERT INTO students (id, name, surname, group_id) VALUES (%s, %s, %s, %s)"""
            item_tuple = (id, name, surname, group_id)
            cursor.execute(insert_query, item_tuple)
            connection.commit()
            print("Entity inserted")

        except (Exception, Error) as error:
            print("Error with PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
    
    def update(self, id, name, surname, group_id):
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
            update_query = """Update students name=%s, surname=%s, group_id=%s WHERE id = %s"""
            item_tuple = (name, surname, group_id, id)
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
            cursor.execute("Delete from students WHERE id = %s", [id])
            connection.commit()
            count = cursor.rowcount
            print(count, "Entity deleted")
        except (Exception, Error) as error:
            print("Error with PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
        
class subjects:

    def __init__(self):  
        self.id = 0  
        self.name = ""  
        self.curator_id = 0 

    def random(self, n):
        res = n
        for i in range(n):
            try:
                connection = psycopg2.connect(user="postgres",
                                            password="1",
                                            host="127.0.0.1",
                                            port="5432",
                                            database="university")
                cursor = connection.cursor()
                try:
                    cursor.execute("INSERT INTO subjects (id, name, curator_id) VALUES ((SELECT trunc(random() * %s + 1)::int), (SELECT chr(trunc(random() * 25 + 65)::int) || chr(trunc(random() * 25 + 65)::int)), (SELECT trunc(random() * %s + 1)::int))", [n, n])
                except:
                    res-=1
                connection.commit()
            except (Exception, Error) as error:
                print("Error with PostgreSQL", error)
            finally:
                if connection:
                    cursor.close()
                    connection.close()
        print(str(res) + " Entities added.")

    def create(self, id, name, c_id):
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
            insert_query = """ INSERT INTO subjects (id, name, curator_id) VALUES (%s, %s, %s)"""
            item_tuple = (id, name, c_id)
            cursor.execute(insert_query, item_tuple)
            connection.commit()
            print("Entity inserted")

        except (Exception, Error) as error:
            print("Error with PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
    
    def update(self, id, name, c_id):
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
            update_query = """Update subjects SET name=%s, curator_id=%s WHERE id = %s"""
            item_tuple = (name, c_id, id)
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
            cursor.execute("Delete from subjects WHERE id = %s", [id])
            connection.commit()
            count = cursor.rowcount
            print(count, "Entity deleted")
        except (Exception, Error) as error:
            print("Error with PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()