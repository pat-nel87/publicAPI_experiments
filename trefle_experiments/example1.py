# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 17:08:26 2020

@author: Patrick
"""

import requests

r = requests.get('https://trefle.io/api/v1/plants?token=YourApikey')
r.json
dictobj = r.json

