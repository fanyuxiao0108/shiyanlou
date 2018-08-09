#!/usr/bin/python
import os, json

path = '/home/shiyanlou/files'
files = os.listdir(path)
s = {}
for file in files:
    if not os.path.isdir(file):
        f = open(path + '/' + file)
        iter_f = iter(f)
        str = ''
        for line in iter_f:
            
                
        
