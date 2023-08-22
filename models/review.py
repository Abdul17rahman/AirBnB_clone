#!/usr/bin/python3

"""
    This is the Review Model
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """ Attribues and Methods in the User Model"""
    place_id = ""
    user_id = ""
    text = ""
