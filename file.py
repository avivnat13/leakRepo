import yaml
import os

def exploitable_yaml_load(**kwargs):
    yaml.unsafe_load("!!python/object/new:os.system [echo EXPLOIT!]", **kwargs)
    print("hello world!")
    print("hello world!")
  
 
