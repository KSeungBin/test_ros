import rclpy
import rclpy.node

class MinimalParam(rclpy.node.Node):
    def __init__(self):
        super().__init__('minimal_param_node') # 노드 초기화
        timer_period = 2  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback) # 2초마다 callback 함수 실행

        self.declare_parameter('my_parameter', 'world') # parameter의 이름 지정, default 지정

    def timer_callback(self):
        my_param = self.get_parameter('my_parameter').get_parameter_value().string_value

        self.get_logger().info('Hello %s!' % my_param) 

        my_new_param = rclpy.parameter.Parameter(
            'my_parameter',
            rclpy.Parameter.Type.STRING, # type은 string,values는 world
            'world'   # 초기화하는 부분이 callback함수 안에 있기 때문에 값을 바꾸면 한번만 바꿔지고, 2초뒤에는 다시 hello world! 출력됨
        )
        all_new_parameters = [my_new_param] # rclpy.parameter가 list type 
        self.set_parameters(all_new_parameters)

def main():
    rclpy.init()
    node = MinimalParam()
    rclpy.spin(node)

if __name__ == '__main__':
    main()