def check_addr():
    while True:
        ip = input('Введите адрес: ')
        ip = ip.split('.')
        if len(ip) != 4:
            print('Введите адрес в формате x.x.x.x')
        else:
            for i in range(4):
                if not ip[i].isdigit() or int(ip[i]) < 0 or int(ip[i]) > 255:  
                    print('Адрес должен содержать 4 числовых октета в диапозоне от 0 до 255')
                    break
                else:
                    return ip
            
def check_mask():
    mask_table = [
    '255.255.255.255', 
    '255.255.255.254', 
    '255.255.255.252', 
    '255.255.255.248', 
    '255.255.255.240', 
    '255.255.255.224',
    '255.255.255.192',
    '255.255.255.128',
    '255.255.255.0',
    '255.255.254.0',
    '255.255.252.0',
    '255.255.248.0',
    '255.255.240.0',
    '255.255.224.0',
    '255.255.192.0',
    '255.255.128.0',
    '255.255.0.0',
    '255.254.0.0',
    '255.252.0.0',
    '255.248.0.0',
    '255.240.0.0',
    '255.224.0.0',
    '255.192.0.0',
    '255.128.0.0',
    '255.0.0.0',
    '254.0.0.0',
    '252.0.0.0',
    '248.0.0.0',
    '240.0.0.0',
    '224.0.0.0',
    '192.0.0.0',
    '128.0.0.0',
    '0.0.0.0']
    
    while True:
        ip = input('Введите маску: ')
        
        if ip not in mask_table:
            print('Некорректный формат маски')
        else:
            ip = ip.split('.')
            return ip
            
def net_addr(ip, mask):
    '''count subnetwork address with known ip address and mask defined in octet list formate'''
    NET = []
    for i in range(4):
        net_i = int(ip[i]) & int(mask[i])
        NET.append(net_i)
    net_= [str(item) for item in NET]
    return '.'.join(net_)
    
def to_binary(ip):
    '''transform ip addres or mask in octet list formate to binary'''
    return'{:08b}.{:08b}.{:08b}.{:08b}'.format(int(ip[0]), int(ip[1]), int(ip[2]), int(ip[3]))

def main():
#ввод ip адреса с проверкой корректности
    addr = check_addr()
#ввод маски с проверкой корректности
    mask = check_mask()
#преобразование в список по разделителю
    #addr = addr.split('.')
    #mask = mask.split('.')
#расчет адреса подсети
    net = net_addr(addr, mask)
#расчет адреса и маски в двоичном виде
    bin_addr = to_binary(addr)
    bin_mask = to_binary(mask)
#расчет длины префикса    
    mask_len = bin_mask.count('1')
#расчет числа хостов
    host_count = 2 ** bin_mask.count('0') - 2
#шаблон
    template = '''
    Адрес в двоичном виде:                      {}
    Маска в двоичном виде:                      {}
    Длина префикса:                             {}
    Адрес подсети:                              {}
    Доступно хостов:                            {}
    '''

    return print(template.format(bin_addr, bin_mask, mask_len, net, host_count))

main()
