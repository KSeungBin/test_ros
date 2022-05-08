import rclpy
from rclpy.node import Node
from std_msgs.msg import String
class BasicPublisher(Node):  # 상위 객체 상속
    def __init__(self):
        super().__init__('basic_publisher')
        self.publisher_ = self.create_publisher(String, 'basic_pubsub', 10)  # msg 데이터타입, topic 명
        timer_period = 1
        self.timer = self.create_timer(timer_period, self.timer_callback)  # 1초마다 아래 정의한 callback함수 실행
        self.count = 0
    def timer_callback(self):   # 빈 데이터 하나 생성
        msg = String()
        msg.data = 'Count: %d' % self.count
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.count += 1
def main(args=None): # 진입점(entry_points)
    rclpy.init(args=args) # 초기화
    basic_publisher = BasicPublisher()
    rclpy.spin(basic_publisher)  # spin : 한 번 실행되면 프로세스가 종료될 때까지 토픽으로 메세지를 발행(센서데이터, 라이다데이터처럼 반복적으로 보내야 하는 경우 사용). spinonce는 한번만 발행
    basic_publisher.destroy_node()
    rclpy.shutdown()
if __name__ == '__main__':
    main() 