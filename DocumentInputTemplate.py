#Using main modules python-docx and tkinter

import docx
import random
import sys
import os
import matplotlib
import collections
import string
from tkinter import *


#create document
reportdoc = docx.Document()

#create base window
root = Tk()
root.geometry("500x500")
root.title("Document Generator")

#in-window title
heading = Label(root, text="Create a Document Template", font=("Times New Roman", 20, "bold"))
heading.pack(side=TOP)

#Form fields
entryName = Entry(root, width=35, bg="lightgray")
entryName.pack()
entryName.place(x=35, y=80)
requestName = entryName.get()

#write name with text cocatenated to doc
firstParagraph = reportdoc.add_paragraph("This person's name is " + requestName + ".")

thingLike = Entry(root, width=35, bg="lightgray")
thingLike.pack()
thingLike.place(x=35, y=100)
personLikes = thingLike.get()

#continue on line
firstParagraph.add_run("They like " + personLikes + ".")

#Name the document
docName = Entry(root, width=35, bg="lightgray")
docName.pack()
docName.place(x=35, y=80)
documentname = docName.get()

#submit button
def submitButtonFunction():
	reportdoc.save(documentname + ".docx")

submitButton = Button(root, text="Submit", command=submitButtonFunction())
submitButton.pack()
submitButton.place(x=35, y=120)

#main
root.mainloop()
