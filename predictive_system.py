import streamlit as st
import pickle as pkl
import pandas as pd

# Load the trained model
model = pkl.load(open("irisproject.sav", "rb"))

# Function to make predictions
def predict_species(sepal_length, sepal_width, petal_length, petal_width):
    features = [[sepal_length, sepal_width, petal_length, petal_width]]
    prediction = model.predict(features)
    return prediction[0]

# Streamlit web app
def main():
    st.title("Iris Flower Species Prediction")
    st.write("Enter the details of the iris flower to predict its species.")

    # Input fields for user
    sepal_length = st.text_input("Sepal Length", "5.0")
    sepal_width = st.text_input("Sepal Width", "3.0")
    petal_length = st.text_input("Petal Length", "4.0")
    petal_width = st.text_input("Petal Width", "1.0")

    # Convert input to float
    sepal_length = float(sepal_length)
    sepal_width = float(sepal_width)
    petal_length = float(petal_length)
    petal_width = float(petal_width)

    # Predict button
    if st.button("Predict"):
        prediction = predict_species(sepal_length, sepal_width, petal_length, petal_width)
        species_mapping = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}
        st.write(f"The predicted species is: {species_mapping[prediction]}")

if __name__ == "__main__":
    main()

export PROJECT_ID=$(gcloud config get-value project)
gcloud projects add-iam-policy-binding $PROJECT_ID \
--member=serviceAccount:$(gcloud projects describe $PROJECT_ID \
--format="value(projectNumber)")@cloudbuild.gserviceaccount.com --role="roles/container.developer"

kubectl expose deployment development-deployment \
    --type=LoadBalancer \
    --name=dev-deployment-service \
    --port=8080 \
    --target-port=8080 \
    -n dev
