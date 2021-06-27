from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()

engine = create_engine("postgresql://diwxevtepyvlsy:458dc293d5d00b3d373133108a9230535744c75b429faed1e95935156f77fd51@ec2-54-158-232-223.compute-1.amazonaws.com:5432/di6j387sfrtsp", convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    def init_db():
        # import all modules here that might define models so that
        # they will be registered properly on the metadata.  Otherwise
        # you will have to import them first before calling init_db()
        import main.Model
        db.init_app(app)
        Base.metadata.create_all(bind=engine)
        db.create_all()

    with app.app_context():
        init_db()
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from main.users.route import users
    from main.posts.route import posts
    from main.main.route import main
    from main.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app





