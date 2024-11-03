import os
from grep import GrepFile
class Sort:
    def __init__(self, filepath):
        self.filepath = filepath
    def sortFiles(self):
        with open(self.filepath) as fo:
            Sort = "Sort"
            grepfile = GrepFile("Script.txt")
            grep = grepfile.grepLine(Sort)
            line = fo.readlines()
            for lines in line:
                if grep == lines:  # Ensure to strip any leading/trailing whitespace
                    splitted = grep.split("\"")
                    source = splitted[1]
                    criteria = splitted[3]
                    print(source)
                    print(criteria)
                    break
            else:
                print("Sort directive not found in file.")
                return False
        files = os.listdir(source)
        # Sort based on criteria
        if criteria == "name":
            sorted_files = sorted(files)
        elif criteria == "date":
            sorted_files = sorted(files, key=lambda f: os.path.getmtime(os.path.join(source, f)))
        elif criteria == "size":
            sorted_files = sorted(files, key=lambda f: os.path.getsize(os.path.join(source, f)))
        else:
            print(f"Invalid sorting criteria: {criteria}")
            return False
        # Rename the files to reflect the sorted order
        # for index, filename in enumerate(sorted_files):
        #     old_path = os.path.join(source, filename)
        #     new_filename = f"{index:03d}_{filename}"
        #     new_path = os.path.join(source, new_filename)
        #     os.rename(old_path, new_path)
        #     sorted_files[index] = new_filename
        # Write the sorted filenames to a text file
        sorted_file_path = os.path.join(source, 'sortedFiles.txt')
        with open(sorted_file_path, 'w') as sorted_file:
            sorted_file.write('\n'.join(sorted_files))
        print(f"Files have been sorted by '{criteria}' and renamed successfully. Sorted file list written to {sorted_file_path}:")
        for file in sorted_files:
            print(file)
        return True