import re
class GrepFile:
    def __init__(self, filepath):
        self.filepath = filepath

    def grepLine(self, word):
        with open(self.filepath, 'r') as fo:
            for line in fo:
                if re.search(word, line):
                    grepWord = line
        return grepWord

