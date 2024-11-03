import os
from grep import GrepFile
class Rename:
    def __init__(self,filepath):
        self.filepath=filepath
    def renameFiles(self):
        with open(self.filepath) as fo:
            move = "Rename"
            grepfile = GrepFile("Script.txt")
            grep = grepfile.grepLine(move)
            line = fo.readlines()
            for lines in line:
                if grep == lines:
                    splitted = lines.split("\"")
                    oldName = splitted[1]
                    newName = splitted[3]
                    destination=splitted[5]
        flag=os.path.exists(destination)
        flagTwo = os.path.isfile(oldName)
        if flag != True:
            print("Can't reach to New Directory")
            return False
        if flagTwo != True:
            print("Can't reach to Old File")
            return False
        try:
            os.rename(oldName,newName)
        except OSError :
             print("You can't rename this")
        else:
            print("Rename successful")
            return True

