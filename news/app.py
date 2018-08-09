#!/usr/bin/python3
import os, json
from flask import Flask, render_template

app = Flask(__name__)

# 获取文件
def get_file(src):
    files = []
    for file_name in os.listdir(src):
        print(file_name)
        file = os.path.join(src, file_name)
        files.append(file)
    return files

# json序列化获取数据
def get_data(json_file):
    with open(json_file) as f:
        data = json.load(f)
    return data

# 取出title内容
def title_get(data):
    return data.get('title')


@app.route('/')
def index():
    datas = []
    src = '/home/shiyanlou/files'
    files = get_file(src)
    
    for f in files:
        data = get_data(f)
        datas.append(data)
    return render_template('index.html', datas = datas)

@app.route('/files/<filename>')
def file(filename):
    src = '/home/shiyanlou/files'
    file_src = os.path.join(src, filename+'.json')    
#    data = get_data(file_src)
    if os.path.exists(file_src) == True:
        data = get_data(file_src)
        return render_template('file.html', data = data)
    else:
        return render_template('404.html', error='shiyanlou 404')

@app.errorhandler(404)
def nor_found(error):
    return render_template('404.html', error='shiyanlou 404')

