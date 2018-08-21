'''
filecrud.py
Idea is to create the CRUD utility functions for FILE.
call the methods based on what the user wants.
'''

import os

def createfile(directory, filename):
   if os.path.exists(os.path.join(directory, filename)):
       #appendfile(filename, True)
       return "File already exists, should open in append mode or delete first"
   else:
       try:
           samfile = open(os.path.join(directory, filename), 'w')
           return samfile
       # samfile.close() #file autoclose when the method exists
       except Exception as e:
           return str(e)


def readfile(directory, filename):
   if os.path.exists(os.path.join(directory, filename)):
       samfile = open(os.path.join(directory, filename), "r")
       contents = samfile.read()
       return contents
   else:
       return None


def appendfile(directory, filename, newtext='', returncontent=False):
    if os.path.exists(os.path.join(directory, filename)):
        samfile = open(os.path.join(directory, filename), "a+")
        samfile.write(newtext)
        if returncontent == True:
            contents = samfile.read()
            return contents
    else:
        return "File doesn't exists"


def deletefile(directory, filename):
   if os.path.exists(os.path.join(directory, filename)):
       try:
           os.remove(os.path.join(directory, filename))
           return "File Deleted"
       except Exception as e:
           return str(e)
   else:
       return "File does not exists"












