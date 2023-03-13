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


class LocationsInfo(Base):
    __tablename__ = 'LocationsInfo'
    __table_args__ = {'extend_existing': True}

    obj_id = Column(Integer, primary_key=True)
    active = Column(Boolean)
    description = Column(String)
    description_long = Column(String)
    description_en = Column(String)
    description_long_en = Column(String)
    municipal_entity = Column(String)
    federal_subject = Column(String)
    significance = Column(String)
    locality = Column(String)
    locality_en = Column(String)
    address = Column(String)
    address_en = Column(String)
    sports_complex_type = Column(String)
    sports_types = Column(String)
    website_url = Column(String)
    work_hours_weekdays = Column(String)
    saturday_working_hours = Column(String)
    sunday_working_hours = Column(String)


class LocationsSpending(Base):
    __tablename__ = 'LocationsSpending'
    __table_args__ = {'extend_existing': True}

    obj_id = Column(Integer, primary_key=True)
    object_actions = Column(String)
    construction_start_date = Column(String)
    construction_end_date = Column(String)
    total_funding = Column(Integer)
    federal_budget_funding = Column(Integer)
    federal_budget_funding_spent = Column(Integer)
    regional_budget_funding = Column(Integer)
    regional_budget_funding_spent = Column(Integer)
    local_budget_funding = Column(Integer)
    local_budget_funding_spent = Column(Integer)
    off_budget_funding = Column(Integer)
    off_budget_funding_spent = Column(Integer)


class LocationsSupervisory(Base):
    __tablename__ = 'LocationsSupervisory'
    __table_args__ = {'extend_existing': True}

    obj_id = Column(Integer, primary_key=True)
    supervisory_authority = Column(String)
    supervisory_authority_phone = Column(String)
    contact_phone = Column(String)
    email = Column(String)
    registered_in_registry = Column(Boolean)


class FederalsGeometry(Base):
    __tablename__ = 'FederalsGeometry'
    __table_args__ = {'extend_existing': True}

    fed_id = Column(Integer, primary_key=True)
    federal_subject = Column(String)
    obj_count = Column(Integer)
    geometry = Column(Geometry)
