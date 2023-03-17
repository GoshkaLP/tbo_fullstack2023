from sqlalchemy.orm import sessionmaker
from sqlalchemy import func, desc, literal_column

from contextlib import contextmanager

import os
from sqlalchemy import create_engine

from app.models import Federals, LocationsFederals, LocationsGeometry, LocationsInfo, LocationsSpending, \
    LocationsSupervisory, FundingSportTypes, ConstructionSportTypes

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
    """
    Функция для получения списка субъектов РФ из БД
    """
    with session_scope() as session:
        res = session.query(Federals).all()
        return res


def db_get_locations() -> list:
    """
    Функция для получения координат сопртивных объектов в виде широты и долготы
    """
    with session_scope() as session:
        res = session.query(LocationsGeometry.obj_id, LocationsGeometry.address,
                            LocationsGeometry.federal_subject, LocationsGeometry.fed_id, LocationsGeometry.geometry.ST_X(),
                            LocationsGeometry.geometry.ST_Y()).all()
        return res


def db_get_location(obj_id: int):
    """
    Функция для получения информации о конкретном объекте
    """
    with session_scope() as session:
        res = session.query(LocationsInfo, LocationsSpending, LocationsSupervisory). \
            join(LocationsSpending, LocationsInfo.obj_id == LocationsSpending.obj_id).\
            join(LocationsSupervisory, LocationsInfo.obj_id == LocationsSupervisory.obj_id).\
            filter(LocationsInfo.obj_id == obj_id).first()
        return res


def db_get_federals_locations() -> list:
    """
    Функция для получения GeoJson с информацией о полигонах субъектов РФ
    Делается прямой запрос, так как это эффективнее в данном случае, чем через ORM
    """
    with session_scope() as session:
        res = session.execute("""SELECT jsonb_build_object(
    'type',       'Feature',
    'id',         f.fed_id,
    'geometry',   ST_AsGeoJSON(f.geometry)::jsonb,
    'properties', to_jsonb( f.* ) - 'fed_id' - 'geometry'
    ) AS string FROM "FederalsGeometry" f """)
        return res.all()


def db_get_hexagon_locations() -> list:
    """
    Функция для получения GeoJson с информацией о гексагонов спортитвных объектов, которые строились
    Делается прямой запрос, так как это эффективнее в данном случае, чем через ORM
    """
    with session_scope() as session:
        res = session.execute("""SELECT jsonb_build_object(
    'type',       'Feature',
    'id',         l.obj_id,
    'geometry',   ST_AsGeoJSON(l.geometry)::jsonb,
    'properties', to_jsonb( l.* ) - 'obj_id' - 'geometry' - 'index_right'
    ) AS json
    FROM "LocationsHexagons" l;""")
        return res.all()


def db_get_funding_sport_types() -> list:
    """
    Функция для получения информации для графика распределения средств по типам спортивных комплексов
    """
    with session_scope() as session:
        res = session.query(FundingSportTypes.sports_complex_type, FundingSportTypes.funding_type,
                            func.sum(FundingSportTypes.count)).group_by(FundingSportTypes.sports_complex_type,
                                                                        FundingSportTypes.funding_type).all()
        return res


def db_get_construction_sport_types() -> list:
    """
    Функция для получения информации для графика распределения выделенного бюджета по годам
    """
    with session_scope() as session:
        res = session.query(ConstructionSportTypes).all()
        return res
