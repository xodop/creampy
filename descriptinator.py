#!/home/vagrant/venv/pyneng-py3-7/bin/python3

import re
from pprint import pprint


with open(r'MBH_25_00015_1-220223_1508.log') as f:
    descr = f.read()


#cоздаем списки интерфейсов и дескрипторов
iface_and_descr = re.findall(r'(\S+) +(?:up|\*?down) +(?:up|down) +(.*)', descr)
ifaces = [] 
descrs = []
for item in iface_and_descr: 
    ifaces.append(item[0])
    descrs.append(item[1])


for item in descrs:
    i = descrs.index(item)
#перемещаем #текст# при наличии в начало дескриптора
    if re.findall(r'#.*#', item): 
        if not item.startswith('#'): 
            item = item.split()
            item = ' '.join(sorted(item))
            descrs.pop(i) 
            descrs.insert(i, item)
#заменяет === на ---
    elif re.search(r'={2,}', item):
        item = item.replace('=', '-')
        descrs.pop(i)
        descrs.insert(i, item)
#
    elif re.search(r'-{2,}', item):
        item = item.replace('-', '')
        descrs.pop(i)
        descrs.insert(i, item)
        

descrs = '\n'.join(descrs)
with open(r'output.log', 'w') as f:
    descr = f.write(descrs)
