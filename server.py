# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 05:32:20 2019

@author: kritika ahuja
"""

from flask import Flask
from flask import render_template
from flaskext.mysql import MySQL
import os
from flask import  request
import pickle
import plotly.graph_objects as go
from flask import redirect, url_for
app = Flask(__name__)
app.config.from_object('config')
@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'local_health' and request.form['password'] == 'admin':
            return render_template('forms.html')
        elif request.form['username'] == 'state_health' and request.form['password'] == 'admin':
            return render_template('data.html')
        elif request.form['username'] == 'national_health' and request.form['password'] == 'admin':
            return render_template('data.html')
        else:
            error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', error=error)
@app.route('/hello', methods=['POST'])
def hello():
    totdeath = request.form['totdeath']
    file1='totdeath1'
    tot=open(file1,'wb')
    pickle.dump(totdeath,tot)
    tot.close()
    d1 = request.form['D1']
    file2='D11'
    D1=open(file2,'wb')
    pickle.dump(d1,D1)
    D1.close()
    d2 = request.form['D2']
    file3='D22'
    D2=open(file3,'wb')
    pickle.dump(d2,D2)
    D2.close()
    d3 = request.form['D3']
    file4='D33'
    D3=open(file4,'wb')
    pickle.dump(d3,D3)
    D3.close()
    d4 = request.form['D4']
    file5='D44'
    D4=open(file5,'wb')
    pickle.dump(d4,D4)
    D4.close()
    d5 = request.form['D5']
    file6='D55'
    D5=open(file6,'wb')
    pickle.dump(d5,D5)
    D5.close()
    d6 = request.form['D6']
    file7='D66'
    D6=open(file7,'wb')
    pickle.dump(d6,D6)
    D6.close()
    d7 = request.form['D7']
    file8='D77'
    D7=open(file8,'wb')
    pickle.dump(d7,D7)
    D7.close()
    d8 = request.form['city']
    file9='D88'
    D8=open(file9,'wb')
    pickle.dump(d8,D8)
    D8.close()   
    infile = open('D11','rb')
    v1 = pickle.load(infile)
    infile = open('D22','rb')
    v2 = pickle.load(infile)
    infile = open('D33','rb')
    v3 = pickle.load(infile)
    infile = open('D44','rb')
    v4 = pickle.load(infile)
    infile = open('D55','rb')
    v5 = pickle.load(infile)
    infile = open('D66','rb')
    v6 = pickle.load(infile)
    infile = open('D77','rb')
    v7 = pickle.load(infile)
    infile = open('D88','rb')
    v8 = pickle.load(infile)
    path='C:\\Users\\kritika ahuja\\Desktop\\deploy\\static\\'
    colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen','lightblue','red']
    labels = ['Pneumonia','Prematurity','Low birth weight','Dirrhoeal disease','Neontal infection','Birth Asphyxia & Birth Trauma','Other Disease']
    values = [55+int(v1), 98+int(v2), 23+int(v3), 64+int(v4),78+int(v5),55+int(v6),10+int(v7)]
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                      marker=dict(colors=colors, line=dict(color='#000000', width=2)))
    fig.write_image(path+str(v8)+"_DIS.jpeg")


    colors = ['lightblue', 'lightgreen','red']
    labels = ['1-5 Year','29 Days - 1 Year','<28 days']
    values = [99,18,65]
    
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                      marker=dict(colors=colors, line=dict(color='#000000', width=2)))
    fig.write_image(path+str(v8)+"_DIS_Age.jpeg")
                                                           

    districts=['Patiala', 'Ludhiana', 'Bhatinda','Amritsar','Chandigarh']
    fig = go.Figure([go.Bar(x=districts, y=[19,58,47,98,189])])
    
    fig.write_image("Death.jpeg")
    return 'Your data has been recorded :) <br/> <a href="/data">Back Home</a>'

@app.route("/index")
def index():
    return render_template('index.html')
@app.route("/data")
def data():
    return render_template('data.html')
@app.route("/facts")
def facts():
    return render_template('facts.html')
@app.route("/health")
def health():
    return render_template('healthCenters.html')
@app.route("/contact")
def contact():
    return render_template('contacts.html')
@app.route("/about")
def about():
    return render_template('about.html')
@app.route("/pmap")
def pmap():
    return render_template('patiala_map.html')
@app.route("/cmap")
def cmap():
    return render_template('chandigarh_map.html')
@app.route("/lmap")
def lmap():
    return render_template('ludhiana_map.html')
@app.route("/jmap")
def jmap():
    return render_template('jalandhar_map.html')
@app.route("/amap")
def amap():
    return render_template('amritsar_map.html')
@app.route("/cpcs")
def cpcs():
    return render_template('chandigarhpics.html')
@app.route("/ppcs")
def ppcs():
    return render_template('patialapics.html')
@app.route("/lpcs")
def lpcs():
    return render_template('ludhianapics.html')
@app.route("/apcs")
def apcs():
    return render_template('amritsarpics.html')
@app.route("/jpcs")
def jpcs():
    return render_template('jalandharpics.html')
if __name__ == "__main__":
    app.run(debug=True)