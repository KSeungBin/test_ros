import sys
from basic_interface.srv import AddTwoFloats
import rclpy
from rclpy.node import Node

class SumServiceClient(Node):
    def __init__(self):
        super().__init__('sum_service_client')
        self.client = self.create_client(AddTwoFloats, 'add_two_floats')
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for service server...')
        self.req = AddTwoFloats.Request()
    
    def send_request(self):
        self.req.o = sys.argv[1]
        self.req.a = float(sys.argv[2])
        self.req.b = float(sys.argv[3])
        self.future = self.client.call_async(self.req)

def main(args=None):
    rclpy.init(args=args)
    sum_service_client = SumServiceClient()
    sum_service_client.send_request()
    while rclpy.ok():
        rclpy.spin_once(sum_service_client)
        if sum_service_client.future.done():
            try:
                response = sum_service_client.future.result()
            except Exception as e:
                sum_service_client.get_logger().info(
                    'Service call failed: %r' % (e,))
            else:
                sum_service_client.get_logger().info('result % f' %
                    response.sum
                )
            break
    sum_service_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
           