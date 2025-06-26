import streamlit as st
import numpy as np
import pickle

# Load trained model
with open('C:/Users/HP/deploy/cancer_survival_model.sav', 'rb') as f:
    model = pickle.load(f)

# Load label encoders
with open('C:/Users/HP/deploy/label_encoders.sav', 'rb') as f:
    encoders = pickle.load(f)

# Title
st.title("🩺 Lung Cancer Survival Prediction")

# Inputs
age = st.number_input("Age", min_value=1, max_value=120, value=55)

gender = st.selectbox("Gender", encoders['gender'].classes_)
country = st.selectbox("Country", encoders['country'].classes_)
cancer_stage = st.selectbox("Cancer Stage", encoders['cancer_stage'].classes_)
family_history = st.selectbox("Family History", encoders['family_history'].classes_)
smoking_status = st.selectbox("Smoking Status", encoders['smoking_status'].classes_)
treatment_type = st.selectbox("Treatment Type", encoders['treatment_type'].classes_)

bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0)
cholesterol = st.number_input("Cholesterol Level", min_value=100, max_value=400, value=200)

hypertension = st.selectbox("Hypertension", ['No', 'Yes'])
asthma = st.selectbox("Asthma", ['No', 'Yes'])
cirrhosis = st.selectbox("Cirrhosis", ['No', 'Yes'])
other_cancer = st.selectbox("Other Cancer History", ['No', 'Yes'])

treatment_duration = st.number_input("Treatment Duration (days)", min_value=1, max_value=2000, value=365)

# Convert Yes/No to 0/1
def binary(val): return 1 if val == 'Yes' else 0

# Prediction
if st.button("Predict"):
    try:
        input_data = np.array([[
            age,
            encoders['gender'].transform([gender])[0],
            encoders['country'].transform([country])[0],
            encoders['cancer_stage'].transform([cancer_stage])[0],
            encoders['family_history'].transform([family_history])[0],
            encoders['smoking_status'].transform([smoking_status])[0],
            bmi,
            cholesterol,
            binary(hypertension),
            binary(asthma),
            binary(cirrhosis),
            binary(other_cancer),
            encoders['treatment_type'].transform([treatment_type])[0],
            treatment_duration
        ]])

        result = model.predict(input_data)[0]
        if result == 1:
            st.success("✅ Likely to Survive.")
        else:
            st.error("❌ Not Likely to Survive.")
    except Exception as e:
        st.error(f"Error during prediction: {e}")
