import json

py_obj = {
    "Name":"Ali Hasan",
    "Age" : 20,
    "is_boy" : True
}

# write json file

# with open("json_file.json","w") as f:
#     json.dump(py_obj,f,indent=4)

py_list = []

dict_obj = {
    "Name":"Ali Hasan",
    "Age" : 20,
    "is_boy" : True,
    "Hobbies" : ["Coding","Gaming","Cooking"],
    "marks" : {
        "Maths" : 90,
        "Physics" : 85,
        "Chemistry" : 80
    },
    "is_pass" : True
}

# read json file and update json file

with open("json_file.json","r") as f:
    data = json.load(f)
    py_list.extend(data)
    py_list.append(dict_obj)



# with open("json_file.json","w") as f:
#     json.dump(py_list,f,indent=4)

# json.dumps() use to convert python object to json string and return json string
js_str = json.dumps(py_obj)
print(js_str)
print(type(js_str))

# json.loads() use to convert json string to python object and return python object
py_data = json.loads(js_str)
print(py_data)
print(type(py_data))