from app import app
from flask import render_template, request
from app.messages.main import return_comp_messages, return_basic_msgs
import json, os
from flask.json import jsonify
from app.models import Features
from app import db
from datetime import datetime

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/result', methods=['POST','GET'])
def send_obits():
    if request.method == 'POST':
        result = request.form
        r = result.to_dict(flat=False)
        print(r)

    ftrs = {}

    for key, val in r.items():
        if len(val[0]) != 0:
            if key == "demise_date" or key == "funeral_date":
                dobj = datetime.strptime(val[0], "%Y-%m-%d")
                ftrs[key] = dobj
            elif key == "ret_met":
                pass
            else:
                ftrs[key] = val[0]

    if ftrs["gender"] == "M":
        print("inside if M")
        if "spouse_name" in list(ftrs.keys()):
            ftrs["spouse_gender"] = "husband"
        if "children_name" in list(ftrs.keys()):
            ftrs["parent_gender"] = "father"
        if "grandchildren_name" in list(ftrs.keys()):
            ftrs["grandparent_gender"] = "papa"
        if "great_grandchildren_name" in list(ftrs.keys()):
            ftrs["great_grandparent_gender"] = "great papa"
        if "children_in_law_name" in list(ftrs.keys()):
            ftrs["parent_in_law_gender"] = "father in law"
        if "siblings_name" in list(ftrs.keys()):
            ftrs["siblings_gender"] = "brother"

    if ftrs["gender"] == "F":
        print("inside if F")
        if "spouse_name" in list(ftrs.keys()):
            ftrs["spouse_gender"] = "wife"
        if "children_name" in list(ftrs.keys()):
            ftrs["parent_gender"] = "mother"
        if "grandchildren_name" in list(ftrs.keys()):
            ftrs["grandparent_gender"] = "nana"
        if "great_grandchildren_name" in list(ftrs.keys()):
            ftrs["great_grandparent_gender"] = "great nana"
        if "children_in_law_name" in list(ftrs.keys()):
            ftrs["parent_in_law_gender"] = "mother in law"
        if "siblings_name" in list(ftrs.keys()):
            ftrs["siblings_gender"] = "sister"

    print(ftrs)

    if r["ret_met"][0] == "basic":
        print("Its basic")
        lst = return_basic_msgs(ftrs)
    else:
        print("Its component")
        lst = return_comp_messages(ftrs)

    return jsonify(
        [
            {"Features:": ftrs},
            {"Option 1:": lst[0]},
            {"Option 2:": lst[1]},
            {"Option 3:": lst[2]},
            {"Option 4:": lst[3]}
        ]
    )


# This is an useless path when I just tried to incorporate database in the service.
@app.route('/resultdb', methods = ['POST', 'GET'])
def add_entry():
    if request.method == 'POST':
        result = request.form
        r = result.to_dict(flat=False)
        print(r)

    # print(type(r["demise_date"][0]))

    dobj = datetime.strptime(r["demise_date"][0], "%Y-%m-%d")

    # print(type(dobj))

    f = Features(name = r["name"][0], demise_place = r["demise_place"][0], demise_date = dobj, age = int(r["age"][0]), \
                    demise_how = r["demise_how"][0], demise_reason = r["demise_reason"][0], home_town = r["home_town"][0])

    db.session.add(f)
    db.session.commit()

    print("Data added to database")
    print(os.getcwd())

    db.session.flush()
    resId = f.id

    print("resId", resId)

    ftrs = Features.query.filter_by(id=resId)
    ctr = 0

    for i in ftrs:
        print(ctr)
        ctr += 1
        r = {
            "name": i.name,
            "demise_date": i.demise_date,
            "demise_place": i.demise_place,
            "age": i.age,
            "demise_reason": i.demise_reason,
            "demise_how": i.demise_how,
            "home_town": i.home_town
        }

    lst = return_basic_msgs(r)

    return jsonify(
        [
            {"Features:": ftrs},
            {"Option 1:": lst[0]},
            {"Option 2:": lst[1]},
            {"Option 3:": lst[2]},
            {"Option 4:": lst[3]}
        ]
    )

if __name__ == "__main__":
    app.run()