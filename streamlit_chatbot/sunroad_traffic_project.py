import streamlit as st
import random

# Set up the page
st.set_page_config(page_title="Sunroad Traffic Project", page_icon="🚗")

# Title and header
st.title("🚦 Sunroad Traffic Project")
st.subheader("Area: Sunway City")

# Description
st.write("Check traffic reasons and how to avoid them.")

# Dropdown for locations
location = st.selectbox("Select a location in Sunway City:", [
    "Sunway Pyramid Entrance",
    "Jalan PJS 11/28",
    "Persiaran Lagoon",
    "Sunway University Road",
    "Jalan Subang Indah"
])

# Define traffic info function
def get_traffic_info(location):
    durations = ["10 minutes", "30 minutes", "1 hour", "45 minutes"]
    reasons = [
        "School dismissal traffic",
        "Mall congestion (Sunway Pyramid)",
        "Peak hour rush",
        "Road construction",
        "Weather condition (rain)"
    ]
    tips = [
        "Use alternate route via Subang Jaya",
        "Travel before 7AM or after 10AM",
        "Avoid mall areas during weekends",
        "Check Waze or Google Maps before leaving",
        "Use public transport (BRT or KTM)"
    ]
    return {
        "location": location,
        "duration": random.choice(durations),
        "reason": random.choice(reasons),
        "tip": random.choice(tips)
    }

# Display traffic info after selection
if location:
    info = get_traffic_info(location)
    st.success(f"📍 Location: {info['location']}")
    st.info(f"⏳ Duration: {info['duration']}")
    st.warning(f"⚠ Reason: {info['reason']}")
    st.write(f"💡 *Tip to Avoid Traffic:* {info['tip']}")
