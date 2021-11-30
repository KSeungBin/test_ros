from djitellopy import Tello, tello

# 클래스를 인스턴스화한 function을 사용하기 위해 변수로 담는다
tello = Tello()

tello.connect()

tello.takeoff()

tello.land()

pass

