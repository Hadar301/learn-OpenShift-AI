import streamlit as st
import pandas as pd
import joblib
from loguru import logger
import random

# Load model
@st.cache_resource
def load_model():
    return joblib.load("model/model.joblib")

_MODEL = load_model()

# Page title
st.title("🚢 Titanic Survival Predictor")

# Input fields
pclass = st.selectbox("Passenger Class (1 = 1st, 2 = 2nd, 3 = 3rd)", [1, 2, 3])
sex = st.selectbox("Sex", ["male", "female"])
age = st.slider("Age", 0, 100, 30)
sibsp = st.slider("Siblings/Spouses Aboard", 0, 8, 0)
parch = st.slider("Parents/Children Aboard", 0, 6, 0)
fare = st.slider("Fare Paid", 0.0, 600.0, 50.0)
embarked = st.selectbox("Port of Embarkation", ["C", "Q", "S"])

# Map inputs to encoded values
sex = 1 if sex == "male" else 0
embarked_map = {"C": 0, "Q": 1, "S": 2}
embarked = embarked_map[embarked]
adult_male = 1 if (sex == 1 and age >= 18) else 0
is_alone = 1 if sibsp > 0 else 0
# Create dataframe
input_data = pd.DataFrame([[pclass, sex, age, sibsp, parch, fare, embarked, adult_male, is_alone]],
                          columns=["pclass", "sex", "age", "sibsp", "parch", "fare", "embarked", "adult_male", "alone"])

# Predict
if st.button("Predict"):
    prediction = _MODEL.predict(input_data)[0]
    result = "🟢 Survived" if prediction == 1 else "🔴 Did Not Survive"
    st.markdown(f"### Prediction: {result}")
