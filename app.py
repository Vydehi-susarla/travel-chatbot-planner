import streamlit as st
import google.generativeai as genai
from utils import build_advanced_prompt

# Set up Gemini API
genai.configure(api_key="your-real-api-key")  # Replace with real key
model = genai.GenerativeModel("gemini-1.5-flash")

# UI
st.set_page_config(page_title="Smart Travel Bot", page_icon="🧳")
st.title("🧳 Smart Travel Planner")
st.write("Plan your ideal trip with AI 🚀")

# Inputs
trip_type = st.selectbox("✈️ Trip Type", ["Backpacking", "Luxury", "Family", "Solo", "Honeymoon"])
budget = st.text_input("💰 Your Budget (₹)", placeholder="25000")
duration = st.text_input("📆 Duration (e.g., 5 days)")
season = st.selectbox("🌦️ Travel Season", ["Summer", "Winter", "Monsoon", "Anytime"])
location = st.text_input("📍 Region or Country", placeholder="Europe, South India...")

filters = st.multiselect(
    "🎛️ Special Filters",
    ["Visa-free", "Snow", "Beaches", "Adventure", "Relaxation", "Spiritual", "Wildlife", "Historical"],
)

# Button to generate
if st.button("🎯 Get Full Plan"):
    if not all([trip_type, budget, duration, season, location]):
        st.warning("Please fill in all fields.")
    else:
        with st.spinner("Planning your trip with Gemini..."):
            prompt = build_advanced_prompt(budget, duration, season, location, trip_type, filters)
            response = model.generate_content(prompt)
            st.success("Here's your plan:")
            st.markdown(response.text)
