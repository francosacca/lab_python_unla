from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///mi_base.db', echo=True)


# Declarar la base
Base = declarative_base()

# Crear una clase que representa una tabla
class Productos(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String)
    price = Column(Float, nullable=False)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
sesion = Session()


