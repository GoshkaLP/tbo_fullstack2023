from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base
from geoalchemy2 import Geometry


Base = declarative_base()


class Federals(Base):
    __tablename__ = 'Federals'
    __table_args__ = {'extend_existing': True}

    fed_id = Column(Integer, primary_key=True)
    federal_subject = Column(String)


class LocationsFederals(Base):
    __tablename__ = 'LocationsFederals'
    __table_args__ = {'extend_existing': True}

    obj_id = Column(Integer, primary_key=True)
    fed_id = Column(Integer)


class LocationsGeometry(Base):
    __tablename__ = 'LocationsGeometry'
    __table_args__ = {'extend_existing': True}

    obj_id = Column(Integer, primary_key=True)
    name = Column(String)
    federal_subject = Column(String)
    address = Column(String)
    geometry = Column(Geometry('POINT'))



