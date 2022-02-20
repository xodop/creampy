#ввод в формате a.b.c.d
addr = input('Введите адрес: ')
mask = input('Введите маску: ')

#преобразование в список по разделителю
addr = addr.split('.')
mask = mask.split('.')

#расчет адреса сети
NET = []
for i in range(4):
    net_i = int(addr[i]) & int(mask[i])
    NET.append(net_i)

net_= [str(item) for item in NET]
net = '.'.join(net_)

#расчет адреса и маски в двоичном виде
bin_addr = '{:08b}.{:08b}.{:08b}.{:08b}'.format(int(addr[0]), int(addr[1]), int(addr[2]), int(addr[3]))
bin_mask = '{:08b}.{:08b}.{:08b}.{:08b}'.format(int(mask[0]), int(mask[1]), int(mask[2]), int(mask[3]))

#расчет длины префикса
mask_len = bin_mask.count('1')

#расчет числа хостов
host_count = 2 ** bin_mask.count('0') - 2

#расчет броадкастового адреса в двоичном виде
bin_host_count = '{:08b}'.format(host_count + 1)
bin_net_= []
for i in range(4):
    bin_net_oct = '{:08b}'.format(NET[i])
    bin_net_.append(bin_net_oct)
    
bin_net = '.'.join(bin_net_)
bin_net_= ''.join(bin_net_)
bin_broadcast = int(bin_net_) + int(bin_host_count)
bin_broadcast = list(str(bin_broadcast))
while len(bin_broadcast) < 32:
    bin_broadcast.insert(0,'0')

i = 0
bb_oct_list = []
while i < 32:
    bb_oct = ''.join(bin_broadcast[i:i+8])
    bb_oct_list.append(bb_oct)
    i += 8
    
bin_broadcast = '.'.join(bb_oct_list)

#перевод широковещательного адреса в десятичный вид
broadcast_ = [str(int(item, 2)) for item in bb_oct_list]
broadcast = '.'.join(broadcast_)

#расчет минимального и максимального адреса
min_host = net_                             #если что-то сломалось, вернуть .copy()                    
min_host[3] = str(int(min_host[3]) + 1)
min_host = '.'.join(min_host)
max_host = broadcast_                       #если что-то сломалось, вернуть .copy()
max_host[3] = str(int(max_host[3]) - 1)
max_host = '.'.join(max_host)

#шаблон
template = '''
Адрес в двоичном виде:                      {}
Адрес подсети в двоичном виде:              {}
Широковещательный адрес в двоичном виде:    {}
Маска в двоичном виде:                      {}

Длина префикса:                             {}
Адрес подсети:                              {}
Широковещательный адрес:                    {}
Минимально возможный адрес хоста:           {}
Максимально возможный адрес хоста:          {}
Доступно хостов:                            {}
'''

print(template.format(bin_addr, bin_net, bin_broadcast, bin_mask, mask_len, net, broadcast, min_host, max_host, host_count))
