from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///mi_base.db', echo=True)

db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
# Declarar la base
Base = declarative_base()
Base.query = db_session.query_property()


class Products(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String)
    price = Column(Float, nullable=False)

Base.metadata.create_all(engine)