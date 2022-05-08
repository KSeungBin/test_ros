#! usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist


def fun_callback(msg):
    pass

# 시간을 쪼개는 방식은 직관적이지 않음. rate는 등가속도 운동
# 단, rate는 속도(speed)를 체크하기 힘들기 때문에 시간으로 프로그래밍하는 것이 맞음
# hz = 기기의 속도, spin = 센서의 속도

if __name__=='__main__':
    rospy.init_node('simturtle_publisher',anonymous=False)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    msg = Twist()
    distance = 2.0
    current_distance = 0.0
    speed = 1
    rate = rospy.Rate(1000)
    while current_distance < distance:
        msg.linear.x += 0.1
        pub.publish(msg)
        current_distance += 0.1
        print(current_distance)
        print(msg.linear.x)
        rate.sleep()
    pass




