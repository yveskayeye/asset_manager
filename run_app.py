from app import create_app
import config
import os

config_name = config.DevelopmentConfig
app = create_app(config_name)


if __name__ == "__main__":
    app.run()
