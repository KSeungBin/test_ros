import rospy
import math
from geographic_msgs.msg import Twist

def main():
    rospy.init_node('rotate')
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    relative_angle = math.radians(90)  # 0도에서 출발하여 목표지점은 90도 꺾는것(목표 각도)
    angular_speed = 1.0                # 미는 힘
    duration = relative_angle / angular_speed  # 어느 기간 동안 미는가 : 1씩 90번 밀면 90도 꺾인다
    time2end = rospy.Time.now() + rospy.Duration(duration)  # 현재 시간에서 정해진 duration 까지만 밀면(publish하면) 90도가 됨
    
    
    msg = Twist()
    msg.angular.z = angular_speed
    while rospy.Time.now() < time2end:
        pub.publish(msg)
        rospy.sleep(0.01)  # 밀리는 동안 시간의 영향을 받지 않으면서 while문은 돌도록 적은 값을 주기
                           # 기기에 메세지를 전달하는 텀을 주는 역할
    msg.angular.z = 0.0
    pub.publish(msg)
    pass

if __name__ == '__main__':
    main()


