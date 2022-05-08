#! /usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist  # geometry_msgs는 standard 아님(std)  
from rospy.core import signal_shutdown
import cv2 as cv

def func_callback(msg):
    pass

if __name__ == '__main__':
    rospy.init_node('simturtle_publisher')  
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10) 

# Twist type일 때 메세지를 보내는 코드 
    msg = Twist()
    msg.linear.x = 3.0  # 5m 전진
    msg.linear.y = msg.linear.z = 0.0
    msg.angular.x = msg.angular.y = msg.angular.z = 0

    # 힘 = 속도, 따라서 거리값만 주면 됨
    speed = 2 # 거리를 계속 증가시키다가(x값만), 특정 시점이 되면 멈추도록 코딩
    time = 1   
    msg.linear.x = speed
    current_distance = 0
    while not rospy.is_shutdown():
        time0 = rospy.Time.now().to_sec()
        while current_distance < speed :
            pub.publish(msg)
            time1 = rospy.Time.now().to_sec()
            current_distance = time * (time1-time0)
        msg.linear.x = -0.5
        while current_distance > -(speed):
            pub.publish(msg)
            time2 = rospy.Time.now().to_sec()
            current_distance = -(time) * (time2-time1)
        msg.angular.z = 3.14/2
        while current_distance < speed:
            pub.publish(msg)
            time3 = rospy.Time.now().to_sec()
            current_distance = time * (time3-time2)
      
        pass

    



    


