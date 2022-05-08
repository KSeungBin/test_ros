import rospy
from geographic_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import numpy as np

def callback(data): # callback은 데이터(LaserScan)를 받는다
    laser_range = data.ranges[0:10] # range list에 들어간 0~360도 데이터 중에서 정면 데이터만 사용
    laser_arr = np.array(laser_range)
    result = np.count_nonzero(laser_arr >= 0.2)
    cmd_vel = Twist()
    if result > 0:
        cmd_vel.linear.x = 0.1   # MOVE
    else:
        cmd_vel.linear.x = 0.0   # STOP
        # print('end scan')
    pub.publish(cmd_vel)
    pass

if __name__ == '__main__':
    rospy.init_node('parking')
    rospy.Subscriber('/scan', LaserScan, callback) # scan을 받아들일 때마다 callback 동작
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size = 10)
    rospy.spin()    




