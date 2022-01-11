import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64
class SumCalculator(Node):
    def __init__(self):
        super().__init__('sum_calculator') # node name
        self.subscription = self.create_subscription(
            Int64,   # msg type
            'natural_number_signal', # topic name
            self.listener_callback, # topic으로 데이터가 들어왔을 때 실행할 callback function
            10)
        self.subscription
        self.sum = 0
    
    def listener_callback(self, msg):
        self.sum += msg.data
        self.get_logger().info('Received: {0} | Sum: {1}'.format(msg.data, self.sum))
        
def main(args=None):
    rclpy.init(args=args)
    sum_calculator = SumCalculator()
    rclpy.spin(sum_calculator) # class를 만들고, 함수를 설계해도 spin을 하지 않으면 node가 실행되지 않음
    sum_calculator.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main()