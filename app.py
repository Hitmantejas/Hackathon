from flask import Flask, abort, jsonify, request, render_template
import numpy as np
import sklearn
import joblib
import pickle

model_file = 'final_model.sav'
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


var = input("Please enter the news text you want to verify")

@app.route('/predict',methods=['POST'])
def detecting_fake_news(var):
    load_model = pickle.load(open('final_model.sav', 'rb'))
    prediction = load_model.predict([var])
    output = prediction[0]
    return (print("The Given statement is", output))
    return render_template('index.html', prediction_text = 'The news is: ${}'.format(output))
 
if __name__ == '__main__':
    detecting_fake_news(var)
