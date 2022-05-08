import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node

from action_tutorials_interfaces.action import Fibonacci


class FibonacciActionClient(Node):

    def __init__(self):
        super().__init__('fibonacci_action_client')
        self._action_client = ActionClient(self, Fibonacci, 'fibonacci') # action name = fibonacci

    # 1번 : action client가 goal request(service) 요청
    def send_goal(self, order):
        goal_msg = Fibonacci.Goal() # action file의 goal(목표) 생성
        goal_msg.order = order   # order는 데이터를 담는 역할(10이 입력됨) , request시 사용할 데이터 지정

        self._action_client.wait_for_server()  # action server가 응답할 때까지 대기
        self._send_goal_future = self._action_client.send_goal_async(goal_msg, feedback_callback=self.feedback_callback) # 여기까지 1번
        self._send_goal_future.add_done_callback(self.goal_response_callback) # action server가 응답했을 때 goal_response_callback이 실행되는 것을 future 객체(인스턴스)의 메서드(add_done_callback)에 등록

    # 2번
    def goal_response_callback(self, future):
        goal_handle = future.result() # Goal Service에서의 response
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')  # client가 요청한 것을 server가 거절한 경우
            return

        self.get_logger().info('Goal accepted :)')
        self._get_result_future = goal_handle.get_result_async()  # 3번
        self._get_result_future.add_done_callback(self.get_result_callback) # future객체가 완료되면 get_result_callback 함수 실행

    # 5번
    def get_result_callback(self, future):
        result = future.result().result 
        self.get_logger().info('Result: {0}'.format(result.sequence)) # 결과 출력 : 맨 마지막 결과는 service로 온다
        rclpy.shutdown()


    # 4번
    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback
        self.get_logger().info('Received feedback: {0}'.format(feedback.partial_sequence))  # feedback은 계속 topic으로 value 전달됨


def main(args=None):
    rclpy.init(args=args)
    action_client = FibonacciActionClient()
    action_client.send_goal(10)
    rclpy.spin(action_client)


if __name__ == '__main__':
    main()