#Writing files (.txt, .json, .csv)
#a will write everytime we run the code, w will overwrite the file, x will not overwrite, r for reading

file_path="output.txt"
try:
    with open(file_path,"r") as file:
        content=file.read()
        print(content)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have the permission to read that file")


import json
file_path_json="new_file.json"
try:
    with open(file_path_json,"r") as file:
        content=json.load(file)
        print(content)
        print(content["name"])
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have the permission to read that file")


import csv
file_path_csv="csv_file.csv"
try:
    with open(file_path_csv,"r") as file:
        content=csv.reader(file)
        print(content)                      #print memory address
        for line in content:
            print(line[0])
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have the permission to read that file")
