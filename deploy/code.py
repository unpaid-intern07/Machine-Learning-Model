import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

# Load trained model
base_path = os.path.dirname(__file__)
model_path = os.path.join(base_path, 'placement_model.sav')
model = pickle.load(open(model_path, 'rb'))

# Sidebar
with st.sidebar:
    selected = option_menu(
        'Placement Prediction App',
        ['Predict Placement'],
        icons=['briefcase'],
        default_index=0
    )

if selected == 'Predict Placement':
    st.title('🎓 Campus Placement Predictor')

    # Collect user input
    col1, col2, col3 = st.columns(3)

    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
        ssc_p = st.number_input("SSC Percentage", min_value=0.0, max_value=100.0)
        hsc_p = st.number_input("HSC Percentage", min_value=0.0, max_value=100.0)
        degree_p = st.number_input("Degree Percentage", min_value=0.0, max_value=100.0)

    with col2:
        ssc_b = st.selectbox("SSC Board", ["Central", "Others"])
        hsc_b = st.selectbox("HSC Board", ["Central", "Others"])
        hsc_s = st.selectbox("HSC Stream", ["Commerce", "Science", "Arts"])
        workex = st.selectbox("Work Experience", ["Yes", "No"])

    with col3:
        degree_t = st.selectbox("Degree Type", ["Sci&Tech", "Comm&Mgmt", "Others"])
        etest_p = st.number_input("E-test Percentage", min_value=0.0, max_value=100.0)
        specialisation = st.selectbox("MBA Specialisation", ["Mkt&HR", "Mkt&Fin"])
        mba_p = st.number_input("MBA Percentage", min_value=0.0, max_value=100.0)

    # On predict
    if st.button("Predict Placement"):
        try:
            input_dict = {
                'gender': gender,
                'ssc_p': ssc_p,
                'ssc_b': ssc_b,
                'hsc_p': hsc_p,
                'hsc_b': hsc_b,
                'hsc_s': hsc_s,
                'degree_p': degree_p,
                'degree_t': degree_t,
                'workex': workex,
                'etest_p': etest_p,
                'specialisation': specialisation,
                'mba_p': mba_p
            }

            input_df = pd.DataFrame([input_dict])

            prediction = model.predict(input_df)[0]
            result = "✅ Placed" if prediction == 1 else "❌ Not Placed"

            st.success(f"🎯 Prediction: {result}")

        except Exception as e:
            st.error(f"❌ Error: {e}")
