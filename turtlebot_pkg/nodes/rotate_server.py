#! /usr/bin/env python3

import rospy
from turtlebot_pkg.srv import rotateResult, rotateResultResponse

# callback함수로 return하면 됨(response)
def func_callback(req):
    # rospy.loginfo('%s' % (req.scan_sequence))
    print('scan : ', req.scan_sequence)   
    success = True
    message = 'This is Success!' 
    return rotateResultResponse(success, message)

if __name__ == '__main__':
    # server 선언
    rospy.init_node('rotate_server') # 서비스 이름을 넣어야 함
    # server 기다리기 : 메세지 주고 받을 때 내용이 동일해야 함
    rospy.Service('rotate_result',rotateResult,func_callback) # 서비스 이름, 서비스 type, callback함수  
    #server 답변
    rospy.spin()   # 주기를 계산하는 3가지 중 spin을 사용 : 주로 sensor에 spin 사용(메세지를 보내는 주기를 기계에 맡기는 것)
    pass           # rate는 프로그래머가 임의적으로 주기를 조절할 수 있음 - keyboard로 입력하는 경우는 rate 사용하는 것이 좋음


