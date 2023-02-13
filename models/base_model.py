#!/usr/bin/python3
"""This script is the base model class"""

import uuid
from datetime import datetime


class BaseModel():

    """Parent Class from which all other classes will inherit"""

    id_list = []

    def __init__(self):
        while (true):
            u_id = uuid.uuid4()
            if (u_id not in id_list):
                id_list.append(u_id)
                self.id = u_id
                break
        self.created_at = d.date.today
        self.updated_at.append(d.date.today) 

           def save(self):
        """this will save the baseModel object"""

        self.updated_at = datetime.now()

  def to_json(self):
        """ Converts the objects to json object """ 

