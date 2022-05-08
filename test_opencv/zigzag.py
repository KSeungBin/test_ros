import rospy
from geographic_msgs.msg import Twist

def main():
    rospy.init_node('zigzag')
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    msg = Twist()   # publish할 때마다 메세지를 계속 보내려면 인스탄스화 or 초기화 해야 함
    
    rate = rospy.Rate(3)
    while not rospy.is_shutdown():
        msg.linear.x = 0.1   # 시스템이 종료될 때까지 메세지를 반복적으로 보냄
        msg.angular.z = 0.3
        time2end = 0
        while time2end < 10 :
            pub.publish(msg)
            rate.sleep()
            time2end = time2end + 1 # time2end += 1  # while문 도는 속도는 모르겠지만 시간이 10이 되기 전까지는 계속 publishing해

        msg.linear.x = 0.1   
        msg.angular.z = -0.3
        time2end = 0
        while time2end < 10 :
            pub.publish(msg)
            rate.sleep()
            time2end = time2end + 1
    pass

if __name__ == '__main__':
    main()




