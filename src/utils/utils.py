import os 
from django.core.exceptions import ImproperlyConfigured


def secret_value_returner(data_name:str)->str:
    """
        Will return the enironment variable for sensetive data in \
        development phase
    """
    try:
        data=os.environ[data_name]
        return data
    except KeyError:
        raise(ImproperlyConfigured(f"Please insert {data_name} "+\
                                   "variable in the environment."))

