import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64
class NumberGenerator(Node):  # 상위 객체 상속
    def __init__(self):
        super().__init__('natural_number_generator')
        self.publisher_ = self.create_publisher(Int64, 'natural_number_signal', 10)  # msg 데이터타입, topic 명
        timer_period = 2
        self.timer = self.create_timer(timer_period, self.timer_callback)  # 2초마다 아래 정의한 callback함수 실행
        self.count = 1   # 1부터 count해야 factorial 계산 가능

    def timer_callback(self):   # 빈 데이터 하나 생성
        msg = Int64()
        msg.data = self.count
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing Natural Number: "%s"' % msg.data)
        self.count += 1
def main(args=None): # 진입점(entry_points)
    rclpy.init(args=args) # 초기화
    natural_number_generator = NumberGenerator()
    rclpy.spin(natural_number_generator)  
    natural_number_generator.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main() 