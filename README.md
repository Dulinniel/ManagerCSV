# CSVManager
Just a random package to deal with csv file.

## Usage

**__Read a file__**:

```py
from CSVManager import CSV_manager

csv_file = CSV_manager("/path/to/your/file")

for values in csv_file.read_csv():
  print(value)
```

Since the `read_csv` method, return a generator of lists, you must iterate over it to read the file content.

**__Write a file__**:

```py
from CSVManager import CSV_manager

csv_file = CSV_manager("/path/to/your/file")

datas: list[list[any]] = [ [ "Name", "First name", "Birth Year" ], [ "Turing", "Alan", 1912 ], [ "Lovelace", "Ada", 1815 ], [ "Shanon", "Claude", 1916 ], [ "Truong", "André", 1936 ] ]

csv_file.write_csv(datas)
```

To write into a file you have to provide a 2-dimensional array, Each Subarray in the main array represents columns and the data present in them, will be displayed on rows.
In this case, the csv file, will looks like this

![view of a csv file](https://github.com/Dulinniel/RandomCSVManager/blob/main/github/ressources/csv_file_preview.png)
