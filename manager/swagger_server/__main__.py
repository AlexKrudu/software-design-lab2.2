#!/usr/bin/env python3
import os

import connexion
import psycopg2

from swagger_server import encoder
from flask_cors import CORS, cross_origin
from swagger_server import connection


def main():
    connection.init()
    connection.conn = psycopg2.connect(
        host=os.environ['POSTGRES_HOST'],
        port=5432,
        database="gym_events",
        user=os.environ['POSTGRES_USER']
    )

    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Manager API'}, pythonic_params=True)
    cors = CORS(app.app)
    app.app.config['CORS_HEADERS'] = 'Content-Type'
    app.run(port=8080)


if __name__ == '__main__':
    main()
