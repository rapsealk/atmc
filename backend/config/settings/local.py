from .base import *
from .base import env

# https://docs.djangoproject.com/en/4.2/ref/settings/#debug
DEBUG = True

# https://docs.djangoproject.com/en/4.2/ref/settings/#secret-key
SECRET_KEY = env(
    "SECRET_KEY",
    default="2srb1ik5y66tvq5kvk4q908hgywrf25fg4whbsfsuui8tkconvqw7ajk4b3swdub",
)
