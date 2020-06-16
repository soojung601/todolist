from flask import Flask, render_template,request, redirect, url_for
import sqlite3
from user_table import make_table, make_list, del_list, get_list, reset_list


app=Flask('todolist')

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/username')
def set_user():
    global username
    username=request.args.get('username').title()
    make_table(username)
    
    userlist=get_list(username)
    
    return render_template("personal.html", username=username, userlist = userlist)

@app.route('/username', methods=['POST'])
def add_list():    
    addedtext = request.form['addedtext']
    make_list(username,addedtext)
    userlist=get_list(username)
    return render_template("personal.html", username=username, userlist = userlist)
 
@app.route('/delete/<list_text>')
def dele_list(list_text):
    del_list(username, list_text)
    userlist=get_list(username)
    return render_template("personal.html", username=username, userlist = userlist)
    
@app.route('/delete_all')
def dele_all():
    reset_list(username)
    userlist=get_list(username)
    return render_template("personal.html", username=username, userlist = userlist)

app.run()