# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 09:18:09 2026

@author: SPAC-B-2
"""


import os #used to validate file existing



def retrieveFile(fileName):
    if os.path.exists(fileName):
        with open(fileName, "r") as f:
            text = f.read()
        print("The data file \"" + fileName +"\" has been retrieved")
    else:
        text = ""
        print("ERROR: The data file \"" + fileName + "\" does not exist.")
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
        data = text, ""
    return data


def convertDataToJSON(data, keys):
    #Start string and adds header
    stringData = "[["
    for k in keys:
        stringData += "\"" + k + "\", "
    stringData = stringData[:-2]
    stringData += "],\n"
    
    #Adds rest of elements
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
   
def writeConvertion(data, key, fileName):
    dataJson = convertDataToJSON(data, key)
    fileNameNew = fileName[:-3]+"json"
    writeToFile(dataJson, fileNameNew)
    print("File \"" + fileName + "\" has now been converted to json format")


def fileConvertion(fileName):
    if fileName[-4:] == ".csv":
        convertedData, headers = retrieveData(fileName)
        if convertedData:
            writeConvertion(convertedData, headers, fileName)
    else:
        print("file is not .csv")
    
def runner():
    while True:
        fileName = input("Input name of file for conversion \n")
        if fileName == "q" or not fileName:
            print("Quiting file conversion")
            break
        fileConvertion(fileName)
    return "runner ended"


if __name__ == "__main__":
    runner()
    
    
    

    
    
    