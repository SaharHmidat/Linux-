import os
import shutil
from grep import GrepFile
class Movefile:
    def __init__(self,filepath):
        self.filepath=  filepath

    def moveFile(self):
        with open(self.filepath) as fo:
            move="Mv_last"
            grepfile = GrepFile("Script.txt")
            grep=grepfile.grepLine(move)
            line = fo.readlines()
            for lines in line:
                if grep == lines:
                    splitted = grep.split("\"")
                    source = splitted[1]
                    destination = splitted[3]
                    print(source)
                    print(destination)
                    flag = os.path.exists(source)
                    flagTwo = os.path.exists(destination)
                    if flag != True:
                        print("Can't reach to this", source)
                        return False
                    if flagTwo != True:
                        print("Can't reach to this", destination)
                        return False
        destinationCheck = os.path.join(destination, os.path.basename(source))
        if os.path.exists(destinationCheck):
             print("OPs,File already exists at destination")
             return False
        else:
            shutil.move(source, destination)
            return True

