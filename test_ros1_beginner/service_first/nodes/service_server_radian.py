#! /usr/bin/env python3


import rospy
from service_first.srv import divideangle, divideangleResponse

def func_callback(req):
    rospy.loginfo('%s, %s' % (req.a, req.b))    
    return divideangleResponse(req.a / req.b)  # input = 속력 , 시간 -> result = 거리

if __name__ == '__main__':
    rospy.init_node('dividetwo')
    rospy.Service('dividetwo',divideangle, func_callback) 
    rospy.spin()  
    pass           


