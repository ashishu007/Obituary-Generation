## Data Labelling
- This folder contains the code/instructions for data annotation for developing case-base.

## Process
- First use `doccano` to manually label the data and download it in `.jsonl (json lines)` format.
    - `doccano` is found [here](https://github.com/doccano/doccano).
- Then use `create_xml.py` script to convert `.jsonl` into `.xml`.
- Finally use `create_csv.py` script to convert `.xml` into `.csv`.

## CSV File
- The `csv` file is the tabular representation of annotated data.
- Each row represent a `case` in the `case-base`.
- Each column is a `feature` used to represent the cases.
- After generating the `csv` file save it to `./app/messages/data` folder.

## Important
- Right now the automated conversion of `jsonl` to `xml` is only possible for `basic-retrieval` method.
- I am trying to develop an automated way for the conversion for `component-retrieval` as well.
- The only challenging task there is to segregating different sentences.
- Right now, file conversion for `component-retrieval` can be done in a semi-automated way by following these steps:
    - Manually label each obituary to identify different components.
    - The three extra tags should be: `personal_info_component`, `relations_component` and `funeral_component`.
        - See: `xml-tagged-comps.xml`
    - Run the `create_csv_comps.py` script.
    - Three new `csv` files will be generated in the `data` folder.