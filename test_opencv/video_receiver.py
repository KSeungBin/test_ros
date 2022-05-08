import socket
import cv2 as cv
 
receiver = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
receiver.bind(('192.168.16.14',7778)) # 내 pc로 보내기


perlength = int ((80 * 640 * 3 ) / 20) # a packet size
reallength = perlength + 1

array = list()
import numpy as np
while True:     
    message, address = receiver.recvfrom(reallength)  # bytepair로 0~19까지 넘버링 된 영상 조각이 날아옴
    # message = bytepair[0]
    # address = bytepair[1]  

# str이 들어왔다는 것(packet은 string) = array로 들어왔다는 것
    str = message[1:46081]   # message[1:]
    
    # 네트워크는 최적의 경로를 찾기 때문에, 넘버링한 순서대로 packet을 보내지 않는다. 1/49232, 4/988927, 2/2343, ...., 19/23541
    # 따라서, 날아온 packet을 순서대로 쌓아줄 array 필요
    # message의 0번에 보낼 패킷의 순서 정보가 담겨있음 -> 배열도 0번에 순서를 넣어줘
    array[message[0]] = str  
    num_array = b''    # 2진수를 받을 때 깨지지 않도록 선언

    if message[0] == 19:
    # 날아올 때는 순번때문에 array(list)에 담았지만, 입체로 바꾸기 위해서는 다시 flat한 str로 바꾼 후, reshape으로 입체로 바꿔줘야 함
        for i in range(20):
            num_array += array[i]
        frame = np.fromstring(num_array, dtype=np.uint8)
        frame = frame.reshape(480, 640, 3)   # depth = 3
        cv.imshow('video receiver', frame)
    pass
    # print(message, ',', address)

    

    