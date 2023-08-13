#!/usr/bin/python3

"""
    This is the City Model
"""

from models.base_model import BaseModel


class City(BaseModel):
    """ Attribues and Methods in the City Model"""
    state_id = ""
    name = ""

    def __init__(self):
        """ Initialize the State Model using the Base"""
        super().__init__()
