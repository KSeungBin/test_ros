#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
#PI = 3.1415926535897
toRAD = 0.0174533

def rotate():
    # Starts a new node
    rospy.init_node('tb3_cleaner', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    msg = Twist()

    # Receiveing the user's input
    print("input speed within 0.0 ~ 160")
    speed     = input("Input your speed (degrees/sec):")
    print("input speed within 0 ~ 360")
    angle     = input("Type your distance (degrees):")
    print("direction cw:1, ccw:0")
    clockwise = input("Clockwise?: ")
    
    angular_speed  = speed * toRAD
    relative_angle = angle * toRAD

    msg.linear.x  = msg.linear.y  = msg.linear.z  = 0
    msg.angular.x = msg.angular.y = 0
    
    if clockwise:
        msg.angular.z = -abs(angular_speed)
    else:
        msg.angular.z =  abs(angular_speed)
        
    duration = relative_angle / angular_speed   # 시간 = 거리(각도를 radian으로 변환) / 속력
    time2end = rospy.Time.now() + rospy.Duration(duration)  # rate 사용하면 시간이 어긋남
    
    pub.publish(msg)
    # rospy.sleep(0.001)
        
    while(rospy.Time.now() < time2end): # duration 시간만큼 반복문이 돈다
        pass    
        
    msg.angular.z = 0
    pub.publish(msg)
    

if __name__ == '__main__':
    try:
        rotate()
        rospy.spin()
        
    except rospy.ROSInterruptException:
        pass