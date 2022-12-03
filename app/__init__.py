import logging
from flask import Flask
from app import ext, models


logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


def create_app(conf: str):

    logging.info("initializing app...")

    # create app
    app = Flask(__name__, static_folder='static_files')

    # load config
    logging.info(f"config={conf}")
    app.config.from_object(conf)

    # init extensions
    ext.db.init_app(app)
    ext.ma.init_app(app)

    with app.app_context():

        # create DB tables if not exist
        ext.db.create_all()

        logging.info("app initialized.")

        return app
