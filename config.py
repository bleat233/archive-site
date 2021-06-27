import os

class Config:
    SECRET_KEY = 'e3abbec48c43cdbff3cb6ce484d9772f'
    SQLALCHEMY_DATABASE_URI = "postgresql://diwxevtepyvlsy:458dc293d5d00b3d373133108a9230535744c75b429faed1e95935156f77fd51@ec2-54-158-232-223.compute-1.amazonaws.com:5432/di6j387sfrtsp"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp-mail.outlook.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'timshellin@outlook.com'
    MAIL_PASSWORD = 'wsalb198423'