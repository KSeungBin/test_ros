from flask import Flask
from flask.wrappers import Response

app = Flask(__name__)  

@app.route("/") 
def helloworld():
    str = "Hello World! Seungbin"
    return str




video_frame = ''
import cv2 as cv

# thread로 돌아가는데 capture한 것을 받으려면 확장자를 global로 선언해야 함
def encodeframe():
    global video_frame
    

    while True:
        ret, encoded_image = cv.imencode('.jpg', video_frame) # 3차원 이미지를 네트워크에 실어 보내기 위해 flat한 일렬(byte)로 보냄
    # send streaming yield : 시간은 느리더라도, 브라우저로 갈 때 유실되지 않게 해줌
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encoded_image) + b'\r\n')
    return

@app.route('/streaming')  # 브라우저와 소통하기 위한 코드(브라우저 url에 streaming이라고 넣어줘야 함)
# 글자가 아닌 이미지 자체를 리턴하는 함수
def streamframe():
    return Response(encodeframe(), mimetype='multipart/x-mixed-replace; boundary=frame')
# 브라우저에 response되는 값 : encodeframe에서 return되는 값을 muptipart 형식으로 frame으로 bound하여 계속 보내줌


def captureframe():
    global video_frame
    cap = cv.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()  # return, frame 2개가 날아옴
        # cv.imshow('webcam', frame)
        frame = cv.rotate(frame, cv.ROTATE_180)
        video_frame = frame.copy()
        cv.waitKey(30)  # frame capture하는 시간을 넉넉히 주기(frame 횟수 제한)
        pass
    # return


import threading
if __name__ == '__main__':
    cap_thread = threading.Thread(target=captureframe)
    cap_thread.daemon = True
    cap_thread.start()
    app.run(host='0.0.0.0', port='8000')
    pass




    



