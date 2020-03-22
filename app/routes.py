from app import app
from flask import render_template, request
from app.messages.main import return_msgs
import json, os
from flask.json import jsonify
from app.models import Features
from app import db
from datetime import datetime

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/result', methods = ['POST', 'GET'])
def add_entry():
    if request.method == 'POST':
        result = request.form
        r = result.to_dict(flat=False)
        print(r)

    print(type(r["demise_date"][0]))

    dobj = datetime.strptime(r["demise_date"][0], "%Y-%m-%d")

    print(type(dobj))

    f = Features(name=r["name"][0], demise_place=r["demise_place"][0], demise_date=dobj, age=int(r["age"][0]))
    db.session.add(f)
    db.session.commit()

    print("Data added to database")
    print(os.getcwd())

    db.session.flush()
    resId = f.id

    print("resId", resId)

    ftrs = Features.query.filter_by(id=resId)
    for i in ftrs:
        r = {
            "name": i.name,
            "demise_date": i.demise_date,
            "demise_place": i.demise_place,
            "age": i.age
        }

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

if __name__ == "__main__":
    app.run()