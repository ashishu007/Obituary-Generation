from app import app
from flask import render_template, request
from app.messages.main import return_msgs
import json, os
from flask.json import jsonify

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/result', methods = ['POST', 'GET'])
def index():

    print(os.getcwd())

    if request.method == 'POST':
        result = request.form
        r = result.to_dict(flat=False)
        print(r)

    lst = return_msgs(r)
    op1 = lst[0]
    op2 = lst[1]
    op3 = lst[2]
    op4 = lst[3]
    return jsonify(
        [
            {"Option 1:": op1},
            {"Option 2:": op2},
            {"Option 3:": op3},
            {"Option 4:": op4}
        ]
    )

    # return render_template("result.html", result = result)

if __name__ == "__main__":
    app.run()