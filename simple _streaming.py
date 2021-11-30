from djitellopy import Tello, tello

# 클래스를 인스턴스화한 function을 사용하기 위해 변수로 담는다
tello = Tello()
tello.connect()

tello.streamon()    # 버전이 바뀌면서 stream_on은 동작 안 됨
frame_read = tello.get_frame_read() # 드론이 촬영한 영상을 desktop으로 가져오기

import cv2
while True:
    cv2.imshow('tello stream', frame_read.frame) # 드론이 촬영한 영상을 네트워크로 한 장씩 가져오는데 이를 한 장으로 만들어주는 기능 -> opencv로 영상을 그대로 띄우면 됨
    key = cv2.waitKey(1) 
    if key == ord('q'):
        break
tello.streamoff()

pass
1
