from flask import Flask, request #to get input from user

app = Flask(__name__)

@app.route('/')
def add():
    a = request.args.get("a")
    b = request.args.get("b")
    return str(int(a)+int(b))

#manggilnya http://127.0.0.1:7000?a=10&b=20

if __name__ == '__main__':
    app.run(port = 7000)

#bisa atur port dengan app.run()