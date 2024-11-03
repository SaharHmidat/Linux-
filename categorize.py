import os
from grep import GrepFile
import shutil # to delete file from folder
import re
class Categorize:
    def __init__(self,filepath,Threshold_size):
        self.filepath=filepath
        self.Threshold_size=Threshold_size

    def categorizeFiles(self):
        ThresholdUpdate= self.convert_size_to_bytes(self.Threshold_size)
        with open(self.filepath) as fo:
            Categorize = "Categorize"
            grepfile = GrepFile("Script.txt")
            grep = grepfile.grepLine(Categorize)
            line = fo.readlines()

            for lines in line:         # split the line read
                if grep == lines:
                    splitted = lines.split("\"")
                    Directory = splitted[1]
        flag=os.path.exists(Directory)
        if flag != True:
            print("Can't reach to New Directory")
            return False
        smallerThanThreshold = os.path.join(Directory, 'SmallerThanThreshold')
        largerThanThreshold = os.path.join(Directory, 'LargerThanThreshold')

        # Create the new directories if they don't exist
        os.makedirs(smallerThanThreshold, exist_ok=True)
        os.makedirs(largerThanThreshold, exist_ok=True)

        # Iterate through the files in the directory
        for filename in os.listdir(Directory):
            file_path = os.path.join(Directory, filename)
            # Skip directories
            if os.path.isdir(file_path):
                continue
            file_size = os.path.getsize(file_path)
            if file_size < ThresholdUpdate:
                shutil.move(file_path, smallerThanThreshold)
            else:
                shutil.move(file_path, largerThanThreshold)

        print("Files have been categorized successfully.")
        return True

    def convert_size_to_bytes(self,Threshold_size):
        size_units = {"B": 1, "KB": 1000, "MB": 1000 ** 2, "GB": 1000 ** 3, "TB": 1000 ** 4}
        match = re.match(r'(\d+)([a-zA-Z]+)', Threshold_size)
        if not match:
            raise ValueError("Invalid size format")
        size_value, unit = match.groups()
        size_value = int(size_value)
        unit = unit.upper()

        if unit not in size_units:
            raise ValueError("Unsupported unit. Please use B, KB, MB, GB, or TB.")

        return size_value * size_units[unit]

