from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from config import Config
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()

engine = create_engine('mysql+pymysql://bleat2333@bleatblog:Lin010427@bleatblog.mysql.database.azure.com/blogdb', convert_unicode=True)
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





