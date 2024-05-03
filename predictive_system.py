import streamlit as st
import pickle as pkl
import pandas as pd
import numpy as np  # Add numpy import for reshaping

# Function to load the trained model
@st.cache(allow_output_mutation=True)
def load_model():
    with open("irisproject.sav", "rb") as model_file:
        model = pkl.load(model_file)
    return model

# Function to make predictions
def predict_species(sepal_length, sepal_width, petal_length, petal_width, model):
    features = [[sepal_length, sepal_width, petal_length, petal_width]]
    prediction = model.predict(features)
    return prediction[0]

# Streamlit web app
def main():
    st.title("Iris Flower Species Prediction")
    st.write("Enter the details of the iris flower to predict its species.")

    # Load the model
    model = load_model()

    # Input fields for user
    sepal_length = st.slider("Sepal Length", 4.0, 8.0, 5.0)
    sepal_width = st.slider("Sepal Width", 2.0, 4.5, 3.0)
    petal_length = st.slider("Petal Length", 1.0, 7.0, 4.0)
    petal_width = st.slider("Petal Width", 0.1, 2.5, 1.0)

    # Predict button
    if st.button("Predict"):
        prediction = predict_species(sepal_length, sepal_width, petal_length, petal_width, model)
        species_mapping = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}
        st.write(f"The predicted species is: {species_mapping[prediction]}")

if __name__ == "__main__":
    main()
