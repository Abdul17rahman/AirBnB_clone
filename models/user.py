#!/usr/bin/python3

"""
    This is the User Model
"""

from models.base_model import BaseModel


class User(BaseModel):
    """ Attribues and Methods in the User Model"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
