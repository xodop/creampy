#!/home/vagrant/venv/pyneng-py3-7/bin/python3

import re
from pprint import pprint


with open(r'MBH_25_00015_1-220223_1508.log') as in_f:
    descr = in_f.read()


#cоздаем списки интерфейсов и дескрипторов
iface_and_descr = re.findall(r'(\S+) +(?:up|\*?down) +(?:up|down) +(.*)', descr)
ifaces = [] 
descrs = []
for item in iface_and_descr: 
    ifaces.append(item[0])
    descrs.append(item[1])

#перемещаем #текст# при наличии в начало дескриптора
for item in descrs:
    if re.findall(r'#.*#', item): 
        i = descrs.index(item) 
        if not item.startswith('#'): 
            item = item.split()
            item = ' '.join(sorted(item))
            descrs.pop(i) 
            descrs.insert(i, item)

    
pprint(descrs)
