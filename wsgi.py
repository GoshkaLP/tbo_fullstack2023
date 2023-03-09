from app import create_app

from config import DevConfig, ProdConfig

app = create_app(DevConfig)

if app is None:
    print('[Error]: No config provided')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8082)
