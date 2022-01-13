import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node
from basic_interface.action import Counter
import random
import time



class RandomActionServer(Node):

    def __init__(self):
        super().__init__('random_action_server')
        self._action_server = ActionServer(
            self,
            Counter,
            'counter',
            self.execute_callback)   # 깂이 들어오면 

    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')
        feedback_msg = Counter.Feedback()
       
        while True:
            feedback_msg.remainder = random.randrange(1,11)
            self.get_logger().info('Feedback: {0}'.format(feedback_msg.remainder))
            goal_handle.publish_feedback(feedback_msg) # 4. action server가 1초마다 feedback topic 발행
            time.sleep(1)
        
            if feedback_msg.remainder == goal_handle.request.order:
                break


        goal_handle.succeed()   # goal_handle을 succeed로 바꾸고 result(server의 역할 끝)
        result = Counter.Result()
        result.multiple = feedback_msg.remainder
        return result


def main(args=None):
    rclpy.init(args=args)
    random_action_server = RandomActionServer()
    rclpy.spin(random_action_server)


if __name__ == '__main__':
    main()