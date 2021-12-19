import psycopg2
from psycopg2 import Error
import random

class RandomClasses:
    def __init__(self):
        self.id = 0  
        self.name = ""
        self.teacher = 0

    def random(self, n):
        res = n
        names = ['Math', 'English', 'Geography', 'History', 'PE', 'Ukrainian', 'Literature', 'Sciense', 'Law']
        try:
            connection = psycopg2.connect(user="postgres",
                                        password="1",
                                        host="127.0.0.1",
                                        port="5432",
                                        database="school")
            cursor = connection.cursor()
            cursor.execute("DROP TABLE IF EXISTS classes; CREATE TABLE classes(id integer NOT NULL, name text, teacher integer);")
            for i in range(n):
                try:
                    name = names[random.randint(0, len(names) - 1)]                  
                    cursor.execute("INSERT INTO classes (id, name, teacher) VALUES ((SELECT trunc(random() * %s + 1)::int), %s, (SELECT trunc(random() * %s + 1)::int))", [n, name, n])
                except(Exception, Error) as error:
                    print("Error with PostgreSQL", error)
                    res-=1
                connection.commit()
        except (Exception, Error) as error:
            print("Error with PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
        print(str(res) + " Entities added.")

class RandomTeachers:
    def __init__(self):
        self.id = 0  
        self.name = ""
        self.surname = ""

    def random(self, n):
        res = n
        names = ['Inna', 'Kyrulo', 'Anna', 'Igor', 'Ivan', 'Evgeniya', 'Lesya', 'Sergey', 'Alla', 'Andriy']
        surnames = ['Kyrychenko', 'Lightman', 'Anfisov', 'Soldatenko', 'Kravchuk', 'Los', 'Tkach', 'Shevchenko', 'Ivanov', 'Petrov', 'Sydorov']
        try:
            connection = psycopg2.connect(user="postgres",
                                        password="1",
                                        host="127.0.0.1",
                                        port="5432",
                                        database="school")
            cursor = connection.cursor()
            cursor.execute("DROP TABLE IF EXISTS teachers; CREATE TABLE teachers(id integer NOT NULL, name text, surname text)")
            for i in range(n):
                try:
                    name = names[random.randint(0, len(names) - 1)]
                    surname = surnames[random.randint(0, len(names) - 1)]
                    cursor.execute("INSERT INTO teachers (id, name, surname) VALUES ((SELECT trunc(random() * %s + 1)::int), %s, %s)", [n, name, surname])
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

class RandomGroups:
    def __init__(self):
        self.id = 0  
        self.name = ""
        self.year = 0
        self.num_of_exc = 0
        self.teacher = 0

    def random(self, n):
        res = n
        names = ['Math', 'Linguistic', 'History', 'Sciense']
        try:
            connection = psycopg2.connect(user="postgres",
                                        password="1",
                                        host="127.0.0.1",
                                        port="5432",
                                        database="school")
            cursor = connection.cursor()
            cursor.execute("DROP TABLE IF EXISTS groups; CREATE TABLE groups(id integer NOT NULL, name text, year integer, num_of_exc integer, teacher integer)")
            for i in range(n):
                try:
                    name = names[random.randint(0, len(names) - 1)]
                    cursor.execute("INSERT INTO groups (id, name, year, num_of_exc, teacher) VALUES ((SELECT trunc(random() * %s + 1)::int), %s, (SELECT trunc(random() * 11 + 1)::int), (SELECT trunc(random() * %s + 1)::int), (SELECT trunc(random() * %s + 1)::int))", [n, name, n, n])
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