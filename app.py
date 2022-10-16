import pickle
import numpy as np
from flask import Flask, request

filepath = r"" # fill filepath

model = None # try a dictionary of multiple models

def load_model():
    global model
    with open('trained_model.pkl','rb') as f:
        model = pickle.load(f)
        
app = Flask(__name__)

@app.route('/')
def home_endpoint():
    return 'I have run!'

@app.route('/predict',methods = ['POST'])
def get_prediction():
    if model:
        try:
            json_ = request.json
            query = get_dummies(pd.DataFrame(json_))
            query = query.reindex(columns = model_columns, fill_value = 0)
            prediction = list(model.predict(query))
            return jsonify({'prediction': prediction})
        except:
            return jsonify({'trace': traceback.format_exc()})
    else:
        print('Trained Model NOT Loaded')
        
if __name__ = '__main__':
    model = joblib.load(trained_model.pkl)
    model_columns = joblib.load(model_columns.pkl)
    app.run(host = '0.0.0.0', port = 80, debug = True)
