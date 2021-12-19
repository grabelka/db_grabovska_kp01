import psycopg2
from psycopg2 import Error

class Index:

    def Create(self):
        try:
            connection = psycopg2.connect(user="postgres",
                                            password="1",
                                            host="127.0.0.1",
                                            port="5432",
                                            database="school")
            cursor = connection.cursor()
            selecr_query = """CREATE INDEX class_index ON classes USING BTREE(id); CREATE INDEX  ON groups USING BTREE(id); CREATE INDEX ON teachers USING BTREE(id);"""
            cursor.execute(selecr_query)
            connection.commit()
            print("Indexes were created.")
        except (Exception, Error) as error:
            print("Error with PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()

    def Drop(self):
        try:
            connection = psycopg2.connect(user="postgres",
                                            password="1",
                                            host="127.0.0.1",
                                            port="5432",
                                            database="school")
            cursor = connection.cursor()
            selecr_query = """DROP INDEX class_index; DROP INDEX group_index; DROP INDEX teacher_index; """
            cursor.execute(selecr_query)
            connection.commit()
            print("Indexes were created.")
        except (Exception, Error) as error:
            print("Error with PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
