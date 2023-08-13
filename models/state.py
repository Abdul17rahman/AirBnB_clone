#!/usr/bin/python3

"""
    This is the State Model
"""

from models.base_model import BaseModel


class State(BaseModel):
    """ Attribues and Methods in the State Model"""
    name = ""

    def __init__(self):
        """ Initialize the User Model using the Base"""
        super().__init__()
