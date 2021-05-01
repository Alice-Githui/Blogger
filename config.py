import os  

class Config():
    '''
    parent class configurations 
    '''
    QUOTES_API='http://quotes.stormconsultancy.co.uk/{}.json'
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://githui:Kqcaptain#2@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS=False

class ProdConfig(Config):
    '''
    Child configurations used in production

    Args:
    Config: The parent configuration with general configuration settings
    '''

    pass

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