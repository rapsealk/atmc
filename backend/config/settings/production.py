from .base import *
from .base import env

# https://docs.djangoproject.com/en/4.2/ref/settings/#debug
DEBUG = False

# https://docs.djangoproject.com/en/4.2/ref/settings/#secret-key
SECRET_KEY = env("SECRET_KEY")
