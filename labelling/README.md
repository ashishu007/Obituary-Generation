## Data Labelling
- This folder contains the code/instructions for data annotation for developing case-base.

## Process
- First use `doccano` to manually label the data and download it in `.jsonl (json lines)` format.
- Then use `...` script to convert `.jsonl` into `.xml`.
- Finally use `...` script to convert `.xml` into `.csv`.

## CSV File
- The `csv` file is the tabular representation of annotated data.
- Each row represent a `case` in the `case-base`.
- Each column is a `feature` used to represent the cases.
- After generating the `csv` file save it to `./app/messages/data` folder.