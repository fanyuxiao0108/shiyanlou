#!/usr/bin/python3
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/shiyanlou'
db = SQLAlchemy(app)

class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    category = db.relationship('Category',backref=db.backref('files',lazy='dynamic'))
    content = db.Column(db.Text)

    def __init__(self,title,created_time,category,content):
        self.title = title
        self.created_time = created_time
        self.category = category
        self.content = content

    def __repr__(self):
        return '<File %r>' % self.title

class Category(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name

def insert_data():
    db.create_all()
    java = Category('Java')
    python = Category('Python')
    file1 = File('Hello Java', datetime.utcnow(), java, 'File Content - Java is cool')
    file2 = File('Hello Python', datetime.utcnow(), python, 'File Content - Python is cool')
    db.session.add(java)
    db.session.add(python)
    db.session.add(file1)
    db.session.add(file2)
    db.session.commit()

@app.route('/')
def index():
    insert_data()
    return render_template('index.html', files = File.query.all())



@app.route('/files/<file_id>')
def file(file_id):
    insert_data()
    file_item = File.query.get_or_404(file_id)
    return render_template('file.html', file_item = file_item)


@app.errorhandler(404)
def nor_found(error):
    return render_template('404.html', error='shiyanlou 404')

if __name__ == '__main__':
    insert_data()
