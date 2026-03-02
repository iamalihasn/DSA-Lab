import pickle

py_dict_obj = {
    "Name":"Ali Hasan",
    "Age" : 20,
    "is_boy" : True
}

num_list = [x for x in range(1,11)]

# dump() use to save python objrct in other file

# if i store data in bin file
# with open("sample.bin","wb") as f:
#     pickle.dump(py_dict_obj,f)
#     pickle.dump(num_list,f)

# Read bin file use pickle mod

# load() use to read json and pickle file

with open("sample.bin","rb") as f :
    while True:
        try:
            data = pickle.load(f)
            print(data)

        except EOFError:
            break

# dumps() use to convert python object and return bynary litral in pickle module and return a string in json module

pic_num = pickle.dumps(num_list)
print(pic_num)

# loads() also convert binary data and json data to python object
py_num = pickle.loads(pic_num)
print(py_num)