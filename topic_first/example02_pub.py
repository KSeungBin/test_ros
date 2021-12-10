#! /usr/bin/env python3

import rospy
from std_msgs.msg import String  

# example_pub.py가 아닌 이 파일에서 example_sub.py로 메세지를 보내려면?
def func():
    pass

if __name__ == '__main__':
    rospy.init_node('sample_pub')
    pub = rospy.Publisher('hello_world', String, queue_size=10) # 메세지 내용을 pub과 sub파일 모두 통일해야 함
    
    rate = rospy.Rate(10)  
    while not rospy.is_shutdown():
        str = "hello_world : %s " % rospy.get_time()  
        pub.publish(str)  
        rate.sleep() 
    pass
