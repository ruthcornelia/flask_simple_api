from flask import Flask, request #to get input from user

app = Flask(__name__)

@app.route('/hello_world',methods=['GET', 'POST'])
def add():
    #a = request.form["a"]
    #b = request.form["b"]
    return "Hello World!" #str(int(a)+int(b))

#manggilnya http://127.0.0.1:5000/hello_world

#def predict(house_size, house_beds):
#    prediction = ml_model.predict(house_size, house_beds)
#    return prediction

if __name__ == '__main__':
    app.run(port=7000)

#bisa atur port dengan app.run()
#pake Postman