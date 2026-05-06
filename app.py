import streamlit as st
import pickle
import numpy as np

# Load models
svc_model = pickle.load(open("svc_model.pkl", "rb"))
rf_model = pickle.load(open("rf_model.pkl", "rb"))
dt_model = pickle.load(open("dt_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

st.title("Titanic Survival Predictor")

# Model selection
model_choice = st.selectbox("Choose Model", ["SVC", "Random Forest", "Decision Tree"])

# Inputs
pclass = st.selectbox("Passenger Class", [1, 2, 3])
sex = st.selectbox("Sex", ["male", "female"])
age = st.slider("Age", 0, 80, 25)
fare = st.number_input("Fare", 0.0, 500.0, 50.0)

sex = 1 if sex == "male" else 0

data = np.array([[pclass, sex, age, fare]])

# Prediction
if st.button("Predict"):

    if model_choice == "SVC":
        data = scaler.transform(data)
        prediction = svc_model.predict(data)

    elif model_choice == "Random Forest":
        prediction = rf_model.predict(data)

    else:
        prediction = dt_model.predict(data)

    if prediction[0] == 1:
        st.success("Survived")
    else:
        st.error("Did not survive")