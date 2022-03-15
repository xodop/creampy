#!/home/vagrant/venv/pyneng-py3-7/bin/python3

import re
from pprint import pprint

def description_rewriter(path_file):
    with open(fr'{path_file}') as f:
        descr = f.read()
    
    
    #cоздать списки интерфейсов и дескрипторов
    iface_and_descr = re.findall(r'(\S+) +(?:up|\*?down) +(?:up|down) +(.*)', descr)
    ifaces = [] 
    descrs = []
    for item in iface_and_descr: 
        ifaces.append(item[0])
        descrs.append(item[1])
    
    for item in descrs:
        i = descrs.index(item)
    #перестить #текст# при наличии в начало дескриптора
        if re.findall(r'#.*#', item): 
            if not item.startswith('#'): 
                item = item.split()
                item = ' '.join(sorted(item))
                descrs.pop(i) 
                descrs.insert(i, item)
    #заменить === на ---
        if re.search(r'={2,}', item):
            item = item.replace('=', '-')
            descrs.pop(i)
            descrs.insert(i, item)
    #удалить ---
        if re.search(r'-{2,}', item):
            item = item.replace('-', '')
            descrs.pop(i)
            descrs.insert(i, item)
    #удалить пробелы из начала строки
        if item.startswith(' '):
            item = item.lstrip()
            descrs.pop(i)
            descrs.insert(i, item)
    
     
    
    iface_and_descr_new = zip(ifaces, descrs)
    '''
    descrs = '\n'.join(descrs)
    with open(r'output.log', 'w') as f:
        descr = f.write(descrs)
    '''
    return(list(set(iface_and_descr_new).difference(set(iface_and_descr))))


def commands_generator(iface_and_descr_dict):
    
    template = '''
interface {}
 description {}
'''
    print('system-view')
    for items in iface_and_descr_dict:
        iface, descr = zip(items)
        iface = ''.join(iface)
        descr = ''.join(descr)
        print(template.format(iface, descr), end='')

if __name__ == "__main__":
    ifde = description_rewriter('MBH_25_00015_1-220223_1508.log')
    commands_generator(ifde)
    
