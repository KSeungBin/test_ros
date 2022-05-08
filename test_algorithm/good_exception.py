def ques():
    a = float(input('input num1 : '))
    b = float(input('input num2 : '))
    return a,b

def func(a,b):
    plus = a+b
    mult = a*b
    dev = a/b
    return plus,mult,dev

while 1:
    try:
        a,b = ques()
        plus,_,_ = func(a,b)
        print(plus)
    
        a2,b2= ques()
        _,mult,dev = func(a2,b2)
        print(mult,dev)

    except ValueError:
        print('u have to input int or float')
        continue
    
    except ZeroDivisionError:
        print('cant devision by 0')
        continue
    finally:
        try:
            print('plus = ',plus,'multiply = ',mult,'devision = ',dev)
            break
        except:
            continue