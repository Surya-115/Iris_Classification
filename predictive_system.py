import numpy as np
import pickle as pkl
import streamlit as st 

load_model = pkl.load(open('C:/Users/ssury/OneDrive/Desktop/internship project(working)/irisproject.sav','rb'))
def pred(x):
     x = np.asarray(x).reshape(1,-1)
     result = load_model.predict(x)
     if result[0] == 0:
         return("Satosa")
     elif(result[0] == 1):
         return("Versicolor")
     else:
         return("verginica")


def main():
     sl = st.number_input("Sepal-length")
     sw = st.number_input("Sepal-width")
     pl = st.number_input("Petal-length")
     pw = st.number_input("Petal-width")

     data = [sl, sw, pl, pw]

     if st.button("Predict"):
         st.write(pred(data))

if __name__ == "__main__":
    main()