import os
from grep import GrepFile
class Delete:
    def __init__(self,filepath):
        self.filepath=filepath

    def deleteFiles(self):
        with open(self.filepath) as fo:
            move = "Delete"
            grepfile = GrepFile("Script.txt")
            grep = grepfile.grepLine(move)
            line = fo.readlines()
            for lines in line:
                if grep == lines:
                    splitted = lines.split("\"")
                    source = splitted[1]
                    destination = splitted[3]
        flag=os.path.exists(destination)
        flagTwo=os.path.isfile(source)
        if flag != True:
            print("Can't reach to this", destination)
        if flagTwo != True:
            print("Can't reach to this", source)
        try:
            os.remove(source)
        except OSError :
             print("You can't delete this")
        else:
            print("Delete successful")
            return True

