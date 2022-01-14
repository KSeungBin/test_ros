from basic_interface.srv import IsimpleLedControl

import rclpy
from rclpy.node import Node

import time
import serial


class LedControlServer(Node):

    def __init__(self):
        super().__init__('led_control_server')
        self.srv = self.create_service(IsimpleLedControl, 'led_control', self.service_callback)
        self.ser = serial.Serial ("/dev/ttyACM0", 115200)
    def service_callback(self, request, response):
        if request.command == 1:
            response.is_success = True
            # openCR과 serial 통신하는 코드
            self.ser.write(str.encode('1'))
            time.sleep(0.1)
            self.ser.write(str.encode('q'))
            time.sleep(0.1)
            self.ser.write(str.encode('w'))
            time.sleep(0.1)
            self.ser.write(str.encode('e'))
            time.sleep(0.1)
            self.ser.write(str.encode('r'))
            time.sleep(0.1)
            self.ser.write(str.encode('a'))
            time.sleep(0.1)
            self.ser.write(str.encode('s'))
            time.sleep(0.1)
            self.ser.write(str.encode('d'))
            time.sleep(0.1)
        else:
            response.is_success = False 
        self.get_logger().info('Command: %d' % request.command)
        return response


def main(args=None):
    rclpy.init(args=args)

    led_control_server = LedControlServer()

    rclpy.spin(led_control_server)

    rclpy.shutdown()


if __name__ == '__main__':
    main()