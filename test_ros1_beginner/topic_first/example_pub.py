#! /usr/bin/env python3

import rospy
from std_msgs.msg import String  # ROS 관련 standard messages 중 String 방식 사용

# publisher에서 발행
# ROS 메세지 내용은 단 2가지 : 나는 node를 할꺼야 & 그 노드에서 publisher 역할 할꺼야 등록, 나는 발행으로 보낼꺼야
def func():
    pass
def func_callback(msg):
    # log를 화면으로 보낼 것인지 file로 보낼 것인지? 아래 코드는 publisher가 보내는 내용을 화면으로 display
    rospy.loginfo('sub 01 %s', msg.data)  # 오는 메세지를 바꾸지 않고 그대로 print
    return

if __name__ == '__main__':
    rospy.init_node('sample_pub')  # 나는 node가 될꺼야 : node 이름은 unique해야 한다
    pub = rospy.Publisher('hello', String, queue_size=10) # 나는 publisher 될꺼고, string 메세지 보낼꺼야 # string = publisher는 메세지를 보내는 역할. ROS 메세지 규칙을 따라야 함
    
    rospy.Subscriber('hello02', String, callback=func_callback) # example_sub.py  ----> example_pub.py

    rate = rospy.Rate(10)   # 메세지를 보내는 주기 설정: 10hz : 1초 쉬고, 메세지 던지기를 반복
    while not rospy.is_shutdown():
        str = "hello publisher : %s " % rospy.get_time()  
        pub.publish(str)  # 메세지를 보내는 명령 : () 안에는 string만 들어가야 함 
        # 만약 메세지 규칙을 위치값으로 설정하면, () 안에 위치값만 들어가야 함
        rate.sleep()   # 설정한 시간 동안 rate가 갔다가 멈췄다를 반복
    pass







