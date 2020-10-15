#!/usr/bin/env python3

from sqlalchemy import MetaData
from sqlalchemy import Table, Column
from sqlalchemy import Integer, String
from sqlalchemy import create_engine
from sqlalchemy import Index
from sqlalchemy import String, Numeric, DateTime, Enum
from sqlalchemy import ForeignKey
from sqlalchemy import inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.pool import StaticPool


metadata = MetaData()


#user_table = Table('user', metadata,
#                   Column('id', Integer, primary_key=True),
#                   Column('name', String),
#                   Column('fullname', String)
#                   )

#print(user_table.c)

#print(user_table.select())
#print(user_table.delete())
#print(user_table.insert())
#print(user_table.update())

# Define the DB engine
#engine = create_engine('sqlite:///myUserDB.sqlite', convert_unicode=True)

# Create all tables (from metadata)
#metadata.create_all(engine)

# Drop the table
#user_table.drop(engine)

# Create only user_table
#user_table.create(engine)

# Example with different types
#fancy_table = Table('fancy', metadata,
#                    Column('id', Integer, ForeignKey('user.id')), # Use tablename.field in the ForeignKey.
#                    Column('key', String(50), primary_key=True),
#                    Column('timestamp', DateTime),
#                    Column('amount', Numeric(10, 2)),
#                    Column('type', Enum('a', 'b', 'c'))
#                    )
#fancy_table.create(engine)

#Index('idx', user_table.c.name, user_table.c.fullname)

# Auto table. Load from existing table "fancy"
#metadata2 = MetaData()
#reflect_table = Table('fancy', metadata2, autoload=True, autoload_with=engine)
#metadata2.create_all(engine)

# Create all tables (from metadata)
#metadata.create_all(engine)

#inspector = inspect(engine)
#print(inspector.get_table_names())
#print(inspector.get_columns('fancy'))
#print(inspector.get_foreign_keys('fancy'))


# Declarative DB. Creates automatically during the codding
engine = create_engine('sqlite:///myUserDB.sqlite', poolclass=StaticPool, convert_unicode=True, echo=False)

from sqlalchemy.orm import scoped_session, sessionmaker
Base = declarative_base()
Base.metadata.create_all(engine)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=True,
                                         bind=engine))
session = db_session()


class User(Base): # inheriting from Base class is required
    __tablename__ = 'userclass' # Table name also requirement

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String)
    fullname = Column(String)

    email = relationship("Email", backref="userclass", order_by="Email.id")

    def __init__(self, name, fullname):
        #super(User, self).__init__() # not an requrement. Optional
        self.name, self.fullname = name, fullname
        print(f"The User class from Basic")

    def __repr__(self):
        # print(f"{a=}") --> a=<__main__.User object at 0x7fbd930f0e50>
        # This function doing like this a=self.name='Test', self.fullname='Testing Testovich'
        return f"{self.name=}, {self.fullname=}, {self.email=}"


class Email(Base):
    __tablename__ = 'mail'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('userclass.id'))
    email_address = Column(String)

    def __repr__(self):
        return f"{self.email_address}"


mail1 = Email(email_address="box1@null.com")
mail2 = Email(email_address="box2@null.com")
mail3 = Email(email_address="box3@null.com")


a = User(name="Test", fullname="Testing Testovich")
a.email = [mail1, mail2, mail3]

session.add(a)

session.commit()

print(f"{a=}")
print(f"{a.email=}")

