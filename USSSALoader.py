#!/usr/bin/env python3.5
# encoding: utf-8

"""
    USSSALoader.py
"""

import os
from zipfile import ZipFile
from urllib import request

import pickle

pickle_file = 'name.pickle'
zip_file = 'names.zip'


def download_names():
    u = request.urlopen('https://github.com/downloads/sholiday/genderPredictor/names.zip')
    with open(zip_file, 'wb') as file:
        file.write(u.read())
    
    
def extract_names_dict():
    zf = ZipFile(zip_file, 'r')
    file_names = zf.namelist()
    names = dict()
    gender_map = {'M': 0, 'F': 1}
    for file_name in file_names:
        file = zf.open(file_name, 'r').read().decode('utf-8')
        infile = file.split('\n')
        rows = [row.strip().split(',') for row in infile if len(row) > 1]
        for row in rows:
            name = row[0].upper()
            gender = gender_map[row[1]]
            count = int(row[2])
            if name not in names:
                names[name] = [0,0]
            names[name][gender] = names[name][gender] + count
        print('Imported - {}'.format(file_name))
    return names
            
            
def get_name_list():
    if not os.path.exists(pickle_file):
        print('{} does not exist, generating'.format(pickle_file))
        
        if not os.path.exists(zip_file):
            print('{} does not exist, downloading from github')
            download_names()
        else:
            print('{} exists, not downloading'.format(zip_file))
            
        print('Extracting names from {}'.format(zip_file))
        names_dict = extract_names_dict()
        
        male_names = list()
        female_names = list()
        
        print('Sorting Names')
        for name in names_dict:
            counts = names_dict[name]
            data = (name, counts[0], counts[1])
            if counts[0] > counts[1]:
                male_names.append(data)
            elif counts[1] > counts[0]:
                female_names.append(data)
        
        names = (male_names, female_names)
        print('Saving {}'.format(pickle_file))
        fw = open(pickle_file, 'wb')
        pickle.dump(names, fw, -1)
        fw.close()
        print('Saved {}'.format(pickle_file))
    else:
        print('{} exists, loading data'.format(pickle_file))
        f = open(pickle_file, 'rb')
        names = pickle.load(f)
        print('{} loaded'.format(pickle_file))
            
    print('{} males names loaded, {} female loaded'.format(len(names[0]), len(names[1])))
    return names
    

if __name__ == "__main__":
    get_name_list()
