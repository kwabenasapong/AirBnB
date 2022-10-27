'''
Store instances created in JSON format in the database
'''

import json
from base_model import BaseModel


class FileStorage():
    '''
    FileStorage Class for that serializes instances 
    to a JSON file and deserializes JSON file to instances
    '''

    '''Private class attributes'''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''returns the dictionary __objects'''
        return self.__objects

    def new(self, obj): 
        '''sets in __objects the obj with key <obj class name>.id'''
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self): 
        '''serializes __objects to the JSON file'''
        with open(self.__file_path, "w", encoding="utf-8") as f:
            dict_store = {}
            for key, value in self.__objects.items():
                dict_store[key] = value.to_dict()
                json.dump(dict_store, f)
            
    def reload(self): 
        '''deserializes the JSON file to __objects'''
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                for obj in json.load(f).values():
                    self.new(eval(obj["__class__"](**obj)))
        except FileNotFoundError:
            return