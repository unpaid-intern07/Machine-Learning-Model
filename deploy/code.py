import pickle
import streamlit as st
import numpy as np
import os
from streamlit_option_menu import option_menu

# Load model
base_path = os.path.dirname(__file__)
model_path = os.path.join(base_path, 'lung_cancer_model.sav')
model = pickle.load(open(model_path, 'rb'))

# Sidebar
with st.sidebar:
    selected = option_menu(
        'Lung Cancer Risk App',
        ['Predict Lung Cancer Risk'],
        icons=['lungs'],
        default_index=0
    )

# Main Page
if selected == 'Predict Lung Cancer Risk':
    st.title("🫁 Lung Cancer Risk Prediction")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", min_value=1, max_value=120)
        gender = st.selectbox("Gender", ['Male', 'Female'])
        smoking = st.selectbox("Do you smoke?", ['Yes', 'No'])
        yellow_fingers = st.selectbox("Yellow Fingers", ['Yes', 'No'])
        anxiety = st.selectbox("Do you experience anxiety?", ['Yes', 'No'])
        peer_pressure = st.selectbox("Peer Pressure", ['Yes', 'No'])
        chronic_disease = st.selectbox("Do you have a chronic disease?", ['Yes', 'No'])
        fatigue = st.selectbox("Fatigue?", ['Yes', 'No'])

    with col2:
        allergy = st.selectbox("Any Allergies?", ['Yes', 'No'])
        wheezing = st.selectbox("Wheezing?", ['Yes', 'No'])
        alcohol = st.selectbox("Do you drink alcohol?", ['Yes', 'No'])
        coughing = st.selectbox("Frequent coughing?", ['Yes', 'No'])
        short_breath = st.selectbox("Shortness of breath?", ['Yes', 'No'])
        swallowing = st.selectbox("Difficulty in swallowing?", ['Yes', 'No'])
        chest_pain = st.selectbox("Chest Pain?", ['Yes', 'No'])

    if st.button("🔍 Predict"):
        try:
            # Encoding
            def encode(val): return 1 if val == 'Yes' else 0
            gender_val = 1 if gender == 'Male' else 0

            input_data = [
                age, gender_val,
                encode(smoking), encode(yellow_fingers), encode(anxiety),
                encode(peer_pressure), encode(chronic_disease), encode(fatigue),
                encode(allergy), encode(wheezing), encode(alcohol), encode(coughing),
                encode(short_breath), encode(swallowing), encode(chest_pain)
            ]

            input_array = np.asarray(input_data).reshape(1, -1)
            prediction = model.predict(input_array)[0]
            result = "🛑 High Risk of Lung Cancer" if prediction == 1 else "✅ Low Risk of Lung Cancer"

            st.success(f"🎯 Prediction: {result}")

        except Exception as e:
            st.error(f"❌ Error: {e}")
