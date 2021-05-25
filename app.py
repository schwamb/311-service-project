#import libraries
import numpy as np
from flask import Flask, render_template,request, jsonify
from flask_cors import CORS
from joblib import load
app = Flask(__name__)
CORS(app)

reg = load("model")

@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/predict',methods=['POST'])
# def predict():

#     int_features = [int(x) for x in request.form.values()]
#     final_features = [np.array(int_features)]
#     prediction = reg.predict(final_features)

#     output = round(prediction[0], 2)

#     return render_template('index.html', prediction_text='Turnaround time should be {} days'.format(output))

@app.route('/test')
def test():
    request.args.get("param1")
    print(request.args)
    return request.args


if __name__ == "__main__":
    app.run(debug=True)

