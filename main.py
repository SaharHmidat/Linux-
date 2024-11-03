import csv
import json
import os
import logging
from mov import Movefile
from list import List
from count import  Count
from Delete import Delete
from rename import  Rename
from categorize import  Categorize
from sort import Sort
jsonfile="C:/Users/HP/pythonProject/linuxProject/data/data/data/config.json"
filepath2="C:/Users/HP/pythonProject/linuxProject"
filepath="Script.txt"
with open(jsonfile) as fp: # to read the data in json
    listObj = json.load(fp)
Threshold=listObj['Threshold_size']
Maxcommands=listObj['Max_commands']
Maxlogfiles=listObj['Max_log_files']
sameDir=listObj['Same_dir']
MaxCom=1
count = 1
# elif word[i]=="Sort":
#     flagMove = moveFile(filepath)
def write_to_csv(line):
    with open('output.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([line])

def log_to_file(message, number, passed):
    if passed:
        log_dir = "PASSED"
    else:
        log_dir= "FAILED"
    if sameDir:
        log_filename = os.path.join("C:/Users/HP/pythonProject/linuxProject/data/data/data", f"{log_dir}{number}.log")
        logging.basicConfig(filename="output.log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info(message)
    else:
        log_filename = os.path.join("C:/Users/HP/pythonProject/linuxProject/data/data", f"{log_dir}{number}.log")
        logging.basicConfig(filename="output.log", level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info(message)
    if not os.path.exists(log_filename):
        with open(log_filename, 'w') as f:
            f.write('')

csv_count = 1
log_number = 1
with open(filepath) as fo:
    line = fo.readlines()
if listObj['Output'] == "csv":
    for lines in line:
        i = 0
        liness = lines.split(" <")
        word = liness
        if word[i] == "Rename":
            flagrename = Rename(filepath)
            flagRename = flagrename.renameFiles()
            if Maxcommands >= MaxCom:
                if flagRename  :
                    write_to_csv(f"line-{csv_count}, True(RENAME)")
                else:
                    write_to_csv(f"line-{csv_count}, False(RENAME)")
                csv_count += 1
                MaxCom = MaxCom + 1
        elif word[i] == "Count":
            flagcount = Count(filepath)
            flagCount = flagcount.countFiles()
            if Maxcommands >= MaxCom:
                if flagCount:
                    write_to_csv(f"line-{csv_count}, True(COUNT)")
                else:
                    write_to_csv(f"line-{csv_count}, False(COUNT)")
                csv_count += 1
                MaxCom = MaxCom + 1
        elif word[i] == "List":
             flaglist=List(filepath)
             flagList = flaglist.listFiles()
             if Maxcommands >= MaxCom:
                if flagList:
                    write_to_csv(f"line-{csv_count}, True(LIST)")
                else:
                     write_to_csv(f"line-{csv_count}, False(LIST)")
                csv_count += 1
                MaxCom = MaxCom + 1

        elif word[i] == "Mv_last":
            flagMove = Movefile(filepath)
            flagmove=flagMove.moveFile()
            if Maxcommands >= MaxCom:
                if flagmove:
                    write_to_csv(f"line-{csv_count}, True(MOVE)")
                else:
                    write_to_csv(f"line-{csv_count}, False(MOVE)")
                csv_count += 1
                MaxCom = MaxCom + 1
        elif word[i] == "Delete":
            flagdelete = Delete(filepath)
            flagDelete = flagdelete.deleteFiles()
            if Maxcommands >= MaxCom:
                if flagDelete:
                    write_to_csv(f"line-{csv_count}, True(DELETE)")
                else:
                     write_to_csv(f"line-{csv_count}, False(DELETE)")
                csv_count += 1
                MaxCom = MaxCom + 1
        elif word[i] == "Delete":
            flagcategorize = Categorize(filepath,Threshold)
            flagCategorize = flagcategorize.categorizeFiles()
            if Maxcommands >= MaxCom:
                if flagCategorize:
                    write_to_csv(f"line-{csv_count}, True(Categorize)")
                else:
                    write_to_csv(f"line-{csv_count}, False(Categorize)")
                csv_count += 1
                MaxCom = MaxCom + 1
        elif word[i] == "Sort":
            flagsort= Sort(filepath)
            flagSort = flagsort.sortFiles()
            if Maxcommands >= MaxCom:
                if flagSort:
                    write_to_csv(f"line-{csv_count}, True(Sort)")
                else:
                    write_to_csv(f"line-{csv_count}, False(Sort)")
                csv_count += 1
                MaxCom = MaxCom + 1

with open(filepath) as fo:
    line = fo.readlines()
if listObj['Output'] == "log":
    for lines in line:
        i = 0
        liness = lines.split(" <")
        word = liness
        if word[i] == "Rename":
            if log_number <= Maxlogfiles:
                flagrename = Rename(filepath)
                flagRename = flagrename.renameFiles()
                if flagRename:
                    log_to_file(f"line-{count}, True(RENAME)", log_number,True)
                else:
                    log_to_file(f"line-{count}, False(RENAME)", log_number,False)
                log_number =log_number+ 1
                count += 1
        elif word[i] == "Count":
            if log_number <= Maxlogfiles:
                flagcount = Count(filepath)
                flagCount = flagcount.countFiles()
                if flagCount:
                    log_to_file(f"line-{count}, True(COUNT)", log_number,True)
                else:
                    log_to_file(f"line-{count}, False(COUNT)", log_number,False)
                log_number =log_number+ 1
                count =count+1
        elif word[i] == "List":
            if log_number <= Maxlogfiles:
                flaglist = List(filepath)
                flagList = flaglist.listFiles()
                if flagList:
                    log_to_file(f"line-{count}, True(LIST)", log_number,True)
                else:
                    log_to_file(f"line-{count}, False(LIST)", log_number,False)
                log_number =log_number+ 1
                count =count+1
        elif word[i] == "Mv_last":
            if log_number <= Maxlogfiles:
                flagMove = Movefile(filepath)
                flagmove = flagMove.moveFile()
                if flagmove:
                    log_to_file(f"line-{count}, True(MOVE)", log_number,True)
                else:
                    log_to_file(f"line-{count}, False(MOVE)", log_number,False)
                log_number =log_number+ 1
                count =count+1
        elif word[i] == "Delete":
            if log_number <= Maxlogfiles:
                flagdelete = Delete(filepath)
                flagDelete = flagdelete.deleteFiles()
                if flagDelete:
                    log_to_file(f"line-{count}, True(DELETE)", log_number,True)
                else:
                    log_to_file(f"line-{count}, False(DELETE)", log_number,False)
                log_number=log_number+ 1
                count =count+1
        elif word[i] == "Categorize":
            if log_number <= Maxlogfiles:
                flagcategorize = Categorize(filepath, Threshold)
                flagCategorize = flagcategorize.categorizeFiles()
                if flagCategorize:
                    log_to_file(f"line-{count}, True(Categorize)", log_number,True)
                else:
                    log_to_file(f"line-{count}, False(Categorize)", log_number,False)
                log_number =log_number+ 1
                count =count+1
        elif word[i] == "Sort":
            if log_number <= Maxlogfiles:
                flagsort = Sort(filepath)
                flagSort = flagsort.sortFiles()
                if flagSort:
                    log_to_file(f"line-{count}, True(Sort)", log_number, True)
                else:
                    log_to_file(f"line-{count}, False(Sort)", log_number, False)
                log_number = log_number + 1
                count = count + 1


