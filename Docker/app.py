from keras.models import load_model
import joblib
import numpy
from flask import Flask, render_template, request
from tensorflow.python.keras.models import Model
from werkzeug import datastructures
app=Flask("Brain Stroke Prediction")
model=joblib.load('Brain.h5')
@app.route("/")
def home():
     return render_template('home.html')
@app.route("/output", methods=['GET'])
def output():
    if request.method=='GET':
       x1=request.args.get("a1")
       x2 = request.args.get("a2")
       if x2=="Yes":
           x2=1
       else:
           x2=0
       x3=request.args.get("a3")
       if x3=="Yes":
           x3=1
       else:
           x3=0
       x4=request.args.get("a4")
       x5=request.args.get("a5")
       x6=request.args.get("a6")
       if x6=="Male":
           x6=1
       else: 
           x6=0
       x7=request.args.get("a7")
       if x7=="Married":
           x7=1
       else:
           x7=0
       x8=request.args.get("a8")
       if x8=="Urban":
           x8=1
       else:
           x8=0
       x9=request.args.get("a9")
       if x9=="children":
           x9=0
       elif x9=="NeverWorked":
           x9=1
       elif x9=="GovtJob":
           x9=2
       elif x9=="Selfemployee":
           x9=3
       elif x9=="Private":
           x9=4
       x10=request.args.get("a10")
       if x10=="neversmoked":
           x10=0
       elif x10=="formerlysmoked":
           x10=1
       elif x10=="smokes":
           x10=2
       elif x10=="unknown":
           x10=3
       
       print(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10)
       output = model.predict([[int(x1),int(x2),int(x3),float(x4),float(x5),int(x6),int(x7),int(x8),int(x9),int(x10)]])
       print("output is :",output)
       if output==1:
           data="Consult a Doctor for treatment"
           return render_template("output.html",data=data)
       else:
           data="No need"
           return render_template("output.html",data=data)
app.run(host="0.0.0.0",port=5000,debug=True)
