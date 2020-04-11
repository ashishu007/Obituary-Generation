## Instructions to run
- Run on windows powershell
    - ```$env:FLASK_ENV="development"```
    - ```$env:FLASK_APP="cbrobit.py"```
    - ```flask run```

## TODO
- ~~Similarity measure in component retrieval.~~ **Done**
- Edge cases:
   - Orthology: Things like one full stops only.
   - ~~Morphology: Things like appropriate use of 'he' or 'she'.~~ **Done**
- Modify the feature list to handle edge-cases.
   - Special care for relations section.
- Maybe break the obituary into two sections, 'funeral' and 'non-funeral', for sending it back.
- Try to add message about previous life.

## Longer Goal
- Add more data.
- Add the framework for data labelling.
   - First manual labelling in Doccano.
   - Second, conversion of Doccano's format into XML.
   - Third, conversion of XML into tabular form, i.e., CSV.
- Add Active Learning for data labelling.

<!-- ## Directory Tree
```
+-- app (flask sevice)
   +-- messages (CBR/Lazy learning part)
      +-- data (Case-Base)
         +-- 101_funeral_component.csv 
         +-- 101_personal_component.csv 
         +-- 101_relations_component.csv 
         +-- 101_single_component.csv 
      +-- __init__.py
      +-- funeral.py
      +-- main.py
      +-- personal_info.py
      +-- relations.py
      +-- single_comp.py
   +-- templates (HTML templates)
         +-- index.html
   +-- __init__.py
   +-- routes.py (flask routes)
+-- cbrobit.py (main flask file)
+-- LICENSE
+-- README.md
``` -->
<!-- ```
|--- cbrservice
|   |--- app 
|       |--- messages 
|           |--- data 
|               |--- 101_funeral_component.csv 
|               |--- 101_personal_component.csv 
|               |--- 101_relations_component.csv 
|               |--- 101_single_component.csv 
|           |--- __init__.py
|           |--- funeral.py
|           |--- main.py
|           |--- personal_info.py
|           |--- relations.py
|           |--- single_comp.py
|       |--- templates 
|               |--- index.html
|       |--- __init__.py
|       |--- routes.py 
|   |--- cbrobit.py
|--- LICENSE
|--- README.md
``` -->
