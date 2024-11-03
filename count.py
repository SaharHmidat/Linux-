import os
from grep import  GrepFile
class Count:
    def __init__(self,filepath):
        self.filepath=filepath
    def countFiles(self):
        with open(self.filepath) as fo:
            count = 0
            move = "Count"
            grepfile = GrepFile("Script.txt")
            grep = grepfile.grepLine(move)
            line = fo.readlines()
            for lines in line:
                if grep == lines:
                    splitted = lines.split("\"")
                    pathList=splitted[1]
            flag = os.path.exists(pathList)
            if flag != True:
                return False
            else:
                for file in os.listdir(pathList):
                    count=count + 1
                print(count)
                filePrint = open("FileCount.txt", "w")
                filePrint.write(str(count))
                filePrint.close()
        return True