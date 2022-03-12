#!/bin/python3

import ipaddress
import subprocess
import itertools

def ping_net():
    
    reachable = []
    unreachable = []
    
    ip_route = subprocess.run(
        'ip route show'.split(),
        stdout = subprocess.PIPE,
        encoding = 'utf-8'
        )

    ip_route = ip_route.stdout.split('\n')
   ''' 
    for line in ip_route:
        if 'br1' in line:                                              #фильтр по подсетке
            subnet = ipaddress.ip_network(line.split()[0])
      '''
    net = [] 
    i = 0 
    for line in ip_route: 
        try: 
            net = ipaddress.ip_network(ip_route[i].split()[0]) 
            nets.append(net) 
        except ValueError: 
            pass 
        except IndexError: 
            break 
        finally: 
            i += 1 
                
    pp_ip = []
    pp_processes = []
    for ip in subnet.hosts():
        pingpong = subprocess.Popen(
        ['ping', '-c', '5', str(ip)],
        stdout = subprocess.PIPE,
        stderr = subprocess.DEVNULL,
        encoding = 'utf-8'
        )
        pp_ip.append(ip)
        pp_processes.append(pingpong)
        
    for ip, process in zip(pp_ip, pp_processes):
        returncode = process.wait()
        if returncode == 0:
            reachable.append(str(ip))
        else:
            unreachable.append(str(ip))
    
            
    return reachable, unreachable
    


if __name__ == "__main__":
    reachable, unreachable = ping_net()
    print(f'Доступные адреса | Недоступные адреса\n{"="*40}')
    for r, u in itertools.zip_longest(reachable, unreachable, fillvalue=' '): 
        print(f'{r:17}{"|":2}{u}') 
            
    
        
        
