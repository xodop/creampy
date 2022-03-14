#!/home/vagrant/venv/pyneng-py3-7/bin/python3

import re
from pprint import pprint


with open(r'MBH_25_00015_1-220223_1508.log') as in_f:
    descr = in_f.read()

#get all descriptors that contain ##
descr_list = re.findall(r'(?:up|\*?down) +(?:up|down) +([\S ]*#.+#[\S ]*)', descr)


#make ## the first in descriptor
for item in descr_list: 
    i = descr_list.index(item) 
    if not item.startswith('#'): 
        item = item.split()
        item = ' '.join(sorted(item))
        descr_list.pop(i) 
        descr_list.insert(i, item) 

    
pprint(descr_list)
