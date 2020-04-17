## Directory Tree
```
+-- app (flask sevice)
   +-- messages (CBR/Lazy learning part)
      +-- data (Case-Base)
         +-- basic.csv
         +-- personal_info_component.csv
         +-- funeral_component.csv
         +-- relations_component.csv
      +-- resources 
         +-- feature_list.csv 
      +-- __init__.py
      +-- errors.py
      +-- funeral.py
      +-- main.py
      +-- personal_info.py
      +-- relations.py
      +-- basic.py
      +-- README.md
   +-- templates (HTML templates)
         +-- index.html
   +-- __init__.py
   +-- routes.py (flask routes)

+-- labelling (data labelling framewrok)
   +-- data
      +-- basic.csv
      +-- personal_info_component.csv
      +-- funeral_component.csv
      +-- relations_component.csv
   +-- resources
      +-- tagged.json1
      +-- xml-tagged.xml
      +-- xml-tagged-comps.xml
   +-- create_csv.py
   +-- create_csv_comps.py
   +-- create_xml.py
   +-- README.md

+-- reports (technical reports)
   +-- images
      +-- basic.png (example output from basic-retrieval method).
      +-- comps.png (example output from component-retrieval method).
      +-- input-form.png (screen capture of input form).
   +-- flask-app-report.pdf.
   +-- ICCBR-accepted-paper.pdf.

+-- migrations (database: useless)

+-- cbrobit.py (main flask file)
+-- LICENSE
+-- README.md
```
**Note**: Files other than listed here might not be useful.

## Instructions to run
- First, install the required libraries:
   - `pip install -r requirements.txt`

- Run on Unix Bash (Linux, Mac):
    - ```export FLASK_ENV="development"```
    - ```export FLASK_APP="cbrobit.py"```
    - ```flask run```

- Run on Windows Powershell:
    - ```$env:FLASK_ENV="development"```
    - ```$env:FLASK_APP="cbrobit.py"```
    - ```flask run```

- Run on Windows CMD:
    - ```set FLASK_ENV="development"```
    - ```set FLASK_APP="cbrobit.py"```
    - ```flask run```

## Input-Output system
- On `https://localhost:5000` there will be a form for different feature values. A screen capture is shown here:
![Basic Retrieval](/reports/images/input-form.png)
- After submitting the form you will get a `json` file with a dictionary of features given as input and four possible obituaries.
- An example of obituaries generated from `basic-retrieval` method.
![Basic Retrieval](/reports/images/basic-out.png)
- An example of obituaries generated from `component-retrieval` method.
![Component Retrieval](/reports/images/comp-out.png)

## Technical Reports
- A technical report about Flask-app can be found [here](/reports/flask-app-report.pdf).
- The accepted paper at ICCBR on the experiments performed can be found [here](/reports/ICCBR-accepted-paper.pdf).

## TODO
- ~~Similarity measure in component retrieval.~~ **Done**
- Edge cases:
   - ~~Morphology: Things like appropriate use of 'he' or 'she'.~~ **Done**
      - ~~Possible solution: Adding the rule-based error handling.~~ **Done**
   - Orthology: Things like one full stops only (mostly occurs in `component-retrieval`).
      - Possible solution: Deep learning based solution adaptaion.
      <!-- - Ongoing deep learning framework, but is not feasible yet -->
   - Modify the feature list to handle edge-cases with a special care for _relations_ section.
- ~~Add the framework for data labelling.~~ **Done**
   - ~~First manual labelling in Doccano.~~
   - ~~Second, conversion of Doccano's format into XML.~~
   - ~~Third, conversion of XML into tabular form, i.e., CSV.~~
   <!-- - **Imp.**: Right now automated conversion of  is only supported for `basic-retrieval` method. -->
- ~~Add a list of features categorised in component type.~~ **Done**
- ~~Remove the tags from generated text which are not given in input.~~ **Done**
- Maybe break the obituary into two sections, 'funeral' and 'non-funeral', for sending it back.
- Try to add message about earlier life.
   - Possible Solution: Collect more data reflecting messages on earlier life.

## Longer Goal
- Add more data.
- Add Active Learning for data labelling.
