import json
import argparse
import os

def generateFile(data):
    path = os.path.abspath(os.getcwd())
    file_name = 'output.cpp'
    f = open(path+file_name, 'w')
    with open('template.cpp','r',encoding='utf-8') as file:
        edit = file.readlines()

    edit = edit[:15]
    for i in data:
        for j in data[i]:
            edit.append('''initDataItem("{}", {}, "{}", {});\n'''.format(j['name'],j['tag'],j['type'],j['size'])) 

    edit.append("}\nvoid DeviceAB::initCollections()\n{\nstd::shared_ptr<Iolink> Colection = Iolink::getInstance();\n")

    for x in data: 
        for y in data[x]:
            edit.append('''Colection.{}->push("{}");\n'''.format(x,y['name'])) 
    
    edit.append("}")
  
    with open('output.cpp', 'w', encoding='utf-8') as file:
       file.writelines(edit)
 

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', nargs=1,
                        help="JSON file to be processed",
                        type=argparse.FileType('r'))

    arguments = parser.parse_args()
    data = json.load(arguments.file[0])
    generateFile(data)