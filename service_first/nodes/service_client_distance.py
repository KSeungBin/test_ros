#! /usr/bin/env python3

import rospy
from service_first.srv import multiplyfloats


if __name__ == '__main__':
    rospy.wait_for_service('multiplytwo')  
    multiply_two_floats = rospy.ServiceProxy('multiplytwo', multiplyfloats) 
    result = multiply_two_floats(3.5 ,4.1)    
    print(result)


