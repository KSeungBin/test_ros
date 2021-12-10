#! /usr/bin/env python3

import rospy
from std_msgs.msg import String

# 발행한 내용을 subscriber가 받는다
# ROS 메세지 내용은 단 2가지 : 나는 node를 할꺼야 & 그 노드에서 subscriber 역할 할꺼야 등록, 나는 어디에서 받을꺼야
def func_callback(msg):
    # log를 화면으로 보낼 것인지 file로 보낼 것인지? 아래 코드는 publisher가 보내는 내용을 화면으로 display
    rospy.loginfo('%s', msg.data)  # 오는 메세지를 바꾸지 않고 그대로 print
    return

if __name__ == '__main__':
    rospy.init_node('sample_sub')
    rospy.Subscriber('hello_publisher', String, callback=func_callback)  # publisher가 보낼 때마다 불려지는데, 그 때 callback함수를 불러 동작시킴
    rospy.Subscriber('hello_world', String, callback=func_callback)
    rospy.spin()   # Rate와 유사한 개념 but, 메세지를 받을 때 관리하는 time
    pass
