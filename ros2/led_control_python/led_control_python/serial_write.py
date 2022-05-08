import time
import serial  # serial 통신을 하기 위함 : python에 내장되어 있음
from time import sleep
ser = serial.Serial ("/dev/ttyACM0", 115200) #Open port with baud rate
if __name__ == '__main__':
    ser.write(bytes('1', 'utf-8')) #transmit data serially
    time.sleep(2)
    ser.write(bytes('2', 'utf-8')) #transmit data serially
    time.sleep(2)
    ser.write(bytes('3', 'utf-8')) #transmit data serially
    time.sleep(2)
    ser.write(bytes('4', 'utf-8')) #transmit data serially
    time.sleep(2)