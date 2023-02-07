from flask import Flask, request #to get input from user

app = Flask(__name__)

@app.route('/',methods=["POST"])
def add():
    a = request.form["a"]
    b = request.form["b"]
    return str(int(a)+int(b))

#manggilnya http://127.0.0.1:5000

if __name__ == '__main__':
    app.run()

#bisa atur port dengan app.run()
#pake Postman