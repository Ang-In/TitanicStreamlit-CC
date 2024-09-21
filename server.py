import streamlit as st
import pandas as pd
from fastai.vision.all import *

survivalModel = load_learner("titanicSurvivalPredictor.pkl")

st.title("Survival Predictor: Will You Survive the Titanic?")
st.text("Built by Crystal")

name = st.text_input("What is your name? ")
age = st.number_input("How old are you? ", min_value=1, max_value=100, step=1)
gender = st.selectbox("Select your gender: ", ("male", "female"))
fare = st.number_input("Enter your ticket price: ", min_value=0.0, max_value=100.0, step=0.01)
sibSp = st.number_input("How many people are in your party? ", min_value=0, max_value=10, step=1)

passenger = {
    "Name": [name],
    "Age": [age],
    "Sex": [gender],
    "Fare": [fare],
    "SibSp": [sibSp],
    "Ticket": [-1],
    "Cabin": ['NaN'],
    "Embarked": ['S'],
    "Pclass": [2]
}

if st.button("Predict My Survival Rate!"):
    pDF = pd.DataFrame(passenger)
    pSurvival = survivalModel.predict(pDF.iloc[0])
    st.write(f"{name}, the chance that you will survive the sinking of the Titanic is: {pSurvival[2][1].item() * 100:.2f}%")