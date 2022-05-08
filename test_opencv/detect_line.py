import cv2 as cv

# 빛이 없거나 실내처럼 자연광 변화가 없는 환경에서 image detecting하려면 grayscale로 만드는 것이 좋음
# 외부, 시간에 따라 자연광과 빛의 방향이 바뀌는 환경에서는 hsl이나 hsv를 사용해야 함
gray_img = cv.imread('./image/center.png', cv.IMREAD_GRAYSCALE)
cv.imshow('gray_img', gray_img)

rect_img = cv.rectangle(gray_img, (92,418),(117,460), (0,0,255),3) 
rect_img = cv.rectangle(gray_img, (129,418),(154,460), (0,0,255),3)
cv.imshow('rect_img', rect_img)


left_img = gray_img[418:460, 92:117]  # 세로, 가로
right_img = gray_img[418:460, 129:154]
cv.imshow('left_img', left_img )
cv.imshow('right_img', right_img )
import numpy as np # img의 data type이 array. 비교를 하려면 벡터로 값을 지정해야 함

# np.where(left_img > 90)  박스 안에 line이 얼마나 들어와 있는지 판단할 때
if not np.all(left_img > 100):  # 하나라도 90이 넘는게 있다면 false : Right 프린트됨 
    print('Right Empty')  # 'LEFT' 명령해야 함
    pass
if not np.all(right_img > 100):   # if np.all(right_img < 90)
    print('Left Empty')
    pass

cv.waitKey(1)  # 0으로 두면 영상이 들어오지 않음!


