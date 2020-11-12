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
from sqlalchemy.orm import scoped_session, sessionmaker


# Declarative DB. Creates automatically during the codding
engine = create_engine('sqlite:///db/myUserDB.sqlite', poolclass=StaticPool, convert_unicode=True, echo=False)
Base = declarative_base()

# It's a requirement to use sessions!
db_session = scoped_session(sessionmaker(autocommit=True, # Means automatically run session.commit()
                                         autoflush=True, # Means automatically run session.flush() to write the file
                                         bind=engine))

# The session cursor
session = db_session()


class User(Base): # inheriting from Base class is required
    """
    Relationships btw User and email. You unable to add one more user id/name field with the same data
    """
    __tablename__ = 'userclass' # Table name also requirement

    id = Column(Integer)
    name = Column(String, primary_key=True, nullable=False, unique=True)
    fullname = Column(String, nullable=True)

    email = relationship("Email", backref="userclass", order_by="Email.id")

    def __init__(self, name, fullname):
        super(User, self).__init__() # not an requirement. Optional
        self.name, self.fullname = name, fullname
        print(f"The User class from Basic")

    def __repr__(self):
        # The func name it's a shortname of "represent" word.
        # print(f"{a=}") --> a=<__main__.User object at 0x7fbd930f0e50>
        # This function doing like this a=self.name='Test', self.fullname='Testing Testovich'
        return f"{self.name=}, {self.fullname=}, {self.email=}"


class Email(Base):
    __tablename__ = 'mail'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(ForeignKey('userclass.id'), nullable=True)
    email_address = Column(String, nullable=False)

    def __repr__(self):
        return f"{self.email_address}"


# Create tables from declarative classes.
Base.metadata.create_all(engine)

# Start the session
#session.begin(subtransactions=True)

# User data
mail1 = Email(email_address="box1@null.com")
mail2 = Email(email_address="box2@null.com")
mail3 = Email(email_address="box3@null.com")

a = User(name="Test", fullname="Testing Testovich")
a.email = [mail1, mail2, mail3]

session.add(a)
#session.commit()

mail4 = Email(email_address="box4@null.com")

b = User("Test2", fullname="Testing2 Testovich")
b.email = [mail4]

#session.begin(subtransactions=True)
session.add(b)
#session.commit()

# Search in the DB
ourUser = session.query(User).filter_by(name="Test2").first()
print(f"{ourUser=}")

#for instance in session.query(User).order_by(User.id):
#    print(f"{instance.name=}, {instance.fullname=}")

#for row in session.query(User, User.name).all():
#    print(f"{row.User}, {row.name}")

# Select from two tables. User and Email in the same time. Using relationships.
for id, name, fullname, email in session.query(User.id, User.name, User.fullname, User.email):
    print(f"{id=}, {name=}, {fullname=}, email={session.query(Email).filter_by(user_id=id)}")
