## Directory Tree
```
.
+-- cbrservice (main flask directory)
|   +-- app (flask sevice)
|   |   +-- messages (CBR/Lazy learning part)
|   |   |   +-- data (Case-Base)
|   |   |   |   +-- 101_funeral_component.csv 
|   |   |   |   +-- 101_personal_component.csv 
|   |   |   |   +-- 101_relations_component.csv 
|   |   |   |   +-- 101_single_component.csv 
|   |   |   +-- __init__.py
|   |   |   +-- funeral.py
|   |   |   +-- main.py
|   |   |   +-- personal_info.py
|   |   |   +-- relations.py
|   |   |   +-- single_comp.py
|   |   +-- templates (HTML templates)
|   |           +-- index.html
|   |   +-- __init__.py
|   |   +-- routes.py (flask routes)
|   +-- cbrobit.py (main flask file)
+-- LICENSE
+-- README.md
```
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

## Instructions to run
- Run on windows powershell
    - ```cd cbrservice```
    - ```$env:FLASK_ENV="development"```
    - ```$env:FLASK_APP="cbrobit.py"```
    - ```flask run```

## TODO
- Fix format for component features.
- 