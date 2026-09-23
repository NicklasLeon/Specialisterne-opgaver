# Specialisterne Parser

This program is used to convert a .csv file to a .json formated file. 

## Description

This is a coding project to make a simple parser for converting a .csv file to a .json file. this is done using a couple of functions. 
It is currently assumed that the csv file has a header.

retrieveFile: Takes a file name and retrieves the file data if the file exists.

convertData: Converts the file from a string to list of dictionary entries with the header elements as keys.

convertDataToJSON: Converts the new format into a new string based on the .json file format.

writeToFile: Last step simply writes the file using the original name with .json.

## Getting Started

### Dependencies

The program is made to run on Python 3.13.
The only library for running the program is the os module.
The library unittest was used in the test_Parser.py file to run unit tests.


### Executing program

To run the code, execute the pyton file Parser.py
```
python ../Parser/ParserCode/Parser.py
```

When the code is run it ask for an input file. if the file is placed in the same folder as the code, this would simply be

```
name_of_folder/name_of_file.csv
```

If the program can't find the file, it will return an error message and ask for a new file name.
If the program can find the file, it will load the file as a text string. 


The .json file is placed in the same folder as the original .csv file. 

To quit the program simply input "q".


## Authors

Nicklas Leon Knudsen
