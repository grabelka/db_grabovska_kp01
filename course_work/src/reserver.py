import psycopg2
from psycopg2 import Error

class Reserver:
    def ClassTrigger(self):
        try:
            connection = psycopg2.connect(user="postgres",
                                            password="1",
                                            host="127.0.0.1",
                                            port="5432",
                                            database="school")
            cursor = connection.cursor()
            query = """DROP TABLE IF EXISTS class_logs;
                        CREATE TABLE class_logs(id integer NOT NULL, name text, teacher integer);
                        CREATE OR REPLACE FUNCTION log_class() RETURNS trigger AS $BODY$
                        BEGIN
                            INSERT INTO class_logs VALUES(OLD.id, OLD.name, OLD.teacher);
                            RETURN NEW;
                        END;
                    $BODY$ LANGUAGE plpgsql;
                    DROP TRIGGER IF EXISTS log_class ON classes;
                    CREATE TRIGGER log_class BEFORE UPDATE OR DELETE ON classes
                        FOR EACH ROW EXECUTE PROCEDURE log_class();"""
            cursor.execute(query)
            connection.commit()
            print('Trigger was created')
        except (Exception, Error) as error:
            print("Error with PostgreSQL", error)
        finally:
            if connection:
                cursor.close()

    def TeacherTrigger(self):
        try:
            connection = psycopg2.connect(user="postgres",
                                            password="1",
                                            host="127.0.0.1",
                                            port="5432",
                                            database="school")
            cursor = connection.cursor()
            query = """DROP TABLE IF EXISTS teacher_logs;
                        CREATE TABLE teacher_logs(id integer NOT NULL, name text, surname text);
                        CREATE OR REPLACE FUNCTION log_teacher() RETURNS trigger AS $BODY$
                        BEGIN
                            INSERT INTO teacher_logs VALUES(OLD.id, OLD.name, OLD.surname);
                            RETURN NEW;
                        END;
                    $BODY$ LANGUAGE plpgsql;
                    DROP TRIGGER IF EXISTS log_teacher ON teachers;
                    CREATE TRIGGER log_teacher BEFORE UPDATE OR DELETE ON teachers
                        FOR EACH ROW EXECUTE PROCEDURE log_teacher();"""
            cursor.execute(query)
            connection.commit()
            print('Trigger was created')
        except (Exception, Error) as error:
            print("Error with PostgreSQL", error)
        finally:
            if connection:
                cursor.close()

    def GroupTrigger(self):
        try:
            connection = psycopg2.connect(user="postgres",
                                            password="1",
                                            host="127.0.0.1",
                                            port="5432",
                                            database="school")
            cursor = connection.cursor()
            query = """DROP TABLE IF EXISTS group_logs;
                        CREATE TABLE group_logs(id integer NOT NULL, name text, year integer, num_of_exc integer, teacher integer);
                        CREATE OR REPLACE FUNCTION log_group() RETURNS trigger AS $BODY$
                        BEGIN
                            INSERT INTO group_logs VALUES(OLD.id, OLD.name, OLD.year, OLD.num_of_exc, OLD.teacher);
                            RETURN NEW;
                        END;
                    $BODY$ LANGUAGE plpgsql;
                    DROP TRIGGER IF EXISTS log_group ON groups;
                    CREATE TRIGGER log_group BEFORE UPDATE OR DELETE ON groups
                        FOR EACH ROW EXECUTE PROCEDURE log_group();"""
            cursor.execute(query)
            connection.commit()
            print('Trigger was created')
        except (Exception, Error) as error:
            print("Error with PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
