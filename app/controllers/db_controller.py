# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
#
#
# class Database:
#     def __init__(self, user: str, password: str, host: str, port: int, database: str):
#         self.user = user
#         self.password = password
#         self.host = host
#         self.port = port
#         self.database = database
#
#         self.engine = None
#         self.session = None
#
#     def connect(self):
#         url = f'postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}'
#         self.engine = create_engine(url)
#         session = sessionmaker(bind=self.engine)
#         self.session = session()
#
#     def disconnect(self):
#         if self.session is not None:
#             self.session.close()
#         self.session = None
#         self.engine = None
#
#     def execute(self, query: str) -> list:
#         result = self.session.execute(query)
#         return result.fetchall()

from sqlalchemy.orm import sessionmaker, load_only

from contextlib import contextmanager

import os
from sqlalchemy import create_engine

from app.models import Federals, LocationsFederals, LocationsGeometry

# Для отладки
from dotenv import load_dotenv

load_dotenv()

# Конфиг с информацией об IP адресе сервера, на котором работает проект с созданием подключения к PSQL базе данных
POSTGRES_HOST = os.getenv('HOSTNAME')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_DB = os.getenv('POSTGRES_DB')

SQL_ENGINE = create_engine("postgresql://{user}:{password}@{host}:{port}/{db}".format(
    user=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
    host=POSTGRES_HOST,
    db=POSTGRES_DB,
    port=5432
),
    pool_recycle=3600)

Session = sessionmaker(SQL_ENGINE, expire_on_commit=False)


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def db_get_federals() -> list:
    with session_scope() as session:
        res = session.query(Federals.fed_id, Federals.federal_subject).all()
        return res


def db_get_locations(fed_ids: list | None = None) -> list:
    with session_scope() as session:
        if fed_ids:
            res = session.query(LocationsGeometry.obj_id, LocationsGeometry.name, LocationsGeometry.address,
                                LocationsGeometry.federal_subject, LocationsGeometry.geometry.ST_X(),
                                LocationsGeometry.geometry.ST_Y()).join(LocationsFederals, LocationsGeometry.obj_id
                                                                        == LocationsFederals.obj_id).\
                filter(LocationsFederals.fed_id.in_(fed_ids)).all()
        else:
            res = session.query(LocationsGeometry.obj_id, LocationsGeometry.name, LocationsGeometry.address,
                                LocationsGeometry.federal_subject, LocationsGeometry.geometry.ST_X(),
                                LocationsGeometry.geometry.ST_Y()).all()
        return res
