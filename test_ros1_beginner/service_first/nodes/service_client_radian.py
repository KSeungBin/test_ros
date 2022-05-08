#! /usr/bin/env python3

import rospy
from service_first.srv import divideangle


if __name__ == '__main__':
    rospy.wait_for_service('dividetwo')  
    divide_two_floats = rospy.ServiceProxy('dividetwo', divideangle) 
    result = divide_two_floats(180 , 3.1415)      
    print(result)


