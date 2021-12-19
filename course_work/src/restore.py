import psycopg2
from psycopg2 import Error

class Restore:
     
    def Save(self):
        try:
            connection = psycopg2.connect(user="postgres",
                                        password="1",
                                        host="127.0.0.1",
                                        port="5432",
                                        database="school")
            cursor = connection.cursor()
            cursor.execute('SELECT groups.id, groups.name, groups.year, groups.num_of_exc, groups.teacher, teachers.id, teachers.name, teachers.surname, classes.id, classes.name, classes.teacher FROM groups, teachers, classes')
            f = open('copy.backup', 'w')
            for row in cursor:
              f.write("insert into t values (" + str(row) + ");")
            connection.commit()
            print("Database saved")

        except (Exception, Error) as error:
            print("Error with PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()