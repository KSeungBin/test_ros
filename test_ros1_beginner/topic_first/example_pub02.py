#! /usr/bin/env python3

import rospy
from std_msgs.msg import String  

# N 대 1 : 메세지(topic)는 동일, node(publisher2)의 이름은 unique해야 함
def func():
    pass

if __name__ == '__main__':
    rospy.init_node('sample_pub02') # node이름 바꿔주기
    pub = rospy.Publisher('hello', String, queue_size=10) # 메세지 내용을 pub과 sub파일 모두 통일해야 함
    
    rate = rospy.Rate(10)  
    while not rospy.is_shutdown():
        str = "hello_publisher : %s " % rospy.get_time()  
        pub.publish(str)  
        rate.sleep() 
    pass
