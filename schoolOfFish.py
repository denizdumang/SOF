# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 17:02:06 2023

@author: denizdu
"""

import xml.etree.ElementTree as ET
from tkinter import *
from tkinter import ttk

'''
class Fish:
    def __init__(self,arg):
        self.ID = arg

class Salmon(Fish):
    type = "S"

class Tuna(Fish):
    type = "T"

'''

class DataBase:
    __allowedTypes = {"S","T"}
    __allowedIndexes = list(range(64))
    
    def __init__(self,name):
        self.name = str(name)
        self.db = {}
        
    def dbUpdate(self):
        ID = getVal()
        if ID in self.__allowedIndexes:
            self.db[ID] = var.get()
        print(self.db)
    
    # @staticmethod
    def parseConfigXml(self):
        self.name = entry.get()
        dom = ET.parse(self.name + "List.xml")
        node = dom.getroot()
        for node in dom.iter(self.name):
            key = 0
            val = ""
            for element in node:
                if element.tag == "Index":
                    key = int(element.text)
                elif element.tag == "Type":
                    self.db[key] = element.tex
        print(self.db)
        return
    
    def saveConfigXml(self):
        body = ET.Element("List")
        tree = ET.ElementTree(body)
        for i in self.db:
            child = ET.Element(self.name)
            childIndex = ET.SubElement(child,"Index")
            childIndex.text = str(i)
            childType = ET.SubElement(child,"Type")
            childType.text = self.db[i]
            body.append(child)
        print(ET.tostring(body))
        with open(self.name + "List.xml","wb") as f:
            tree.write(f)
            
    def saveAsConfigXml(self):
        self.name = entry.get()
        self.saveConfigXml()
        
def getVal():
    text = entry.get()
    return int(text)

def donothing():
    filewin = TopLevel(root)
    button = Button(filewin,text="do nothing button")
    button.pack()

db = DataBase("dbTemp")
root = Tk()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open",command=db.parseConfigXml)
filemenu.add_command(label="Save",command=db.saveConfigXml)
filemenu.add_command(label="Save As...",command=db.saveAsConfigXml)
menubar.add_cascade(label="File",menu=filemenu)
viewmenu = Menu(menubar, tearoff=0)
viewmenu.add_command(label="Current..",command=donothing)
menubar.add_cascade(label="View",menu=viewmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About..",command=donothing)
menubar.add_cascade(label="Help",menu=helpmenu)
root.config(menu=menubar)

var = StringVar()
R1 = Radiobutton(root, text="Salmon", variable=var,value="S").pack(anchor=W)
R1 = Radiobutton(root, text="Tuna", variable=var,value="T").pack(anchor=W)
label = Label(root)
label.pack()
entry = ttk.Entry(root)
entry.pack()
addButton = Button(root, text="ADD", fg="green", command=db.dbUpdate).pack(side=BOTTOM)
root.mainloop()            
        
        