
# coding: utf-8

# In[ ]:



import argparse
import os

# importing necessary libraries
import numpy as np

from sklearn import datasets
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

from azureml.data.dataset_factory import TabularDatasetFactory
from azureml.core.dataset import Dataset
from azureml.data.datapath import DataPath

import joblib

from azureml.core.run import Run


# loading the iris dataset
url_path = 'https://raw.githubusercontent.com/dib1979/Temporary/main/IRIS.csv'
dataset = TabularDatasetFactory.from_delimited_files(path=url_path)
df = dataset.to_pandas_dataframe()   
    
# X -> features, y -> label
X= df.drop(['species'], axis=1)
y = df['species']

# dividing X, y into train and test data
from sklearn.model_selection import train_test_split
import pandas as pd

(X_train, X_test, y_train, y_test) = train_test_split(X, y, test_size= 0.3, random_state = 0)
label = 'species'



def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--kernel', type=str, default='linear',
                        help='Kernel type to be used in the algorithm')
    parser.add_argument('--penalty', type=float, default=1.0,
                        help='Penalty parameter of the error term')

    args = parser.parse_args()
    
    run = Run.get_context()
    
    run.log('Kernel type', np.str(args.kernel))
    run.log('Penalty', np.float(args.penalty))



    

    # training a linear SVM classifier
    from sklearn.svm import SVC
    svm_model_linear = SVC(kernel=args.kernel, C=args.penalty).fit(X_train, y_train)
    svm_predictions = svm_model_linear.predict(X_test)

    # model accuracy for X_test
    accuracy = svm_model_linear.score(X_test, y_test)
    print('Accuracy of SVM classifier on test set: {:.2f}'.format(accuracy))
    run.log('Accuracy', np.float(accuracy))
    # creating a confusion matrix
    cm = confusion_matrix(y_test, svm_predictions)
    print(cm)

    os.makedirs('outputs', exist_ok=True)
    # files saved in the "outputs" folder are automatically uploaded into run history
    joblib.dump(svm_model_linear, 'outputs/model.joblib')


if __name__ == '__main__':
    main()

