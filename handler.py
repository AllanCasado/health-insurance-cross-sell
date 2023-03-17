from flask import Flask, request, Response
from healthinsurance.HealthInsurance import HealthInsurance
import pandas as pd
import pickle
import os

#loading model
path = ''
model = pickle.load(open(path + 'artifacts/model.pkl', 'rb'))

#initializing api
app = Flask(__name__)

#see if api is working
@app.route('/health')
def health():
    return Response('Pong', status=200, mimetype='application/json')

#make prediction
@app.route('/healthinsurance/predict', methods=["POST"])
def health_insurance_predict():
    test_json = request.get_json()
    
    if test_json:
        if isinstance(test_json, dict): #unique_example
            test_raw = pd.DataFrame(test_json, index=[0])
        
        else:
            test_raw = pd.DataFrame(test_json, columns=test_json[0].keys())
            
        #instantiate health insurance class
        pipeline = HealthInsurance()

        original_data = test_raw.copy()

        #data cleaning
        df1 = pipeline.data_cleaning(test_raw)

        #data preparation
        df2 = pipeline.data_preparation(df1)

        #data selection
        prediction_data = pipeline.data_selection(df2)

        #get precition
        df_response = pipeline.get_prediction(model, original_data, prediction_data)

        return df_response

    else:
        return Response('{}', status=200, mimetype='application/json')

if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run(host='0.0.0.0', port=port)