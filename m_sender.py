import socket
sender = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# 'nc 상대방IP port번호' 와 동일  
sender.sendto(str.encode('Hello Sender'), ('192.168.16.14', 7778)) # 내가 보낼 매세지, address -> 수신자가 bytepair[0], bytepair[1]로 받는다
            # 우리의 메세지를 2진수로 encoding해줘야 함(wrapping)

            #commit
            