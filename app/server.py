#import libraries
import numpy as np
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# prediction function
def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 8)
    loaded_model = pickle.load(open("model.pkl", "rb"))
    result = loaded_model.predict(to_predict)
    return result[0]
 
@app.route('/')
def home():
    return render_template('predict.html')

@app.route('/result', methods = ['POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(int, to_predict_list))
        result = ValuePredictor(to_predict_list)       
        if int(result)== 1:
            prediction ='He or She will likely GRADUATE or COMPLETE the program'
        else:
            prediction ='He or She will likely be TERMINATED from the program'                    
        return render_template("predict.html", prediction = prediction)

if __name__ == '__main__':
    app.run(port=5000, debug=True)