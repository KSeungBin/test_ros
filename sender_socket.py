import socket
import ipaddress
import sys

def MessageSending():
    sender = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    
    try:
        ip = ipaddress.ip_address(sys.argv[1])
        print('%s is a correct IP%s address.' % (ip, ip.version))
        sender.sendto(str.encode('Hello Sender'), (ip, 7778))
    except ValueError:
        print('address/netmask is invalid: %s' % sys.argv[1])
    except:
        print('Usage : %s  ip' % sys.argv[0])


def EchoServer():
    with socket.socket() as s:
        host = 'localhost'
        port = 7778

        s.bind((host,port))
        print(f'socket binded to {port}')

        s.listen()

        con, addr = s.accept()

        with con:
            while True:
                data = con.recv(1024)
                if not data:
                    break
                con.sendall(data)


  

if __name__ == '__main__':
    MessageSending
    EchoServer
    
