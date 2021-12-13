#! /usr/bin/env python3


# 1 대 N : 메세지(topic)는 동일, node이름은 unique해야 함
import rospy
from std_msgs.msg import String


def func_callback(msg):
    rospy.loginfo('sub 02 %s', msg.data)  
    return

if __name__ == '__main__':
    rospy.init_node('sample_sub02')  # node 이름은 바꿔야 함
    rospy.Subscriber('hello', String, callback=func_callback)  # 메세지는 동일
    rospy.spin()  
    pass
