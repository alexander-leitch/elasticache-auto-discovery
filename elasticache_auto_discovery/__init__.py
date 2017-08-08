# -*- coding: utf-8 -*-

import socket


def discover(configuration_endpoint, time_to_timeout=None):
    host, port = configuration_endpoint.split(':')

    configs = []
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if time_to_timeout is not None:
        sock.settimeout(time_to_timeout)

    try:
        sock.connect((host, int(port)))
        sock.sendall(bytes('cluster nodes\r\n', 'utf-8'))

        data = bytes('', 'utf-8')
        while True:
            buf = sock.recv(1024);
            data += buf
            if data[-3:] == bytes('\n\r\n', 'utf-8'):
              break
            
        lines = data.split(bytes('\r\n', 'utf-8'))
        servers = lines[1].split(bytes('\n', 'utf-8'))
        
        configs = []
        for server in servers:        # Second Example
           details = server.split(b' ')
           if len(details) > 2:
             configs.append(details[1])
        
        # print('-----------------')
        # print(configs)
        # print('-----------------')
        
        # configs = [conf.split(b':') for conf in ips]
        
        sock.sendall(bytes('quit\r\n', 'utf-8'))

    finally:
        sock.close()

    return configs


if __name__ == '__main__':
    import sys
    mycache_servers = discover(sys.argv[1])
    # print(mycache_servers)
