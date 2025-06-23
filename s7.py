import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np

# Load models
diabetes_model = pickle.load(open('D:/sem5 internship/diabbetes_model.sav', 'rb'))
heart_model = pickle.load(open("D:\sem5 internship\heart(logistic).sva", 'rb'))
parkinsons_model = pickle.load(open("D:/sem5 internship/parkinsons_logistic.sav", 'rb'))

# Sidebar Navigation
with st.sidebar:
    select = option_menu('Multiple Disease Prediction System',
                         ['Diabetes Prediction',
                          'Heart Disease Prediction',
                          'Parkinson Prediction'],
                         icons=['activity', 'heart', 'person'],
                         default_index=0)

# ------------------------- DIABETES -----------------------------------
if select == 'Diabetes Prediction':
    st.title('🩺 Diabetes Prediction using Machine Learning')

    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness Level')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI Value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    with col2:
        Age = st.text_input('Age')

    dia_diagnosis = ''

    if st.button('Diabetes Test Result'):
        try:
            input_data = [[float(Pregnancies), float(Glucose), float(BloodPressure),
                           float(SkinThickness), float(Insulin), float(BMI),
                           float(DiabetesPedigreeFunction), float(Age)]]
            dia_prediction = diabetes_model.predict(input_data)

            if dia_prediction[0] == 0:
                dia_diagnosis = '🟢 You are not diabetic'
            else:
                dia_diagnosis = '🔴 You have diabetes (Meetha Bandh!)'
        except:
            dia_diagnosis = '❌ Please enter all fields with valid numbers.'

    st.success(dia_diagnosis)

# ------------------------- HEART DISEASE ------------------------------
elif select == 'Heart Disease Prediction':
    st.title("❤️ Heart Disease Prediction App")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex (1=Male, 0=Female)')
    with col3:
        cp = st.text_input('Chest Pain Type (0-3)')
    with col4:
        trestbps = st.text_input('Resting Blood Pressure')
    with col1:
        chol = st.text_input('Cholesterol')
    with col2:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (1=True)')
    with col3:
        restecg = st.text_input('Resting ECG (0–2)')
    with col4:
        thalach = st.text_input('Max Heart Rate')
    with col1:
        exang = st.text_input('Exercise Induced Angina (1=Yes)')
    with col2:
        oldpeak = st.text_input('ST depression')
    with col3:
        slope = st.text_input('Slope (0–2)')
    with col4:
        ca = st.text_input('No. of Major Vessels (0–3)')
    with col1:
        thal = st.text_input('Thalassemia (1–3)')

    heart_diagnosis = ''

    if st.button('Heart Report Result'):
        try:
            input_data = [float(age), float(sex), float(cp), float(trestbps),
                          float(chol), float(fbs), float(restecg), float(thalach),
                          float(exang), float(oldpeak), float(slope), float(ca), float(thal)]
            heart_prediction = heart_model.predict([input_data])

            if heart_prediction[0] == 0:
                heart_diagnosis = '🟢 You are not likely to have heart disease'
            else:
                heart_diagnosis = '🔴 Risk of heart disease detected'
        except:
            heart_diagnosis = "❌ Please enter valid numerical values in all fields."

    st.success(heart_diagnosis)

# ------------------------- PARKINSON’S ------------------------------
elif select == 'Parkinson Prediction':
    st.title("🧠 Parkinson’s Disease Prediction App")

    # Create 2 columns for cleaner layout
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input("MDVP:Fo(Hz)")
        shimmer_db = st.text_input("MDVP:Shimmer(dB)")
        hnr = st.text_input("HNR")
        dfa = st.text_input("DFA")
        d2 = st.text_input("D2")

    with col2:
        fhi = st.text_input("MDVP:Fhi(Hz)")
        apq3 = st.text_input("Shimmer:APQ3")
        rpde = st.text_input("RPDE")
        spread1 = st.text_input("Spread1")
        ppe = st.text_input("PPE")

    with col3:
        flo = st.text_input("MDVP:Flo(Hz)")
        apq5 = st.text_input("Shimmer:APQ5")
        spread2 = st.text_input("Spread2")

    with col4:
        jitter_percent = st.text_input("MDVP:Jitter(%)")
        apq = st.text_input("MDVP:APQ")
        nhr = st.text_input("NHR")

    with col5:
        jitter_abs = st.text_input("MDVP:Jitter(Abs)")
        dda = st.text_input("Shimmer:DDA")
        rap = st.text_input("MDVP:RAP")
        ppq = st.text_input("MDVP:PPQ")
        ddp = st.text_input("Jitter:DDP")

    diagnosis = ''

    if st.button('Check Parkinson’s Result'):
        try:
            input_features = [
                float(fo), float(fhi), float(flo), float(jitter_percent),
                float(jitter_abs), float(rap), float(ppq), float(ddp),
                float(shimmer_db), float(apq3), float(apq5), float(apq),
                float(dda), float(nhr), float(hnr), float(rpde),
                float(dfa), float(spread1), float(spread2), float(d2),
                float(ppe)
                ]
            park_prediction = parkinsons_model.predict(input_data)
        except ValueError:
            diagnosis = "❌ Please enter valid numerical values in all fields."

    st.success(diagnosis)

