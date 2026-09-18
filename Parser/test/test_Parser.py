# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 09:50:58 2026

@author: SPAC-B-2
"""

import os
import unittest
import ParserCode.Parser as Parser



class testImport(unittest.TestCase):
    def test_file_exists_true(self):
        text = Parser.retrieveFile("sogne.dawa.csv")
        self.assertTrue(text)
        
    def test_file_exists_false(self):
        text = Parser.retrieveFile("../sogned.dawa.csv")
        self.assertFalse(text)
        

class test_of_conversion(unittest.TestCase):
    test, head = Parser.retrieveData("employees.ascii.csv")
    test2, head2 = Parser.retrieveData("sogne.dawa.csv")
    
    def test_of_import(self):
        self.assertEqual(self.test[11]["role"], "VP of Marketing")
        
    def test_of_size1(self):
        self.assertEqual(len(self.test), 30)
    def test_of_size2(self):
        self.assertEqual(len(self.head), 7)

    def test_of_import2(self):
        self.assertEqual(self.test2[100]["geo_version"], 5)


class test_of_toJSON(unittest.TestCase):
    fileName = "employees.ascii.csv"
    test, head = Parser.retrieveData(fileName)
    testConversion = Parser.convertDataToJSON(test, head)
    newFileName = fileName[:-3]+"json"
    Parser.writeToFile(testConversion, newFileName)
    
    def test_is_string(self):
        self.assertTrue(type(self.testConversion) == str)
        
    def test_new_file_exists(self):
        self.assertTrue(os.path.exists(self.newFileName))
        
    def test_new_file_has_text(self):
        text = Parser.retrieveFile(self.newFileName)
        self.assertTrue(text)

    def test_contains_all_headers(self):
        containsHeads = True
        for i in self.head:
            if "\"" + i + "\"" not in self.testConversion:
                containsHeads = False
        self.assertTrue(containsHeads)
        
    def test_contains_all_headers_false(self):
        head_false = self.head.copy()
        head_false[0] = "False head element"
        containsHeads = True
        for i in head_false:
            if i not in self.testConversion:
                containsHeads = False
        self.assertFalse(containsHeads)
        
    def test_contains_all_values(self):
        containsHeads = True
        for i in range(len(self.test)):
            for j in self.head:
                if type(self.test[i][j]) == int or type(self.test[i][j]) == float:
                    if str(self.test[i][j]) not in self.testConversion:
                        print(self.test[i][j])
                        containsHeads = False
                else:
                    if "\"" + self.test[i][j] + "\"" not in self.testConversion:
                        print(self.test[i][j])
                        containsHeads = False
        self.assertTrue(containsHeads)
        

