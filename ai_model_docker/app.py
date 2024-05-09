import pickle
import numpy as np
from sklearn.datasets import load_iris

# Load Iris dataset
iris = load_iris()

#load the trained model
with open('ai_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Promt the user for input
print("input format: 1.5 3.5 0.2 3\n")
user_input = input("Please enter your input: ")
input_vector = np.array([float(i) for i in user_input.split()])

# Use the model to make to make a prediction
prediction = model.predict([input_vector])

#print(f"Prediction: {prediction}")

# Mapping predicted class to actual class label
target_names = iris['target_names']
predicted_class_name = target_names[int(prediction)]

print(predicted_class_name)
