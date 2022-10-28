'''
Store instances created in JSON format in the database
'''

import json
#from models.base_model import BaseModel


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
        self.__objects[key] = obj.to_dict()
        #type(self).__objects[key] = obj

    def save(self): 
        '''serializes __objects to the JSON file'''
        new_dict = self.__objects.copy()
        if new_dict is not None:
            json_fmt =json.dumps(new_dict)
            with open(FileStorage.__file_path, 'a', encoding='utf-8') as f:
                f.write(json_fmt)
         
    def reload(self):
        pass 
        '''deserializes the JSON file to __objects'''
        

    @staticmethod
    def to_json_string(dict_obj):
        '''returns json string rep of dict arg'''
        if dict_obj is not None:
            return json.dumps(dict_obj)
        else:
            return "[]"

    @classmethod
    def save_to_file():
        pass   