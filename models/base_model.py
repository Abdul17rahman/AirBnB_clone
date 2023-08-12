#!/usr/bin/python3

"""
    This is the Base Module
"""

from datetime import datetime
import uuid
import models


class BaseModel:
    """
        This class defines the common attribues/methods
        Attributes:
            id - string assigned with uuid
            created_at: datetime the instance is created
            updated_at: datetime an instance is updated

        Methods:
            save - updates the public instance
            to_dict - returns a dictionary of the instance
    """
    id = ""
    created_at = datetime
    updated_at = datetime

    def __init__(self, *args, **kwargs):
        """
            Initalization of the class attributes
        """

        # Creating an instance from a dictionary
        if kwargs is not None:
            if '__class__' in kwargs:
                del kwargs['__class__']
            if 'created_at' in kwargs:
                kwargs['created_at'] = datetime.fromisoformat(kwargs
                                                              ['created_at'])
            if 'updated_at' in kwargs:
                kwargs['updated_at'] = datetime.fromisoformat(kwargs
                                                              ['updated_at'])
            self.__dict__ = kwargs
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        models.storage.new(self)

    def save(self):
        """ Updates the updated_at instance with current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """
            str Prints [<class name>] (self.id) <self.__dict__>
        """
        cls_name = type(self).__name__
        return "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)

    def to_dict(self):
        """
            Returns a dictionary of all keys.
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = type(self).__name__
        if 'created_at' in new_dict:
            new_dict['created_at'] = new_dict['created_at'].isoformat()
        if 'updated_at' in new_dict:
            new_dict['updated_at'] = new_dict['updated_at'].isoformat()
        return new_dict
