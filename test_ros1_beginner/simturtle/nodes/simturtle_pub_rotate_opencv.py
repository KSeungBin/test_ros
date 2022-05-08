#! /usr/bin/env python3

# turtlesim 제자리에서 회전하는 코드
from re import T
import rospy
from geometry_msgs.msg import Twist   
from rospy.core import signal_shutdown
import cv2 as cv

def func_callback(msg):
    pass

if __name__ == '__main__':
    rospy.init_node('simturtle_pub_rotate')  
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10) 

# Twist type일 때 메세지를 보내는 코드 
    msg = Twist()

    speed = 2  # 회전속도
    angle = 180  # degree

    cv.namedWindow('keyboard control')
    number = 1
    # angle은 radian으로 구한다 = 물체가 자신의 중심점을 기준으로 얼만큼 회전할지 radian으로 구함
    angular_speed = (speed* 2 * 3.14) / 360     # 호를 얼만큼 빨리 돌 것인가
    relative_angle = (angle * 2 * 3.14) / 360  # 얼만큼 각도로 돌 것인가  # 2π = 원의 둘레   # 회전하는 speed가 결국 relative angle이 된다.(radian)
    
    
    current_angle = 0    # 0이 아닌 최소한의 값을 주기
    msg.angular.z = angular_speed
    time0 = rospy.Time.now().to_sec()
    while current_angle < relative_angle:
        key = cv.waitKey(1)
        if key == ord('r'):
            number = str.encode('f')
            pub.publish(msg)
            time1 = rospy.Time.now().to_sec()
            current_angle = angular_speed * (time1 - time0)  # speed 대신 current값 넣는다. current 계속 증가하다가 특정 relative 값이 되면 밖으로 빠져 나옴  
    msg.angular.z = 0.0 # while문을 빠져나오면 z값을 0으로 만들어야 멈춘다
    pub.publish(msg)
    pass