"""
This module sets the configurations for the application
"""
import os


class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv("SECRET_KEY")
    DATABASE_URL = os.getenv("DATABASE_URL")


class DevelopmentConfig(Config):
    """Development phase configurations"""
    DEBUG = True


class TestingConfig(Config):
    """Testing Configurations."""
    TESTING = True
    DEBUG = True
    DATABASE_URL = os.getenv("DATABASE_TEST_URL")
    PRESERVE_CONTEXT_ON_EXCEPTION = True


class ReleaseConfig(Config):
    """Release Configurations."""
    DEBUG = False
    TESTING = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'release': ReleaseConfig,
}
