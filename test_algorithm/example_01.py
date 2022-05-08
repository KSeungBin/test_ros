def func01():
    a = 50
    b = 20
    return a + b

def func02():
    c = 10
    d = 0
    return c * d, c / d

# def func():
#     pass
#     return

if __name__ == '__main__':
    try:
        func01()
        func02()
        

    except ZeroDivisionError:
        d = 1
        pass
    except Exception as e:
        pass

