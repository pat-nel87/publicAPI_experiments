# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 17:18:37 2020

@author: Patrick
"""

import json
from urllib.request import urlopen

with urlopen('https://trefle.io/api/v1/plants?token=YOURAPIkey') as response:
    source = response.read()

data = json.loads(source)

#print(json.dumps(data, indent=2))

for data['common_name'] in data['data']:
    print(data['common_name'])
