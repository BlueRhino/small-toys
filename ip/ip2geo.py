# encoding='utf-8'
"""
use api from https://www.ipvigilante.com/
"""
import time

import requests


def ip2geo(ip_: str, format_='json'):
    url = f'https://ipvigilante.com/{format_}/{ip_}'
    headers = {
        'accept': f'application/{format_}',
        'content-type': f'application/{format_}',
    }
    response = requests.request('GET', url, headers=headers, timeout=5)
    return response.content


if __name__ == '__main__':
    # aa = ip2geo('82.131.200.119', 'csv')
    ips_file = open('ips', mode='r')
    ips = ips_file.readlines()
    count = 0
    with open(f'res_file+{int(time.time())}', mode='w', encoding='utf-8') as res_file:
        for ip in ips:
            ip = ip.split(':')[0]
            count += 1
            print(f'count = {count},ip = {ip}')
            res_file.write(ip2geo(ip, 'csv').decode('utf-8')+'\n')
            if count % 30 == 0:
                res_file.flush()
