from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import numpy as np
import pickle


#load the iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2, random_state = 42)

# Create a Random forest classifier and train it on the traing data
model = RandomForestClassifier(n_estimators = 100, random_state = 42)
model.fit(X_train, y_train)

# Evaluate the model on the test data
y_pred = model.predict(X_test)
print( f"Model accuracy: {accuracy_score(y_test, y_pred)}")

# Save the trained model to a file
#with open('ai_model.pkl', 'wb') as f:
#    pickle.dump(model,f)


# trying to take user input and then test the model
user_input = input("please enter your input: ")
input_vector = np.array([float(i) for i in user_input.split()])

prediction_test = model.predict([input_vector])
print(prediction_test)
