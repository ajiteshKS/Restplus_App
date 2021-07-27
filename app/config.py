import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:ajitesh1234@localhost/test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

    # MySql Database settings
    MYSQL_DATABASE_HOST = "host.com"
    MYSQL_DATABASE_PORT = 3306
    MYSQL_DATABASE_USER = "Ajitesh"
    MYSQL_DATABASE_PASSWORD = "abc"
    MYSQL_DATABASE_DB = "test"
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024 * 1024

    # Flask-Restplus settings
    RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
    RESTPLUS_VALIDATE = True
    RESTPLUS_MASK_SWAGGER = False
    RESTPLUS_ERROR_404_HELP = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:ajitesh1234@localhost/test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False

    # MySql Database settings
    MYSQL_DATABASE_HOST = "host.com"
    MYSQL_DATABASE_PORT = 3306
    MYSQL_DATABASE_USER = "Ajitesh"
    MYSQL_DATABASE_PASSWORD = "abc"
    MYSQL_DATABASE_DB = "test"
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024 * 1024

    # Flask-Restplus settings
    RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
    RESTPLUS_VALIDATE = True
    RESTPLUS_MASK_SWAGGER = False
    RESTPLUS_ERROR_404_HELP = False


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:ajitesh1234@localhost/test'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
