import os  

class Config():
    '''
    parent class configurations 
    '''
    pass

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