import cv2 as cv
import socket

# send할 때는 imshow하지 말고 디버깅 모드로 cap에 영상이 들어갔는지 확인
cap = cv.VideoCapture(0)
sender = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


    
# 480 * 640 * 3 / 20   => color는 입체이므로 3을 곱한 후, 20개의 packet으로 wrapping해서 보냄
perlength = int ((80 * 640 * 3 ) / 20) # a packet size
reallength = perlength + 1
while cap.isOpened():
    ret, frame = cap.read()
    frame = cv.resize(frame, (480,640))  # parameter로 넣을 때는 tuple사용하는 경우 많음 - 특히 opencv는 C와 연결되어 있기 때문
    num = frame.flatten()    #frame(입체)을 네트워크로 보내려면 1차원으로 바꿔줘야 함
    str = num.tostring()

    for i in range(20):
        # string을 배열로 바꿔 보냄
        sender.sendto(bytes([i]) + str[i*perlength:(i+1)*perlength], ('192.168.16.14',7778))
        pass
        







