import argparse

args = argparse.ArgumentParser() # ArgumentParser는 클래스이므로 인스턴스화하기 위해 변수로 받아야 함
args.add_argument('-x','--xVal',required=True) # required=True 안 넣으면 error : 필수로 넣어야할 것과 아닌 것 구분
                                               # argument 하나를 받아들일 준비

args.add_argument('-y','--yVal',required=False)  # 값이 없어도 error 안 남

argvar = vars(args.parse_args())
pass



