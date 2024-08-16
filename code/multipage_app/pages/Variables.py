import streamlit as st
st.title("Variables used")
st.write("""
### Below are some of the variables used
1. Age \\
    Type: Integer \\
    Description: The age of the patient in years. 
2. Sex \\
    Type: Binary (0 or 1) \\
    Description: The sex of the patient. \\
        0: Male \\
        1: Female

3. Chest Pain Type (CP) \\
    Type: Categorical \\
    Description: The type of chest pain experienced by the patient. \\
        0: Typical Angina (TA) - Chest pain related to decreased blood supply to the heart. \\
        1: Atypical Angina (ATA) - Chest pain not related to heart issues. \\
        2: Non-Anginal Pain (NAP) - Indigestion or other types of chest pain not related to the heart. \\
        3: Asymptomatic (ASY) - No chest pain or heart-related symptoms.

4. Resting Blood Pressure (Trestbps) \\
    Type: Integer (in mm Hg) \\
    Description: Resting blood pressure of the patient.

5. Serum Cholesterol (Chol) \\
    Type: Integer (in mg/dL) \\
    Description: The patient's serum cholesterol level.

6. Fasting Blood Sugar (FBS) \\
    Type: Binary (0 or 1) \\
    Description: Whether the patient's fasting blood sugar is greater than 120 mg/dL. \\
        0: Fasting blood sugar ≤ 120 mg/dL \\
        1: Fasting blood sugar > 120 mg/dL

7. Resting Electrocardiographic Results (Restecg) \\
    Type: Categorical \\
    Description: Resting electrocardiographic results. \\
        0: Showing probable or definite left ventricular hypertrophy by Estes' criteria \\
        1: Normal \\
        2: Having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)

8. Maximum Heart Rate Achieved (Thalach) \\
    Type: Integer \\
    Description: The maximum heart rate achieved during a stress test.

9. Exercise-Induced Angina (Exang) \\
    Type: Binary (0 or 1) \\
    Description: Whether the patient experiences angina induced by exercise. \\
    0: No \\
    1: Yes
10. ST_slope: \\
    Type: Categorical \\
    Description: The slope of the peak exercise ST segment, which indicates the direction and nature of the ST segment during exercise, an important factor in diagnosing heart conditions. \\
    0: Downsloping - The ST segment goes downward, which is often associated with a higher risk of coronary artery disease and worse prognosis. \\
    1: Flat - The ST segment remains level, which may indicate potential ischemia (reduced blood flow to the heart). \\
    2: Upsloping - The ST segment goes upward, which is generally considered a better prognosis. \\
11. The Oldpeak feature in heart disease prediction datasets refers to the ST depression induced by exercise relative to rest. It is a crucial measure in stress tests used to diagnose the severity of heart disease. \\
    Type: Numerical (Continuous) \\
    Description: ST depression induced by exercise relative to rest, measured in millimeters. This feature helps in understanding how much the ST segment of an electrocardiogram (ECG) deviates from the baseline during peak exercise compared to rest. A higher value of ST depression often indicates a higher likelihood of heart disease, as it suggests the presence of ischemia or reduced blood flow to the heart muscle. \\
    Values: Typically a continuous range, e.g., 0.0, 1.5, 2.3, etc. \\
    Higher oldpeak values can indicate more severe blockages in the coronary arteries and a greater risk of heart disease. 
12. Outcome (Heart Disease):  \\
    Type: Categorical (Binary) \\
    Description: Indicates the presence of heart disease. \\
    0: No heart disease (Negative) \\
    1: Presence of heart disease (Positive)


""")