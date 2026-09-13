import streamlit as st
import joblib

# Load model
model = joblib.load("model/model.pkl")

# Page config
st.set_page_config(
    page_title="SMS Spam Detector",
    page_icon="📩",
    layout="centered"
)

# Title
st.title("📩 SMS Spam Detector")
st.write("Enter an SMS message to check whether it is **Spam** or **Ham**.")

# Input
message = st.text_area(
    "Enter your message:",
    placeholder="e.g. Congratulations! You have won a prize..."
)

# Prediction
if st.button("Predict", use_container_width=True):

    if not message.strip():
        st.warning("Please enter a message.")

    else:
        prediction = model.predict([message])[0]

        st.subheader("Result")

        if prediction == "spam":
            st.error("🚨 SPAM")
        else:
            st.success("✅ HAM")