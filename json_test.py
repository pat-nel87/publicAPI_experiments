# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 19:49:41 2021
Learning to work with JSON objects
@author: Patrick
"""

import json

data = {
        "president": {
            "name": "Zaphod Beeblebrox",
            "species": "Betelgeusian"
            }
        }

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)

json_string = json.dumps(data)
print(data["president"]['species'])
    