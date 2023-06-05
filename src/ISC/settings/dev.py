from .base import *
from utils.utils import secret_value_returner

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY =  secret_value_returner("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True