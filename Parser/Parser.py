# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 09:18:09 2026

@author: SPAC-B-2
"""


"""
to do :
    -make tests for convertDataToJSON
    -look into how to make better tests
    -maybe acount for lack of header
    -make test for divided up functions
"""


import unittest
import os



def retrieveFile(fileName):
    if os.path.exists(fileName):
        with open(fileName, "r") as f:
            text = f.read()
        print("The data file " + fileName +" has been retrieved")
    else:
        text = ""
        print("ERROR: The data file " + fileName + " does not exist.")
    return text
        

def convertData(text):   
    dictionaries = []

    rows = text.split("\n")
    headers = rows[0].split(",")
    for row in rows[1:]:
        if  row: #Ignores empty lines(Last line can be empty)
            dictOfRow = {}
            rowElements = row.split(",")
            for i in range(len(headers)):
                if rowElements[i].isdigit():
                    dictOfRow[headers[i]] = int(rowElements[i])
                elif rowElements[i].replace(".", "").isnumeric():
                    dictOfRow[headers[i]] = float(rowElements[i])
                else:
                    dictOfRow[headers[i]] = rowElements[i]
                
            dictionaries.append(dictOfRow)
    return dictionaries, headers


def retrieveData(fileName):
    text = retrieveFile(fileName)            
    if text:
        data = convertData(text)
    else:
        data = text, text
    return data


def convertDataToJSON(data, keys):
    #Start string and adds header
    stringData = "[["
    for k in keys:
        stringData += "\"" + k + "\", "
    stringData = stringData[:-2]
    stringData += "],\n"
    
    #Adds rest og elements
    for d in data:
        stringData += "["
        for k in keys:
            if type(d[k]) == int or type(d[k]) == float:
                stringData += str(d[k]) + ", "
            else:
                stringData += "\"" + d[k] + "\", "
        stringData = stringData[:-2]
        stringData += "],\n"
    stringData = stringData[:-2]
    stringData += "]"

    return stringData


def writeToFile(text,fileNameNew):
    with open(fileNameNew, "w", encoding="utf-8") as f:
        f.write(text)
        
        
test, head = retrieveData("employees.ascii.csv")
#test, head = retrieveData("sogne.dawa.csv")
testConversion = convertDataToJSON(test, head)
newFileName = "test_JSON_file.json"
writeToFile(testConversion, newFileName)

 
class testImport(unittest.TestCase):
    def test_file_exists_true(self):
        text = retrieveFile("sogne.dawa.csv")
        self.assertTrue(text)
        
    def test_file_exists_false(self):
        text = retrieveFile("sogned.dawa.csv")
        self.assertFalse(text)
        

class test_of_conversion(unittest.TestCase):
    test, head = retrieveData("employees.ascii.csv")
    test2, head2 = retrieveData("sogne.dawa.csv")
    
    #test if imporing file works
    def test_of_import(self):
        self.assertEqual(self.test[11]["role"], "VP of Marketing")
        
    #test if indexes work
    
    #test if array is of expected size
    def test_of_size1(self):
        self.assertEqual(len(self.test), 30)
    def test_of_size2(self):
        self.assertEqual(len(self.head), 7)
    #test datatype of numbers
    
    #test if other csv file also works
    def test_of_import2(self):
        self.assertEqual(self.test2[100]["geo_version"], 5)


class test_of_toJSON(unittest.TestCase):
    def test_is_string(self):
        self.assertTrue(type(testConversion) == str)
        
    def test_new_file_exists(self):
        self.assertTrue(os.path.exists(newFileName))

    def test_contains_all_headers(self):
        containsHeads = True
        for i in head:
            if "\"" + i + "\"" not in testConversion:
                containsHeads = False
        self.assertTrue(containsHeads)
        
    def test_contains_all_headers_false(self):
        head_false = head.copy()
        head_false[0] = "False head element"
        containsHeads = True
        for i in head_false:
            if i not in testConversion:
                containsHeads = False
        self.assertFalse(containsHeads)
        
    def test_contains_all_values(self):
        containsHeads = True
        for i in range(len(test)):
            for j in head:
                if type(test[i][j]) == int or type(test[i][j]) == float:
                    if str(test[i][j]) not in testConversion:
                        print(test[i][j])
                        containsHeads = False
                else:
                    if "\"" + test[i][j] + "\"" not in testConversion:
                        print(test[i][j])
                        containsHeads = False
        self.assertTrue(containsHeads)
if __name__ == "__main__":
    unittest.main()





