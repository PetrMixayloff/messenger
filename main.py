from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# CREATE DATABASE messenger;
#
# CREATE USER messenger_user WITH PASSWORD '12345678';
#
# GRANT ALL PRIVILEGES ON DATABASE messenger TO messenger_user;
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

# 'sqlite:///db.sqlite'
engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')

metadata = Base.metadata

metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

admin_user = User(name="vasia", fullname="Vasiliy Pypkin", password="vasia2000")

session.add(admin_user)

session.commit()
