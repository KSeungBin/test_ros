def func():
    pass
    return


if __name__ == '__main__':
    try:
        fh = open('./testfile.txt', 'w') # 현재 디렉토리의 testfile.txt 파일 열기 # ../testfile.txt 넣고 디버깅 모드 실행해보기
        fh.write('This is exception finally.')
    except Exception as e:
        pass
    finally:
        fh.close()  # exception이 있든 없든 finally는 반드시 거쳐간다는 장점이 있음
pass
