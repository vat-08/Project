from flask import Flask, render_template, request

app = Flask(__name__)# interface between my server and my application wsgi
import numpy as np
import pickle
model = pickle.load(open(r'D:/ML/Flask/model1.pkl','rb'))

@app.route('/')#binds to an url

def helloworld():
    return render_template("index.html")

@app.route('/login', methods =['POST'])#binds to an url
def login():
    p =request.form['ut']
    q= request.form['te']
    r= request.form['hu']
    s= request.form['tv']
    t= request.form['co']
    u= request.form['ra']
    v=request.form['et']
    w=request.form['pr']
    x=request.form['pm']
    y=request.form['pn']
    z=request.form['nc']
    a=request.form['nd']
    b=request.form['ne']
    c=request.form['cn']
    total=np.array([[p,q,r,s,t,u,v,w,x,y,z,a,b,c]])
    output= model.predict(total)
    print(output) 
    if(output==0):  
     return render_template("index.html",y = "Smoke is not detected" )
    else:
     return render_template("index.html",y = "Smoke is detected" )
if __name__ == '__main__' :
    app.run(debug= False)


