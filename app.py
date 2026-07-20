import streamlit as st
import joblib
import numpy as np

# 1. Load your saved ML model
model = joblib.load('heart_disease_model.pkl')

# 2. Add Title and Subtitle to the Web Page
st.title("🫀 Heart Disease Risk Prediction")
st.write("Enter patient clinical parameters below to check the estimated risk of heart disease.")

st.divider()

# 3. Create Inputs for Patient Data (Age, Blood Pressure, Cholesterol, etc.)
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=1, max_value=120, value=50)
    sex = st.selectbox("Sex", options=[0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
    cp = st.selectbox("Chest Pain Type (0-3)", options=[0, 1, 2, 3])
    trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=80, max_value=220, value=120)
    chol = st.number_input("Serum Cholesterol (mg/dl)", min_value=100, max_value=600, value=200)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", options=[0, 1], format_func=lambda x: "False" if x == 0 else "True")
    restecg = st.selectbox("Resting ECG Results (0-2)", options=[0, 1, 2])

with col2:
    thalach = st.number_input("Max Heart Rate Achieved", min_value=60, max_value=220, value=150)
    exang = st.selectbox("Exercise Induced Angina", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
    oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.0, max_value=10.0, value=1.0, step=0.1)
    slope = st.selectbox("Slope of Peak Exercise ST Segment (0-2)", options=[0, 1, 2])
    ca = st.selectbox("Number of Major Vessels (0-4)", options=[0, 1, 2, 3, 4])
    thal = st.selectbox("Thalassemia (0 = Normal, 1 = Fixed Defect, 2 = Reversable Defect)", options=[0, 1, 2, 3])

st.divider()

# 4. Predict Button Logic
if st.button("Predict"):
    features = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    
    # Get raw probabilities
    probabilities = model.predict_proba(features)[0]
    prediction = model.predict(features)[0]
    
    st.write(f"**Debug Info:** Raw Prediction Class = `{prediction}`")
    st.write(f"**Debug Info:** Probabilities (Class 0 vs Class 1) = `{probabilities}`")

    if prediction == 1:
        st.error("⚠️ High Risk: Higher likelihood of heart disease detected.")
    else:
        st.success("✅ Low Risk: Lower likelihood of heart disease detected.")
