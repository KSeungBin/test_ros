import rospy
import cv2 as cv
from sensor_msgs.msg import Image
from cv_bridge import CvBridge  
bridge = CvBridge()     

# ROS Image를 opencv로 받기
def callback(image_data):
    cv_image = bridge.imgmsg_to_cv2(image_data, 'bgr8')  
    cv.imshow('callback', cv_image)
    cv.waitKey(1)  
    pass

rospy.init_node('img2_cv_node')
rospy.Subscriber('/camera/image_raw', Image, callback)  
rospy.spin()    








