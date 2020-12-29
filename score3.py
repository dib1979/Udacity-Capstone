Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
import os
import pandas as pd
import json
import pickle
#from azureml.core import Model
from sklearn.externals import joblib
import azureml.train.automl


def init():
    global deploy_model
    model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), 'best_fit_automl_model.pkl')
    deploy_model = joblib.load(model_path)

def run(data):
    try:
        temp = json.loads(data)
        data = pd.DataFrame(temp['data'])
        result = deploy_model.predict(data)
        # You can return any data type, as long as it is JSON serializable.
        return result.tolist()
    except Exception as e:
        error = str(e)
        return error