import itertools
from multiprocessing import Pool
import socket
from netaddr import IPRange


def port_scan(connect_data):
    hostname, port_num = str(connect_data[0]), connect_data[1]
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        s.connect((hostname, port_num))
        print(hostname, 'Port:', port_num, "is open")
    except socket.error:
        pass
    finally:
        s.close()


ipStart, ipEnd = input("Enter IP-IP: ").split("-")
iprange = IPRange(ipStart, ipEnd)

ports = (43, 80, 109, 110, 115, 118, 119, 143, 194,
         220, 443, 540, 585, 591, 1112, 1433, 1443,
         3128, 3197, 3306, 3899, 4224, 4444, 5000, 5432,
         6379, 8000, 8080, 10000)

if __name__ == "__main__":
    with Pool(4) as p:
        p.map(port_scan, itertools.product(iprange, ports))
