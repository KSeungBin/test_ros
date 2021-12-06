import serial

opencr = serial.Serial(port = '/dev/ttyACM0', baudrate = 115200, timeout = 1  )
# boardrate는 begin에 넣어준 값과 동일해야 함.머신과 통신할 때는 timeout 무조건 들어가야 한다
# opencr이 serial이 됨

while True:
    number = input('Enter a number: ')
    opencr.write(bytes(number), 'utf-8')    # ASCII로 날아가야 상대가 받을 수 있음(ASCII는 2진수로 날아감) : 35를 보내면, 3과 5(문자)로 받아들임
    value = opencr.readline()
    print('Result: ', value)
    