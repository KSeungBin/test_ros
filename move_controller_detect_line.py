#! /usr/bin/env python3
import rospy
import cv2 as cv
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge  
bridge = CvBridge()      


# 카메라 image를 봐야 키 조작을 할 수 있음 - callback(image가 오면 동작)함수 안에 넣어주는 것이 좋다
direction = None       # direction은 글로벌 변수 선언
pub = rospy.Publisher('/motor_commands', String, queue_size=10)
def callback(image):   # 이름은 msg, data 뭐든 상관 없음. 
    global direction  
    cv_image = bridge.imgmsg_to_cv2(image, 'bgr8')  # opencv는 rgb가 아닌 bgr로 바꿔줘야 함, 8bit로 비트 수는 맞춰주기
    cv.imshow('callback', cv_image)
    key = cv.waitKey(1) 
        # 전진(GO)
    if key == ord('w'):
        direction = 'GO'
        # STOP
    elif key == ord('s'):
        direction = 'STOP'
        # BACK
    elif key == ord('x'):
        direction = 'BACK'
        # LEFT
    elif key == ord('a'):
        direction = 'LEFT'
        # RIGHT
    elif key == ord('d'):
        direction = 'RIGHT'
    pub.publish(direction)
    # rospy.sleep(0.3)


import numpy as np
def detect_line():
    gray_img = cv.imread('./image/center.png', cv.IMREAD_GRAYSCALE)
    rect_img = cv.rectangle(gray_img, (92,418),(117,460), (0,0,255),3)  # (x, y) 
    rect_img = cv.rectangle(gray_img, (129,418),(154,460), (0,0,255),3)
    cv.imshow('rect_img', rect_img)

    left_img = gray_img[418:460, 92:117]  # 세로(y), 가로(x)
    right_img = gray_img[418:460, 129:154]


    if not np.all(left_img > 100):
        print('Right Empty')
        pub.publish('LEFT')
    
    if not np.all(right_img > 100):   # if np.all(right_img < 90)
        print('Left Empty')
        pub.publish('RIGHT')
    
    cv.waitKey(1)

def main():
    rospy.init_node('planner_node')
    rospy.Subscriber('/camera/image_raw', Image, callback) # 영상을 보면서 좌우 변환을 하기 때문에 필요 # callback 앞에 있는 변수가, callback함수의 param으로 들어감
    rospy.spin()


    
if __name__ == '__main__':
    main()
    detect_line()
    pass
