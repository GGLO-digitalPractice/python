import os
path = "P:/Dynamo/Packages/Clockwork for Dynamo 2.x/dyf/"
list_of_files = []

for root, dirs, files in os.walk(path):
    for file in files:
        list_of_files.append(os.path.join(root,file))

def search_str(file_path, word, place):
    with open(file_path, 'r+') as file:
        #read all content of the file
        content = file.read()
        #check if sting present in file
        if word in content:
            print ('string exists in file')
            if place in content:
                print(place+'exists in file')
            else:
                print(place+'Does not exist in file')

for file in files:
    search_str(path,'"Code": "','"Engine": "CPython3",')

#for name in list_of_files:
#    print(name)