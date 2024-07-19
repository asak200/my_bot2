#!/usr/bin/env python3


import yaml

with open('/home/asak/dev_ws2/src/goal_sender/my_services/gui_data.yaml', 'r') as file:
    data = yaml.safe_load(file)

if 'ch' in data:
    print('yay')