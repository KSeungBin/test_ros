from djitellopy import Tello, tello

# 클래스를 인스턴스화한 function을 사용하기 위해 변수로 담는다
tello = Tello()
tello.connect()

# 패널 띄우기
import cv2
panel = cv2.imread('./telloedu.jpg') # imread = 이미지 불러오기
cv2.imshow('tello panel', panel)     # image show 

# # move : API에서 move 검색
# tello.move_up(50)
# tello.move_forward(50)
# tello.move_back(50)


# routine을 돌며 키가 드론에 계속 명령을 줄 수 있게 함
while True:
    key = cv2.waitKey()   # waitKey()는 ASCII코드를 다룸: 따라서 2진수를 10진수로 바꿔줌(113)
    if key == ord('q'):   # key에 마우스 hover 하면 113  # ord는 우리가 아는 문자로 바로 변환해줌
        break
    elif key == ord('t'):
        tello.takeoff()
    elif key == ord('l'):
        tello.land()
    elif key == ord('b'):
        tello.move('back', 20) # 최대한 작은 숫자를 주고, 계속 key 명령을 주며 조작하는 게 더 유리함
    elif key == ord('f'):    
        tello.move('forward', 20)
    elif key == ord('u'):
        tello.move('up', 20)
    elif key == ord('d'):
        tello.move('down', 20)
pass

