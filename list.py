import os
from grep import  GrepFile

class List:
    def __init__(self,filepath):
        self.filepath=filepath

    def listFiles(self):
        with open(self.filepath) as fo:
            move = "List"
            grepfile = GrepFile("Script.txt")
            grep = grepfile.grepLine(move)
            line = fo.readlines()
            for lines in line:
                if grep == lines:
                    splitted = grep.split("\"")

        for file in os.listdir(splitted[1]):
            print(file)
        return True
