import serial


opencr = serial.Serial(port = '/dev/ttyACM0', baudrate = 115200, timeout = 1)

def BlinkBuzzer():
    c = input("enter a command(f,b,l,r,q): ")
    c = c.encode('utf-8')
    if c == 'f':
        opencr.write(c)
    elif c == 'b':
        opencr.write(c)
    elif c == 'l':
        opencr.write(c)
    elif c == 'r':
        opencr.write(c)
    elif c == 'q':
        opencr.write(c)

if __name__ == '__main__': 
        BlinkBuzzer()






    
