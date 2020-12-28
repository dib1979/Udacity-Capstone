# Project Title -  Predicting IRIS Flower Species                                                                                                       

The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by the British statistician, eugenicist, and biologist Ronald Fisher. The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters. Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other.  
The Project is using the same dataset to train a ML model using Hyperdrive and AutoML runs, then deploy the best model as a Webservice in terms of Accuracy which has been chosen as the Primary metric. Finally we would test the Prediction capability of the model by calling the Webservice. 
Additionally we have enabled Application insight to view the detailed logs related to the requests being sent to the web app.

## Project Set Up and Installation
*OPTIONAL:* If your project has any special installation steps, this is where you should put it. To turn this project into a professional portfolio project, you are encouraged to explain how to set up this project in AzureML.

## Dataset

### Overview
The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters. 
1. Sepal Length 
2. Sepal Width 
3. Petal Length 
4. Petal Width 

Based on the combination of these four features the species of the flower is being determined. We have taken the IRIS data set from Kaggle and added the same to github repository. 
The dataset is accessed directly within Azure from github using Azure's TabularDatasetFactory


### Task
The project focuses on building a Classification Model.  
First we are training the Model using Hyperdrive and AutoML.  
Then we deploy the best model as a webservice which is being chosen based upon the Primary Metric - Accuracy score. 
Finally we would test the Prediction capability of the model by calling the Webservice.  
Additionally we have enabled Application insight to view the detailed logs related to the requests being sent to the web app. 


### Access
The dataset is accessed directly from github using Azure's TabularDatasetFactory

<img src="Capstone/pic1.PNG">

## Automated ML
### AutoML Settings
1. "enable_early_stopping" : True - Whether to enable early termination if the score is not improving in the short term. The default is False. 
2. "iteration_timeout_minutes": 5 - Maximum time in minutes that each iteration can run for before it terminates. If not specified, a value of 1 month or 43200 minutes is used. 
3. "max_concurrent_iterations": 4 - Represents the maximum number of iterations that would be executed in parallel. The default value is 1. 
4. "max_cores_per_iteration": -1 - The maximum number of threads to use for a given training iteration.   
5. "featurization": 'auto' - FeaturizationConfig Indicator for whether featurization step should be done automatically or not, or whether customized featurization should be used 
6. "verbosity": logging.INFO - The verbosity level for writing to the log file. The default is INFO or 20. 

### Results
*TODO*: What are the results you got with your automated ML model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Hyperparameter Tuning
*TODO*: What kind of model did you choose for this experiment and why? Give an overview of the types of parameters and their ranges used for the hyperparameter search


### Results
*TODO*: What are the results you got with your model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
