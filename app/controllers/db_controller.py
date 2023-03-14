from sqlalchemy.orm import sessionmaker, load_only

from shapely import wkb

from contextlib import contextmanager

import os
from sqlalchemy import create_engine

from app.models import Federals, LocationsFederals, LocationsGeometry, LocationsInfo, LocationsSpending, \
    LocationsSupervisory, FederalsGeometry

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
        res = session.query(Federals).all()
        return res


def db_get_locations() -> list:
    with session_scope() as session:
        res = session.query(LocationsGeometry.obj_id, LocationsGeometry.name, LocationsGeometry.address,
                            LocationsGeometry.federal_subject, LocationsGeometry.fed_id, LocationsGeometry.geometry.ST_X(),
                            LocationsGeometry.geometry.ST_Y()).all()
        return res


def db_get_locations_info(obj_id: int) -> LocationsInfo:
    with session_scope() as session:
        res = session.query(LocationsInfo).filter(LocationsInfo.obj_id == obj_id).first()
        return res


def db_get_locations_spending(obj_id: int) -> LocationsSpending:
    with session_scope() as session:
        res = session.query(LocationsSpending).filter(LocationsSpending.obj_id == obj_id).first()
        return res


def db_get_locations_supervisory(obj_id: int) -> LocationsSupervisory:
    with session_scope() as session:
        res = session.query(LocationsSupervisory).filter(LocationsSupervisory.obj_id == obj_id).first()
        return res


def db_get_federals_locations() -> list:
    with session_scope() as session:
        res = session.execute("""SELECT jsonb_build_object(
    'type',       'Feature',
    'id',         f.fed_id,
    'geometry',   ST_AsGeoJSON(f.geometry)::jsonb,
    'properties', to_jsonb( f.* ) - 'fed_id' - 'geometry'
    ) AS string FROM "FederalsGeometry" f """)
        return res.all()
