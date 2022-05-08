from example_interfaces.srv import AddTwoInts

import rclpy
from rclpy.node import Node


class BasicServiceServer(Node):

    def __init__(self):
        super().__init__('basic_service_server') # 부모 class(=Node)를 상속받은 basic_service_server node
        self.srv = self.create_service(AddTwoInts, 'add_two_ints', self.service_callback)

    def service_callback(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info('Incoming request\na: %d b: %d' % (request.a, request.b))

        return response


def main(args=None):
    rclpy.init(args=args)

    basic_service_server = BasicServiceServer()

    rclpy.spin(basic_service_server) #loop를 계속 돈다

    rclpy.shutdown()


if __name__ == '__main__':
    main()