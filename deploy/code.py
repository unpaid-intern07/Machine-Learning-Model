import os
import pickle
import streamlit as st
import numpy as np
from streamlit_option_menu import option_menu

# Load model
base_path = os.path.dirname(__file__)
model_path = os.path.join(base_path, 'weather_model.sav')
weather_model = pickle.load(open(model_path, 'rb'))

# Sidebar navigation
with st.sidebar:
    selected = option_menu(
        'Weather Prediction App',
        ['Weather Predictor'],
        icons=['cloud-sun'],
        default_index=0
    )

# Main app
if selected == 'Weather Predictor':
    st.title('Weather Condition Predictor')

    col1, col2, col3 = st.columns(3)

    with col1:
        temperature = st.text_input("Temperature (°C)")
        wind_speed = st.text_input("Wind Speed (km/h)")
        cloud_cover = st.text_input("Cloud Cover (%)")
        uv_index = st.text_input("UV Index")

    with col2:
        humidity = st.text_input("Humidity (%)")
        precipitation = st.text_input("Precipitation (%)")
        pressure = st.text_input("Atmospheric Pressure (hPa)")
        season = st.selectbox("Season", ["Spring", "Summer", "Autumn", "Winter"])

    with col3:
        visibility = st.text_input("Visibility (km)")
        location = st.selectbox("Location", ["City A", "City B", "City C", "Other"])  # Replace with actual location list

    diagnosis = ''

    if st.button("Predict Weather Type"):
        # Check for empty inputs first
        required_fields = [temperature, humidity, wind_speed, precipitation,
                           cloud_cover, pressure, uv_index, visibility]

        if any(field.strip() == "" for field in required_fields):
            diagnosis = "Please fill in all numerical fields before submitting."
        else:
            try:
                # Encode categorical fields
                season_map = {"Spring": 0, "Summer": 1, "Autumn": 2, "Winter": 3}
                location_map = {"City A": 0, "City B": 1, "City C": 2, "Other": 3}

                # Convert all fields to float
                input_data = [
                    float(temperature), float(humidity), float(wind_speed), float(precipitation),
                    float(cloud_cover), float(pressure), float(uv_index), season_map[season],
                    float(visibility), location_map[location]
                ]

                # Debug print (optional)
                st.write("Encoded Input Data:", input_data)

                prediction = weather_model.predict([input_data])[0]
                diagnosis = f"Predicted Weather: {prediction}"

            except ValueError:
                diagnosis = "Invalid input detected. Please check each field for correct numbers."

        st.success(diagnosis)
