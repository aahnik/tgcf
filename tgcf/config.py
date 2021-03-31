# a custom config parser
import yaml
from typing import List
from pydantic import BaseModel



class Forward(BaseModel):
    source: int
    dest: List[int]
    offset: int

class Config(BaseModel):
    forwards: List[Forward]

def read_config(config_file:str):
    with open(config_file) as file:
        config_dict = yaml.full_load(file)
        try:
            config = Config(**config_dict)
        except Exception as err:
            print(err)
            quit(1)
        else:
            return config

def update_config(config_file:str,config:Config):
    with open(config_file,'w') as file:
        yaml.dump(config.dict(),file)

