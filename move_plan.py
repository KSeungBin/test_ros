from djitellopy import Tello, tello

# 클래스를 인스턴스화한 function을 사용하기 위해 변수로 담는다
tello = Tello()

tello.connect()

tello.takeoff()

# move : API에서 move 검색
tello.move_up(50)     # 안전을 위해, 이륙 후 고도를 높여야 함
tello.move_forward(50)
tello.move_left(50)
tello.move_back(50)  # 전진하면, 후진도 그만큼 해줘야 land 가능
tello.move_right(50)
tello.rotate_clockwise(90)
tello.rotate_counter_clockwise(90)


tello.land()
pass

