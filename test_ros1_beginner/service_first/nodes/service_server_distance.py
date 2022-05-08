#! /usr/bin/env python3


import rospy
from service_first.srv import multiplyfloats, multiplyfloatsResponse

def func_callback(req):
    rospy.loginfo('%s, %s' % (req.a, req.b))    
    return multiplyfloatsResponse(req.a * req.b)  # input = 속력 , 시간 -> result = 거리

if __name__ == '__main__':
    rospy.init_node('multiplytwo')
    rospy.Service('multiplytwo',multiplyfloats, func_callback) 
    rospy.spin()  
    pass           


