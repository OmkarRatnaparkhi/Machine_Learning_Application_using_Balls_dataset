# Machine_Learning_Application_using_Balls_dataset

### Description :
* Below application uses Decision Tree algorithm to classify the type of ball.
* In this application training set contains two types of balls.
* Features of our training set is weight and type of surface of ball.
* We are using two labels as Tennis and Cricket.
* We train our data set using Decision tree algorithm.

### Consider below characteristics of Machine Learning Application :
* Classifier : Decision Tree
* DataSet : Balls Dataset
* Features : Weight & Surface type
* Labels : Tennis and Cricket
* Training Dataset : 15 Entries
* Testing Dataset : 1 Entry

### Training set referred by above application 
<p align="center">
  <img src="https://github.com/OmkarRatnaparkhi/Machine_Learning_Application_using_Balls_dataset/blob/main/Assets/1Supervised%20Machine%20Learning%20using%20Decision%20Tree%20Balls%20Dataset%20Application.pdf%20-%20Adobe%20Acrobat%20Reader%20DC%20(32-bit)%2002-04-2021%2010_30_55.png" alt="Diagram1">
</p>
Note: In Source code Rough is considered as 1 and Smooth is considered as 0 as well as Tennis is considered as 1 and Cricket is considered as 2

### This Appication is example of Supervised machine learning:
Supervised machine learning : Supervised machine learning algorithms can apply what has been learned in the past to
new data using labeled examples to predict future events.
Starting from the analysis of a known training dataset, the learning algorithm produces
an inferred function to make predictions about the output values.
The system is able to provide targets for any new input after sufficient training.
The learning algorithm can also compare its output with the correct, intended output and
find errors in order to modify the model accordingly.

### sklearn machine learning library:
* Scikit-learn machine learning library is used in this application.
* For installing Scikit-learn library use command as : pip install -U scikit-learn
* Scikit-learn(sklearn) is a free software machine learning library for the Python programming language.
* It features various classification, regression and clustering algorithms including support vector machines, random forests, gradient boosting, k-means and DBSCAN, and is designed to interoperate with the Python numerical and scientific libraries NumPy and SciPy.
* In this application Decision Tree algorithm is used which is imported from Scikit-learn(sklearn) library.
* Decision Trees (DTs) are a non-parametric supervised learning method used for classification and regression. The goal is to create a model that predicts the value of a target variable by learning simple decision rules inferred from the data features. A tree can be seen as a piecewise constant approximation. Reference: https://scikit-learn.org/stable/modules/tree.html
* What is a decision tree ? :- A decision tree a tree like structure whereby an internal node represents an attribute, a branch represents a decision rule, and the leaf nodes represent an outcome. This works by splitting the data into separate partitions according to an attribute selection measure, which in this case is the Gini index (although we can change this to information gain if we wanted). This essentially means that we each split aims toreduce Gini impurity which measures how impure a node is according to incorrectly classified results.

### Steps used to design this application :
Step1: Get the data for the machine learning application. </br>
Step2: Clean, prepare and manipulate that data. </br>
Step3. Decide the machine learning algorithm and train the dataset. </br>
Step4. Test the algorithm with some test dataset. </br>
Step5. Depending on the test result improve the algorithm.  </br>

