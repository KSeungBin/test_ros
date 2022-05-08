import rclpy
from rclpy.node import Node
from std_msgs.msg import String
class BasicSubscriber(Node):
    def __init__(self):
        super().__init__('basic_subscriber') # node name
        self.subscription = self.create_subscription(
            String,   # msg type
            'basic_pubsub', # topic name
            self.listener_callback, # topic으로 데이터가 들어왔을 때 실행할 callback function
            10)
        self.subscription
    def listener_callback(self, msg):
        self.get_logger().info('Received: "%s"' % msg.data)
def main(args=None):
    rclpy.init(args=args)
    basic_subcriber = BasicSubscriber()
    rclpy.spin(basic_subcriber) # class를 만들고, 함수를 설계해도 spin을 하지 않으면 node가 실행되지 않음
    basic_subcriber.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()