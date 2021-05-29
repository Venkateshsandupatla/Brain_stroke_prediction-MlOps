from keras.models import load_model
import joblib
from flask import Flask, render_template, request
from tensorflow.python.keras.models import Model
app=Flask("Brain Stroke Prediction")
model=joblib.load('BrainStroke_prediction.h5')
@app.route("/home")
def home():
     return render_template('home.html')
@app.route("/output", methods=['GET'])
def output():
        x1=request.args.get('a1')
        x2=request.args.get('a2')
        if x2=="Yes":
            x2=1
        else:
            x2=0
        x3=request.args.get('a3')
        if x3=='Yes':
            x3=1
        else:
            x3=0
        x4=request.args.get('a4')
        x5=request.args.get('a5')
        x6=request.args.get('a6')
        if x6=="Male":
            x6=1
        else:
            x6=0
        x7=request.args.get('a7')
        if x7=="Married":
            x7=1
        else:
            x7=0
        x8=request.args.get('a8')
        if x8=="Urban":
            x8=1
        else:
            x8=0
        x9=request.args.get('a8')
        if x9=='Private Employee':
            x9=0
        elif x9=='Self-employed':
            x9=1
        elif x9=='Govt-Employee':
            x9=2
        elif x9=='Children':
            x9=3
        else:
            x9=4
        x10=request.args.get('a10')
        if x10=='formerly-smoked':
            x10=0
        elif x10=='Never-smoked':
            x10=1
        elif x10=='Smokes':
            x10=2
        else:
            x10=3
        output=model.predict([[int(x1),int(x2),int(x3),float(x4),float(x5),int(x6),int(x7),int(x8),int(x9),int(x10)]]) 
        data="Consult a doctor"
        if output == 1:
            data="Consult a doctor"
            return render_template('output.html',data=data)
        else:
            data="No doctor needed"
            return render_template('output.html',data=data)
        





app.run(host="0.0.0.0",port=5000,debug=True)