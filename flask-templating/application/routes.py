from flask import render_template
from application import app


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/name')
def name():
    return render_template('name.html')

@app.route('/name2')
def name2():
    namelist = ["ben", "harry", "bob", "jay", "matt", "bill", "morbo"]
    return render_template('name2.html', users=namelist)
    
@app.route('/ben')    
def ben():
    return render_template('ben.html')

@app.route('/bill')    
def bill():
    return render_template('bill.html')

@app.route('/bob')    
def bob():
    return render_template('bob.html')
    
@app.route('/harry')
def harry():
    return render_template('harry.html')

@app.route('/jay')    
def jay():
    return render_template('jay.html')

@app.route('/matt')    
def matt():
    return render_template('matt.html')

@app.route('/morbo')    
def morbo():
    return render_template('morbo.html')