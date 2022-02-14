import unittest
import config
import os

from flask_testing import TestCase

from app import create_app, db
from app.models import User

class TestBase(TestCase):

    def create_app(self):
        config_name = config.DevelopmentConfig
        app = create_app(config_name)
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
        return app

    def setUp(self):

        db.create_all()

        # create test admin user
        admin = User(email="admin@gmail.com", password="admin2016")


        # save users to database
        db.session.add(admin)
        db.session.commit()
    
    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()


if __name__ == "__main__":
    unittest.main()