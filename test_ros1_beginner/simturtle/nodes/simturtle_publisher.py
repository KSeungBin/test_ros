#! /usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist  # geometry_msgs는 standard 아님(std)  
from rospy.core import signal_shutdown

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
    distance = 2 # 거리를 계속 증가시키다가(x값만), 특정 시점이 되면 멈추도록 코딩
    distance2 = 1   
    msg.linear.x = distance
    current_distance = 0
    while not rospy.is_shutdown():
        time0 = rospy.Time.now().to_sec()
        while current_distance < distance :
            key = cv.waitKey(1)
            if key == ord("f"):
                pub.publish(msg)
                time1 = rospy.Time.now().to_sec()
                current_distance = distance2 * (time1-time0)
            msg.linear.x = 0   # current_distance가 2만큼 가면 turtlesim이 멈춘다
            pub.publish(msg)   # 그 때 한번 메세지를 발행해야 한다.
            pass

    # msg.linear.x = -5.0   # turtlesim이 전진하고, 쉬다가, 뒤로 온다.
    # pub.publish(msg)
    


# string type일 때 메세지를 보내는 코드
    # rate = rospy.Rate(20) 
    # while not rospy.is_shutdown():
    #     str = "hello publisher : %s " % rospy.get_time()  
    #     pub.publish(str)  
    #     rate.sleep()
    


