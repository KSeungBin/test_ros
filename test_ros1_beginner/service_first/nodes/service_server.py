#! /usr/bin/env python3

import rospy

# 누가 요청을 받아 계산할 것인지
# server는 응답을 주는 역할
from service_first.srv import addtwoints, addtwointsResponse

# callback함수로 return하면 됨(response)
def func_callback(req):
    rospy.loginfo('%s, %s' % (req.a, req.b))   # request한 것(a+b)을 뿌려줌  
    return addtwointsResponse(req.a + req.b)

if __name__ == '__main__':
    # server 선언
    rospy.init_node('addtwo') # 서비스 이름을 넣어야 함
    # server 기다리기
    rospy.Service('addtwo',addtwoints,func_callback) # 서비스 이름, 서비스 type, callback함수  
    #server 답변
    rospy.spin()   # 주기를 계산하는 3가지 중 spin을 사용 : 주로 sensor에 spin 사용(메세지를 보내는 주기를 기계에 맡기는 것)
    pass           # rate는 프로그래머가 임의적으로 주기를 조절할 수 있음 - keyboard로 입력하는 경우는 rate 사용하는 것이 좋음


