#!/usr/bin/python3
import os # Debug
from models import storage
from models.base_model import BaseModel

print("Current working directory:", os.getcwd()) # Debug
all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)
print("File saved to:", storage._FileStorage__file_path) # Debug
