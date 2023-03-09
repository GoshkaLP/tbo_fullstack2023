from os import getenv, name

# Для отладки
# from dotenv import load_dotenv
# load_dotenv()


class Config:
    SECRET_KEY = getenv('FLASK_SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{password}@{host}:5432/{db}'.format(
        user=getenv('POSTGRES_USER'),
        password=getenv('POSTGRES_PASSWORD'),
        host=getenv('HOST'),
        db=getenv('POSTGRES_DB')
    )
    print(SQLALCHEMY_DATABASE_URI)


class ProdConfig(Config):
    DEBUG = False
    TESTING = False


class DevConfig(Config):
    DEBUG = True
    TESTING = False