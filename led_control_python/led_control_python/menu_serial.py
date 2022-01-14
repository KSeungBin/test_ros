# -*- coding: utf-8 -*-
__author__ = 'e2g1234@naver.com'



import time
import serial
ser = serial.Serial ("/dev/ttyACM0", 115200)

def main_menu():
  print("-------------------------------------------------")
  print(" LIST MENU")
  print("-------------------------------------------------")
  print('1. LED1 ON - OFF ')
  print('2. LED2 ON - OFF ')
  print('3. LED3 ON - OFF ')
  print('4. LED4 ON - OFF ')
  print('5. LED 1 2 3 4 ON - OFF')
  print("-------------------------------------------------")
  print(" q. QUIT")
  print("-------------------------------------------------")
  print()
  #print("SELECT THE COMMAND NUMBER : ")
  key = input("SELECT THE COMMAND NUMBER : ")
  return key


while True :
  key = main_menu()
  if key == '1':
    ser.write(bytes('1','utf-8'))
    time.sleep(2)
  elif key == '2':
    ser.write(bytes('2','utf-8'))
  elif key == '3':
    ser.write(bytes('3','utf-8'))
  elif key == '4':
    ser.write(bytes('4','utf-8'))
  elif key == '5':
    ser.write(bytes('1','utf-8'))
    time.sleep(0.1)
    ser.write(bytes('2','utf-8'))
    time.sleep(0.1)
    ser.write(bytes('3','utf-8'))
    time.sleep(0.1)
    ser.write(bytes('4','utf-8'))
    time.sleep(0.1)


  elif key == 'q':
    print('exit app')
    break
  else:
    print('Wrong key try again', key)