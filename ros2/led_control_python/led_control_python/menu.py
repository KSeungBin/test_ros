# -*- coding: utf-8 -*-
__author__ = 'e2g1234@naver.com'
def main_menu():
  print("-------------------------------------------------")
  print(" LIST MENU");
  print("-------------------------------------------------")
  print('1. 정수형(Integer)')
  print('2. 소수점 포함된 것(Floating-point)')
  print('3. 8비트형 수(Octal)')
  print('4. 16비트형 수(Hexadecimal)')
  print('5. 복소수 (Complex number)')
  print('6. 복소수 - 실수(a.real)')
  print('7. 복소수 - 허수(a.imag)')
  print('8. 복소수 - 켤레(a.conjugate)')
  print('9. 복소수 - 절대값(a.abs)')
  print('0. 숫자 연산 - + * / ** %')
  print("-------------------------------------------------")
  print(" q. QUIT");
  print("-------------------------------------------------")
  print()
  #print("SELECT THE COMMAND NUMBER : ")
  key = input("SELECT THE COMMAND NUMBER : ")
  return key
while True :
  key = main_menu()
  '''   
  리스트에 요소 추가 (append)
  append의 뜻이 무엇인지 안다면 아래의 예가 금방 이해가 될 것이다. append(x)는 리스트의 맨
  마지막에 x를 추가시키는 함수이다.
  '''
  if key == '1':
    print('No.1')
    #코드 시작
    a = 123
    print('a = 123', a)
    a = -178
    print(a)
    a = 0
    print(a)
    #코드 끝
    '''
    '''
  elif key == '2':
    print('No.2')
    #코드 시작
    a = 1.2
    print(a)
    a = -3.45
    print(a)
    a = 4.24E10 # 4.24 * 10의 10승
    print(a)
    a = 4.24e-10 # 4.24 * 10의 마이너스 10승
    print(a)
    #코드 끝
  elif key == '3':
    print('No.3')
    #코드 시작
    #a = 0177   # 2 버젼
    a = 0o177   # 8bit
    print(a)
    #코드 끝
  elif key == '4':
    print('No.4')
    #코드 시작
    a = 0x8ff   # 16진수
    print(a)
    b = 0xABC   
    print(b)
    #코드 끝
  elif key == '5':
    print('No.5')
    #코드 시작
    a = 1+2j
    print(a)
    b = 3-4J
    print(b)
    #코드 끝
  elif key == '6':
    print('No.6')
    #코드 시작
    a = 1+2j
    print(a.real)
    #코드 끝
  elif key == '7':
    print('No.7')
    #코드 시작
    a = 1+2j
    print(a.imag)
    #코드 끝
  elif key == '8':
    print('No.8')
    #코드 시작
    a = 1+2j
    print(a.conjugate())
    #(1-2j)   
    #코드 끝
  elif key == '9':
    print('No.9')
    #코드 시작
    a = 1+2j
    print(abs(a))  
    #코드 끝
  elif key == '0':
    print('No.0')
    #코드 시작
    a=3
    b=4
    print('a+b', a+b)
    input('any key for next')
    print('a*b', a*b)
    input('any key for next')
    print('3/4', 3/4)  # 정수 나누기
    input('any key for next')
    print('3/4.0', 3/4.0)  # 실수 나누기
    input('any key for next')
    print('3.0/4', 3.0/4)  # 실수 나누기
    input('any key for next')
    print('float(a)/b', float(a)/b)  # 실수 나누기
    input('any key for next')
    print('a**b', a**b)   # 승
    input('any key for next')
    print('7%3', 7%3)   # 모듈러
    input('any key for next')
    print('3%7', 3%7)   # 모듈러
    #코드 끝
  elif key == 'q':
#  elif key == 27:
#  elif key == 0x37:
#  elif repr(key.keysym) == "Escape":
#  elif key.keysym[0] == "Escape":
    print('exit app')
#    continue
    break
  else:
    # print('Wrong no. try again', key, int(key))
    print('Wrong key try again', key)