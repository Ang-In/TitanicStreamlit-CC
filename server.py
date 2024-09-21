import streamlit as st
import pandas as pd
from fastai.vision.all import *

survivalModel = load_learner("titanicSurvivalPredictor.pkl")

'''def take_inputs():
    #name = input("What is your name? ")
    #age = float(input("How old are you? "))
    #gender = input("What is your gender (male/female)? ")
    #fare = float(input("Enter your ticket price: "))
    #sibSp = int(input("How many people are in your party? "))

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

    pDF = pd.DataFrame(passenger)
    pSurvival = survivalModel.predict(pDF.iloc[0])
    print(f"{name}, the chance that you will survive the sinking of the Titanic is: {pSurvival[2][1].item() * 100:.2f}%")'''

st.title("Survival Predictor: Will You Survive the Titanic?")
st.text("Built by Crystal")

name = st.text_input("What is your name? ")
age = st.number_input("How old are you? ", min_value=1, max_value=100, step=1)
gender = st.selectbox("Select your gender: ", ("male", "female"))
#fare = float(input("Enter your ticket price: "))
#sibSp = int(input("How many people are in your party? "))