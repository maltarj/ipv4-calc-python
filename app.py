from ipv4CalcProject.calcipv4 import CalcIpv4

calc_ipv4 = CalcIpv4(ip='192.168.0.1', mask='255.255.255.192')

print(f'IP: {calc_ipv4.ip}')
print(f'MASK: {calc_ipv4.mask}')
print(f'NETWORK: {calc_ipv4.network}')
print(f'BROADCAST: {calc_ipv4.broadcast}')
print(f'PREFIX: {calc_ipv4.prefix}')
print(f'NUMBER OF NETWORK IPS: {calc_ipv4.number_ips}')