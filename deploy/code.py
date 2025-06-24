import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load model
base_path = os.path.dirname(__file__)
model_path = os.path.join(base_path, 'weather_model.sav')
weather_model = pickle.load(open(model_path, 'rb'))

# Sidebar
with st.sidebar:
    selected = option_menu(
        'Weather Prediction App',
        ['Weather Predictor'],
        icons=['cloud-sun'],
        default_index=0
    )

if selected == 'Weather Predictor':
    st.title('☀️ Weather Condition Predictor')

    col1, col2, col3 = st.columns(3)

    with col1:
        temperature = st.text_input("Temperature (°C)")
        humidity = st.text_input("Humidity (%)")
        wind_speed = st.text_input("Wind Speed (km/h)")
        precipitation = st.text_input("Precipitation (%)")

    with col2:
        pressure = st.text_input("Atmospheric Pressure (hPa)")
        uv_index = st.text_input("UV Index")
        visibility = st.text_input("Visibility (km)")
        cloud_cover = st.text_input("Cloud Cover (%)")

    with col3:
        season = st.selectbox("Season", ["Winter", "Spring", "Autumn", "Summer"])
        location = st.selectbox("Location", ["Coastal", "Mountain", "Inland"])  # Matches lowercase training keys
        weather_type = st.selectbox("Weather Type", ["Rainy", "Sunny", "Cloudy", "Snowy"])

    # Correct mapping as per your model training
    season_map = {"Winter": 0, "Spring": 1, "Autumn": 2, "Summer": 3}
    location_map = {"Coastal": 0, "Mountain": 1, "Inland": 2}
    weather_type_map = {"Rainy": 0, "Sunny": 1, "Cloudy": 2, "Snowy": 3}

    # Output label mapping for prediction result
    weather_label_map = {
        0: "Rainy ☔",
        1: "Sunny ☀️",
        2: "Cloudy ☁️",
        3: "Snowy ❄️"
    }

    if st.button("Predict"):
        inputs = [temperature, humidity, wind_speed, precipitation, pressure,
                  uv_index, visibility, cloud_cover]

        if any(val.strip() == "" for val in inputs):
            st.warning("⚠️ Please fill in all numerical fields.")
        else:
            try:
                input_data = [
                    float(temperature), float(humidity), float(wind_speed), float(precipitation),
                    float(pressure), float(uv_index), float(visibility),
                    season_map[season], location_map[location],
                    weather_type_map[weather_type], float(cloud_cover)
                ]

                st.write("🔍 Input to Model:", input_data)
                prediction = weather_model.predict([input_data])[0]
                diagnosis = f"✅ Weather prediction result: {weather_label_map.get(prediction, 'Unknown')}"

            except Exception as e:
                diagnosis = f"❌ Error: {e}"

            st.success(diagnosis)
