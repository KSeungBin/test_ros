from flask import Flask

app = Flask(__name__)  # 인스턴스화

@app.route("/") # 브라우저의 경로와 함수 지정
def helloworld():
    str = "Hello World! Seungbin"
    return str

app.run(host='0.0.0.0', port='8000')    #runserver - flask가 서버처럼 동작


