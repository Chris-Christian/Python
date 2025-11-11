#Writing files (.txt, .json, .csv)

txt_data="Hello, I'm Chris"
file_path="output.txt"
try:
    with open(file_path,"a") as file:           #a will write everytime we run the code, w will overwrite the file, x will not overwrite
        file.write(txt_data+"\n")
        print(f"txt file '{file_path}' was created")
except FileExistsError:
    print("That file already exists")


#List
employees=["Doraemon", "Nobita", "Gian", "Suneo"]
file_path_list="list.txt"
try:
    with open(file_path_list,"a") as file:
        for employee in employees:
            file.write(employee+" ")
        print(f"txt file '{file_path_list}' was created")
except FileExistsError:
    print("That file already exists")


#json
import json
character={
    "name":"Doraemon",
    "age":10
}
file_path_json="new_file.json"

try:
    with open(file_path_json,"w") as file:
        json.dump(character, file, indent=4)
        print(f"json file '{file_path_json}' was created")
except FileExistsError:
    print("That file already exists")


#csv (Comma separated values)
import csv
Students=[["Name","Age"],
         ["Chris",20],
         ["Saitama",25],
         ["Kira",23]]
file_path_csv="csv_file.csv"

try:
    with open(file_path_csv,"w",newline="") as file:
        writer=csv.writer(file)
        for row in Students:
            writer.writerow(row)
        print(f"csv file '{file_path_csv}' was created")
except FileExistsError:
    print("That file already exists")
