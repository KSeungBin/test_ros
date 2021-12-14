#! /usr/bin/env python3

import rospy
from service_first.srv import addtwoints

# 누가 요청할 것인지
# custom service message : topic은 가는 것만 있음, service는 가는 게 있고 오는 것(response)도 있음

if __name__ == '__main__':
    # 요청만 하면 되니까 node가 필요 없음 : 프로세스는 요청만 하고 사라짐, 자신이 응답을 받을 때까지 대부분 기다리는 역할만 함
    rospy.wait_for_service('addtwo')  
    add_two_ints = rospy.ServiceProxy('addtwo', addtwoints)  # 서비스 이름, 서비스의 data type
          # 전달이 되면 add_two_ints가 function화 된다 : proxy에서 받은 addtwoints 서비스를 인자로 갖는 function이 만들어짐
    result = add_two_ints(3,4)    # addtwoints.srv의 int64 result가 됨
    print(result)


