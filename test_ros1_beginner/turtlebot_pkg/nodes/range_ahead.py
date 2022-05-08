#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
import sensor_msgs.msg

pub = rospy.Publisher('/revised_scan', LaserScan, queue_size=10)
rev_scan = LaserScan()

# BEGIN MEASUREMENT
def scan_callback(msg):
    range_center = msg.ranges[len(msg.ranges)/2]
    range_left = msg.ranges[len(msg.ranges)-1]
    range_right = msg.ranges[0]
    print ("range ahead: left - %0.1f" %range_left, " center- %0.1f" %range_center,
    " right - %0.1f" %range_right)
    pub.publish(range_center, range_left, range_right)


#END MEASUREMENT
rospy.init_node('revised_scan', anonymous=True)
scan_sub = rospy.Subscriber('/scan', LaserScan, scan_callback)
rospy.spin() 