from basic_interface.srv import AddTwoFloats
import rclpy
from rclpy.node import Node
from rclpy.service import Service

class SumServiceServer(Node):
    def __init__(self):
        super().__init__('sum_service_server')
        self.srv = self.create_service(AddTwoFloats, 'add_two_floats', self.service_callback)

    def service_callback(self, request, response):
        if request.o == '+':
            response.sum = request.a + request.b
        elif request.o == '-':
            response.sum = request.a - request.b
        elif request.o == 'x':
            response.sum = request.a * request.b
        elif request.o == '/':
            response.sum = request.a / request.b
        # response.min = request.a - request.b
        # response.mul = request.a * request.b
        # response.div = request.a / request.b
        self.get_logger().info('request content\na: %.2f b: %.2f' % (request.a, request.b))
        return response

def main(args=None):
    rclpy.init(args=args)
    sum_service_server = SumServiceServer()
    rclpy.spin(sum_service_server)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

   