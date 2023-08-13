#!/usr/bin/python3

"""
    This is the Amenity Model
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Attribues and Methods in the Amenity Model"""
    name = ""

    def __init__(self):
        """ Initialize the Amenity Model using the Base"""
        super().__init__()
