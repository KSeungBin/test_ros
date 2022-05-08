import socket

# 내가 원하는 인스턴스(생성자)만 가져오는 function
# UDP 통신을 할 것, tpye(socket으로 실어보낼 데이터 용량) # receiver라는 변수지정으로 인스턴스화 
receiver = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# 정보 binding
receiver.bind('192.168.16.14',7778) # 내 pc로 보내기

# 나는 이만큼의 사이즈로 데이터를 보낼꺼라는 정보를 노드에게 알려줘야 함(header)
# -> 1GB의 영상을 보낼 때에도, 특정 단위로 쪼개서 보내는 것 
while True:    # nc -l 7778 와 동일하려면 while True문 써야 함 - 영상을 계속 받을 준비하는 것 
    bytepair = receiver.recvfrom(1024) # 1kb  recvfrom으로 인스턴스화되면 하나의 패킷으로 날아옴
    message = bytepair[0]
    address = bytepair[1]  # bytepair의 첫번째 부분은 메세지, 두번째 부분은 sender 주소가 담겨 있음

    print(message, ',', address)