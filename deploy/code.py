import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load model
base_path = os.path.dirname(__file__)
model_path = os.path.join(base_path, 'weather_model.sav')  # Adjust path if needed
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
        location = st.selectbox("Location", ["Inland", "Mountain", "Coastal"])
        weather_type = st.selectbox("Weather Type", ["Rainy", "Sunny", "Cloudy", "Snowy"])

    # Mappings used during training
    season_map = {"Winter": 0, "Spring": 1, "Autumn": 2, "Summer": 3}
    location_map = {"Inland": 0, "Mountain": 1, "Coastal": 2}
    weather_type_map = {"Rainy": 0, "Sunny": 1, "Cloudy": 2, "Snowy": 3}

    if st.button("Predict"):
        # Check all numerical fields are filled
        inputs = [temperature, humidity, wind_speed, precipitation, pressure,
                  uv_index, visibility, cloud_cover]
        if any(val.strip() == "" for val in inputs):
            st.warning("⚠️ Please fill in all numerical fields.")
        else:
            try:
                # Convert inputs
                input_data = [
                    float(temperature), float(humidity), float(wind_speed), float(precipitation),
                    float(pressure), float(uv_index), float(visibility),
                    season_map[season], location_map[location],
                    weather_type_map[weather_type], float(cloud_cover)
                ]

                st.write("🔍 Input to Model:", input_data)
                st.write("Expected Features:", weather_model.n_features_in_)

                prediction = weather_model.predict([input_data])[0]
                st.success(f"✅ Weather prediction result: {prediction}")

            except Exception as e:
                st.error(f"❌ Error: {e}")
