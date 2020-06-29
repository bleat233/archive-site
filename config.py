import pymysql


class Config:
    SECRET_KEY = 'e3abbec48c43cdbff3cb6ce484d9772f'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://bleat2333@bleatblog:Lin010427@bleatblog.mysql.database.azure.com/blogdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp-mail.outlook.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'timshellin@outlook.com'
    MAIL_PASSWORD = 'wsalb198423'