import timeit
import psycopg2
from psycopg2 import Error
from sqlalchemy import create_engine, Integer, String, \
    Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session, sessionmaker, relationship

Base = declarative_base()

engine = create_engine("postgresql+psycopg2://postgres:1@localhost/university")
Base.metadata.bind = engine
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
engine.connect()

class Curator(Base):
    __tablename__ = 'curators'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(50))
    surname = Column(String(50))
    phone = Column(String(50))
    group = relationship('Group', uselist=False)
    subjects = relationship('Subject')
    __table_args__ = {'extend_existing': True}

class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)  
    name = Column(String(50))
    curator_id = Column(Integer, ForeignKey('curators.id'))
    curator = relationship("Curator", foreign_keys=[curator_id, id, name])
    __table_args__ = {'extend_existing': True}

class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)  
    code = Column(String(50))
    curator_id = Column(Integer, ForeignKey('curators.id'))
    curator = relationship("Curator", foreign_keys=[curator_id, id, code])
    students = relationship("Students")
    __table_args__ = {'extend_existing': True}

class Student(Base):
    __tablename__ = 'curators'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(50))
    surname = Column(String(50))
    group_id = Column(Integer, ForeignKey('groups.id'))
    group = relationship("Group", foreign_keys=[group_id])
    __table_args__ = {'extend_existing': True}

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
            session = Session()
            session.add(Curator(
                id = id,
                name = name,
                surname = surname,
                phone = phone
            ))
            session.commit()
            print("Entity inserted")

        except (Exception, Error) as error:
            print("Error with PostgreSQL", error)
        finally:
            print()
    
    def update(self, id, name, surname, phone):
        if (id < 1):
            print('Error with input!')
            return  
        try:
            i = session.query(Curator).get(id)
            i.name = name
            i.surname = surname
            i.phone = phone
            session.add(i)
            session.commit()
            print("Entity updated")
        except (Exception, Error) as error:
            print("Error with PostgreSQL", error)
        finally:
            print()

    def delete(self, id):
        if (id < 1):
            print('Error with input!')
            return 
        try:
            i = session.query(Curator).get(44)
            session.delete(i)
            session.commit()
            print("Entity deleted")
        except (Exception, Error) as error:
            print("Error with PostgreSQL", error)
        finally:
            print()
        
class groups:

    def __init__(self):  
        self.id = 0  
        self.code = ""  
        self.curator_id = 0  

    def create(self, id, code, c_id):
        if (id < 1):
            print('Error with input!')
            return 
        try:
            session = Session()
            session.add(Group(
                id = id,
                code = code,
                curator_id = c_id
            ))
            session.commit()
            print("Entity inserted")

        except (Exception, Error) as error:
            print("Error with PostgreSQL", error)
        finally:
            print()
    
    def update(self, id, code, c_id):
        if (id < 1):
            print('Error with input!')
            return  
        try:
            i = session.query(Group).get(id)
            i.code = code,
            i.curator_id = c_id
            session.add(i)
            session.commit()
            print("Entity updated")
        except (Exception, Error) as error:
            print("Error with PostgreSQL", error)
        finally:
            print()

    def delete(self, id):
        if (id < 1):
            print('Error with input!')
            return 
        try:
            i = session.query(Group).get(id)
            session.delete(i)
            session.commit()
            print("Entity deleted")
        except (Exception, Error) as error:
            print("Error with PostgreSQL", error)
        finally:
            print()
        
class students:

    def __init__(self):  
        self.id = 0  
        self.name = ""
        self.surname = ""
        self.group_id = 0  
    def create(self, id, name, surname, c_id):
        if (id < 1):
            print('Error with input!')
            return 
        try:
            session = Session()
            session.add(Student(
                id = id,
                name = name,
                surname = surname,
                curator_id = c_id
            ))
            session.commit()
            print("Entity inserted")

        except (Exception, Error) as error:
            print("Error with PostgreSQL", error)
        finally:
            print()
    
    def update(self, id, name, surname, c_id):
        if (id < 1):
            print('Error with input!')
            return  
        try:
            i = session.query(Student).get(id)
            i.name = name
            i.surname = surname
            i.curator_id = c_id
            session.add(i)
            session.commit()
            print("Entity updated")
        except (Exception, Error) as error:
            print("Error with PostgreSQL", error)
        finally:
            print()

    def delete(self, id):
        if (id < 1):
            print('Error with input!')
            return 
        try:
            i = session.query(Student).get(id)
            session.delete(i)
            session.commit()
            print("Entity deleted")
        except (Exception, Error) as error:
            print("Error with PostgreSQL", error)
        finally:
            print()
    
        
class subjects:

    def __init__(self):  
        self.id = 0  
        self.name = ""  
        self.curator_id = 0 

    def create(self, id, name, c_id):
        if (id < 1):
            print('Error with input!')
            return 
        try:
            session = Session()
            session.add(Subject(
                id = id,
                name = name,
                curator_id = c_id
            ))
            print("Entity inserted")
            session.commit()
        except (Exception, Error) as error:
            print("Error with PostgreSQL", error)
        finally:
            print()
    
    def update(self, id, name, c_id):
        if (id < 1):
            print('Error with input!')
            return  
        try:
            i = session.query(Subject).get(id)
            i.name = name,
            i.curator_id = c_id
            session.add(i)
            session.commit()
            print("Entity updated")
        except (Exception, Error) as error:
            print("Error with PostgreSQL", error)
        finally:
            print()

    def delete(self, id):
        if (id < 1):
            print('Error with input!')
            return 
        try:
            i = session.query(Subject).get(id)
            session.delete(i)
            session.commit()
            print("Entity deleted")
        except (Exception, Error) as error:
            print("Error with PostgreSQL", error)
        finally:
            print()

class Index:

    def test(self):
        start = timeit.timeit()
        try:
            connection = psycopg2.connect(user="postgres",
                                            password="1",
                                            host="127.0.0.1",
                                            port="5432",
                                            database="university")
            cursor = connection.cursor()
            selecr_query = """CREATE INDEX ON curators USING BTREE(id); 
                            CREATE INDEX group_code ON groups USING gin (to_tsvector('english', code)); 
                            SELECT curators.name, curators.surname, groups.code from curators, groups 
                            WHERE curators.id = 7 AND groups.curator_id = 7; 
                            SELECT curators.name, curators.surname, groups.code from curators, groups 
                            WHERE curators.id = groups.curator_id AND groups.code LIKE 'KM%'; 
                            SELECT curators.id, curators.name, curators.surname, groups.code from curators, groups 
                            WHERE curators.id = groups.curator_id ORDER BY curators.id;
                            SELECT groups.code from curators, groups 
                            WHERE curators.id = groups.curator_id AND curators.id > 20 GROUP BY groups.code;"""
            cursor.execute(selecr_query)
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

class Trigger:

    def create(self):
        try:
            connection = psycopg2.connect(user="postgres",
                                            password="1",
                                            host="127.0.0.1",
                                            port="5432",
                                            database="university")
            cursor = connection.cursor()
            query = """DROP TABLE IF EXISTS subj_logs;
                        CREATE TABLE subj_logs(id integer NOT NULL, old_name text, new_name text, curator_id integer);
                        CREATE OR REPLACE FUNCTION log_subj() RETURNS trigger AS $BODY$
                        BEGIN
                            IF NEW.name IS NULL THEN
                                RAISE EXCEPTION 'Name cannot be null';
                            END IF;
                            IF NEW.curator_id IS NULL THEN
                                RAISE EXCEPTION 'Subject cannot have null curator id';
                            END IF;
                            INSERT INTO subj_logs VALUES(OLD.id, OLD.name, NEW.name, NEW.curator_id);
                            RETURN NEW;
                        END;
                    $BODY$ LANGUAGE plpgsql;
                    DROP TRIGGER IF EXISTS log_subj ON subjects;
                    CREATE TRIGGER log_subj BEFORE UPDATE OR DELETE ON subjects
                        FOR EACH ROW EXECUTE PROCEDURE log_subj();"""
            cursor.execute(query)
            connection.commit()
            # print("Result", cursor.fetchall())
        except (Exception, Error) as error:
            print("Error with PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close() 