import streamlit as st
import numpy as np
import pickle

# Load the model
model_filename = ('../model.pkl')
with open(model_filename, 'rb') as file:
    model = pickle.load(file)
    
st.title("Heart Disease Prediction Tool")
st.write("""
    ### Random Forest Model to Predict Risk of Heart Disease
""")

# Define columns
col1, col2, col3 = st.columns(3)

# Input features in columns
with col1:
    age = st.slider('Age (years)', 0, 120, 40)
    rbp = st.slider('Resting Blood Pressure (mmHg)', 80, 200, 120)
    chol = st.slider('Serum Cholesterol (mg/dL)', 100, 400, 200)
    MaxHR = st.slider('Maximum Heart Rate Achieved (bpm)', 70, 220, 150)

with col2:
    chest_pain_type = st.selectbox('Chest Pain Type', ["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"])
    chest_pain_type = {"Typical Angina": 0, "Atypical Angina": 1, "Non-Anginal Pain": 2, "Asymptomatic": 3}[chest_pain_type]

    Resting_Electrocardiographic_Results = st.selectbox("Resting Electrocardiographic Results", ["showing left ventricular hypertrophy", "Normal", "ST-T wave abnormality"])
    Resting_Electrocardiographic_Results = {"showing left ventricular hypertrophy": 0, "Normal": 1, "ST-T wave abnormality": 2}[Resting_Electrocardiographic_Results]

    Fasting_Blood_Sugar = st.selectbox('Fasting Blood Sugar', ["≤ 120 mg/dL", "> 120 mg/dL"])
    Fasting_Blood_Sugar = 1 if Fasting_Blood_Sugar == "> 120 mg/dL" else 0

    Oldpeak = st.number_input('OldPeak', min_value=0.0, max_value=6.0, value=1.0, step=0.1)

with col3:
    sex = st.selectbox('Sex', ["Male", "Female"])
    sex = 1 if sex == "Male" else 0

    Exercise_Induced_Angina = st.selectbox('Exercise-Induced Angina', ["Yes", "No"])
    Exercise_Induced_Angina = 1 if Exercise_Induced_Angina == "Yes" else 0

    ST_Slope = st.selectbox("ST Slope", ["Downsloping", "Flat", "Upsloping"])
    ST_Slope = {"Downsloping": 0, "Flat": 1, "Upsloping": 2}[ST_Slope]

# Prediction button
if st.button("Predict"):
    # Create input features array
    input_features = np.array([[age,sex, chest_pain_type, rbp, chol, Fasting_Blood_Sugar, Resting_Electrocardiographic_Results, MaxHR,
                               Exercise_Induced_Angina, Oldpeak, ST_Slope]])
    
    # Predict probability
    prediction_proba = model.predict_proba(input_features)[0][1]  # Probability of class 1
    prediction = model.predict(input_features)[0]  # Class label

    # Display the results
    st.write(f"The probability of having heart disease is: {prediction_proba:.2f}")
    st.write(f"Prediction: {'Heart Disease' if prediction == 1 else 'No Heart Disease'}")

# Age	Sex	ChestPainType	RestingBP	Cholesterol	FastingBS	RestingECG	MaxHR	ExerciseAngina	Oldpeak	ST_Slope	HeartDisease