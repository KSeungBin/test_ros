import time

import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

from action_tutorials_interfaces.action import Fibonacci

'''
Fibonacci라는 action파일은 다음과 같이 생겼습니다!
int32 order
---
int32[] sequence
---
int32[] partial_sequence
'''


class FibonacciActionServer(Node):

    def __init__(self):
        super().__init__('fibonacci_action_server')
        self._action_server = ActionServer(
            self,
            Fibonacci,
            'fibonacci',
            self.execute_callback)   # 깂이 들어오면 

    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')


        feedback_msg = Fibonacci.Feedback()
        feedback_msg.partial_sequence = [0, 1]  # 초기화


        for i in range(1, goal_handle.request.order):  # client에서 order에 10을 넣어 전달했기 때문에 10번 돈다
            feedback_msg.partial_sequence.append(
                feedback_msg.partial_sequence[i] + feedback_msg.partial_sequence[i-1]) # 피보나치 리스트에 데이터 추가
            self.get_logger().info('Feedback: {0}'.format(feedback_msg.partial_sequence))
            goal_handle.publish_feedback(feedback_msg) # 4. action server가 1초마다 feedback topic 발행
            time.sleep(1)


        goal_handle.succeed()   # goal_handle을 succeed로 바꾸고 result(server의 역할 끝)
        result = Fibonacci.Result()
        result.sequence = feedback_msg.partial_sequence

        return result


def main(args=None):
    rclpy.init(args=args)
    fibonacci_action_server = FibonacciActionServer()
    rclpy.spin(fibonacci_action_server)


if __name__ == '__main__':
    main()