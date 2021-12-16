import cv2 as cv

# 빛이 없거나 실내처럼 자연광 변화가 없는 환경에서 image detecting하려면 grayscale로 만드는 것이 좋음
# 외부, 시간에 따라 자연광과 빛의 방향이 바뀌는 환경에서는 hsl이나 hsv를 사용해야 함
gray_img = cv.imread('./image/center.png', cv.IMREAD_GRAYSCALE)
cv.imshow('gray_img', gray_img)

rect_img = cv.rectangle(gray_img, (121,527),(185,571), (0,0,255),3) # pt1, pt2, red, thickness
rect_img = cv.rectangle(gray_img, (270,521),(315,569), (0,0,255),3)
cv.imshow('rect_img', rect_img)


left_img = gray_img[121:159, 527:553]
right_img = gray_img[270:315, 539:558]

import numpy as np # img의 data type이 array. 비교를 하려면 벡터로 값을 지정해야 함

# np.where(left_img > 90)  박스 안에 line이 얼마나 들어와 있는지 판단할 때
if not np.all(left_img > 90):  # 하나라도 90이 넘는게 있다면 false : Right 프린트됨 
    print('Right Empty')  # 'LEFT' 명령해야 함
    pass
if not np.all(right_img > 90):   # if np.all(right_img < 90)
    print('Left Empty')
    pass

cv.waitKey(0)


