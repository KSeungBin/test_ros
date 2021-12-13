#! /usr/bin/env python3

import rospy
from std_msgs.msg import String

# 발행한 내용을 subscriber가 받는다
# ROS 메세지 내용은 단 2가지 : 나는 node를 할꺼야 & 그 노드에서 subscriber 역할 할꺼야 등록, 나는 어디에서 받을꺼야
def func_callback(msg):
    # log를 화면으로 보낼 것인지 file로 보낼 것인지? 아래 코드는 publisher가 보내는 내용을 화면으로 display
    rospy.loginfo('sub 01 %s', msg.data)  # 오는 메세지를 바꾸지 않고 그대로 print

    pub = rospy.Publisher('hello02', String, queue_size=10) # example_sub.py  ----> example_pub.py : 노드 이름은 이미 선언 되었으니 바꿀 필요X, 단 새로운 메세지를 보내는 것이므로 topic명 바꿔야 함
    pub.publish(msg.data)  # publisher는 한 번만 보내기 때문에 반복문 안에 넣으면 안 됨, str이 아닌 받은 메세지(msg.data)를 보내는 것
    return

if __name__ == '__main__':
    rospy.init_node('sample_sub')
    rospy.Subscriber('hello', String, callback=func_callback)  # publisher가 보낼 때만 메세지를 받기 때문에, 그 때 callback함수를 불러 동작시킴
    rospy.spin()   # Rate와 유사한 개념 but, 메세지를 받을 때 관리하는 time
    pass




