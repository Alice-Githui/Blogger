import os  

class Config():
    '''
    parent class configurations 
    '''
    QUOTES_API='http://quotes.stormconsultancy.co.uk/{}.json'
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://githui:Kqcaptain#2@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY=os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST='app/static/photos'

    #email configurations
    MAIL_SERVER='smtp.googlemail.com'
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USERNAME=os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD=os.environ.get("MAIL_PASSWORD")

    #simple mde configurations
    SIMPLE_JS_IIFE=True
    SIMPLEMDE_USE_CDN=True

class ProdConfig(Config):
    '''
    Child configurations used in production

    Args:
    Config: The parent configuration with general configuration settings
    '''

    SQLALCHEMY_DATABASE_URI = "postgresql://raajgragqpplsx:bac12cb9a45c2502b0722f327052e0288e7f3c8f71cfb541390c2ff2bcb7cb38@ec2-54-224-120-186.compute-1.amazonaws.com:5432/d5crblq3j860e0?sslmode=require"

class DevConfig(Config):
    '''
    child configurations used in development

    Args:
    Config: The parent configurations with general configuration settings
    '''

    DEBUG=True

config_options={
    'production':ProdConfig,
    'development':DevConfig
}