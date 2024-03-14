class Config:
    SECRET_KEY = b"secretkey"
    WTF_CSRF_ENABLED = True
class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    FLASK_SECRET = b"secretkey"