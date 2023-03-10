from flask import Flask, render_template
from flask_restx import Api

from app.config import Config
from app.setup_db import db
from app.views.auth import auth_ns
from app.views.directors import director_ns
from app.views.genres import genre_ns
from app.views.movies import movie_ns
from app.views.users import user_ns

api = Api(doc='/docs')


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)

    @app.route('/')
    def index():
        return render_template('index.html')

    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    api.init_app(app)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)


#     create_data(app, db)
#
#
# def create_data(app, db):
#     with app.app_context():
#         db.create_all()


app = create_app(Config())

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=3000)