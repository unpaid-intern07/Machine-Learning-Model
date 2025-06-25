import pickle
import streamlit as st
import numpy as np
from streamlit_option_menu import option_menu
import os

# Load trained model
base_path = os.path.dirname(__file__)
model_path = os.path.join(base_path, 'online.sav')
model = pickle.load(open(model_path, 'rb'))

# Prediction logic
def predict(input_data):
    input_array = np.asarray(input_data).reshape(1, -1)
    prediction = model.predict(input_array)

    if prediction[0] == 0:
        return 'High'
    elif prediction[0] == 1:
        return 'Low'
    elif prediction[0] == 2:
        return 'Medium'
    else:
        return 'Unknown'

# Main app
def main():
    st.title("🎮 Online Gaming Engagement Prediction App")

    # Inputs
    Age = st.text_input("Age")
    Gender = st.selectbox("Gender", ['Male', 'Female'])  # Male=1, Female=0
    Location = st.selectbox("Location", ['USA', 'Europe', 'Asia', 'Other'])
    GameGenre = st.selectbox("Game Genre", ['Strategy', 'Sports', 'Action'])
    PlayTimeHours = st.text_input("Play Time Hours")
    InGamePurchases = st.text_input("In-Game Purchases")
    GameDifficulty = st.selectbox("Game Difficulty", ['Easy', 'Medium', 'Hard'])
    SessionsPerWeek = st.text_input("Sessions Per Week")
    AvgSessionDurationMinutes = st.text_input("Average Session Duration (Minutes)")
    PlayerLevel = st.text_input("Player Level")
    AchievementsUnlocked = st.text_input("Achievements Unlocked")

    # Encoding maps
    gender_map = {'Male': 1, 'Female': 0}
    location_map = {'USA': 0, 'Europe': 1, 'Asia': 2, 'Other': 3}
    genre_map = {'Strategy': 0, 'Sports': 1, 'Action': 2}
    difficulty_map = {'Easy': 0, 'Medium': 1, 'Hard': 2}

    # Button logic
    if st.button("🔍 Predict Engagement Level"):
        try:
            # Convert and map inputs
            input_list = [
                float(Age),
                gender_map[Gender],
                location_map[Location],
                genre_map[GameGenre],
                float(PlayTimeHours),
                float(InGamePurchases),
                difficulty_map[GameDifficulty],
                float(SessionsPerWeek),
                float(AvgSessionDurationMinutes),
                float(PlayerLevel),
                float(AchievementsUnlocked)
            ]

            result = predict(input_list)
            st.success(f"✅ Predicted Engagement Level: *{result}*")

        except Exception as e:
            st.error(f"❌ Error: Please check your inputs.\nDetails: {e}")

if __name__ == '__main__':
    main()
