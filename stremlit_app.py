import streamlit as st

st.set_page_config(page_title="Ayurvedic Lifestyle Optimizer", layout="centered")

# --- SKY BLUE BACKGROUND ---


st.title("Ayurvedic Lifestyle Optimizer")
st.write("Evaluate your daily routine using Ayurveda (Dinacharya principles)")

# --- INPUTS ---
st.header("Lifestyle Inputs")

wake_time = st.slider("Wake-up Time (hour)", 4, 10, 7)
sleep_time = st.slider("Sleep Time (hour)", 20, 2, 23)
screen_time = st.slider("Screen Time (hours/day)", 0, 12, 5)
work_hours = st.slider("Work/Study Hours", 0, 12, 6)
stress = st.slider("Stress Level (1-10)", 1, 10, 5)

st.header("Health & Ayurveda Inputs")

activity = st.slider("Physical Activity (minutes/day)", 0, 120, 30)
meditation = st.slider("Meditation/Yoga (minutes/day)", 0, 60, 10)
water = st.slider("Water Intake (glasses(250ml/)/day)", 0, 15, 6)
meals = st.selectbox("Regular Meal Timing?", ["Yes", "No"])
junk = st.selectbox("Junk Food Frequency", ["Low", "Moderate", "High"])
nature = st.slider("Nature Exposure (minutes/day)", 0, 120, 20)
digestion = st.selectbox("Digestion Quality", ["Good", "Average", "Poor"])
energy = st.slider("Energy Level (1-10)", 1, 10, 5)

# --- SCORING ---
score = 0

if wake_time <= 7:
    score += 10

if sleep_time <= 23 or sleep_time <= 2:
    score += 10

if screen_time <= 4:
    score += 10

if activity >= 30:
    score += 15

if meditation >= 10:
    score += 10

if water >= 7:
    score += 10

if meals == "Yes":
    score += 10

if junk == "Low":
    score += 10
elif junk == "Moderate":
    score += 5

if nature >= 20:
    score += 5

if digestion == "Good":
    score += 5

score += energy * 0.5

if stress <= 4:
    score += 10
elif stress <= 7:
    score += 5

# --- CLASSIFICATION ---
if score >= 80:
    category = "Healthy"
elif score >= 50:
    category = "Moderate"
else:
    category = "Needs Improvement"

# --- OUTPUT ---
st.subheader(f"Your Score: {int(score)}/100")
st.progress(int(score))

st.subheader(f"Lifestyle Category: {category}")

# --- SUGGESTIONS ---
st.write("Personalized Ayurvedic Suggestions:")

if wake_time > 7:
    st.write("- Wake up earlier (Brahma Muhurta)")

if sleep_time > 23:
    st.write("- Sleep before 11 PM")

if screen_time > 4:
    st.write("- Reduce screen exposure")

if activity < 30:
    st.write("- Add yoga or walking")

if meditation < 10:
    st.write("- Practice meditation daily")

if water < 7:
    st.write("- Increase water intake")

if meals == "No":
    st.write("- Maintain fixed meal timings")

if junk == "High":
    st.write("- Reduce junk food")

if nature < 20:
    st.write("- Spend time outdoors")

if digestion == "Poor":
    st.write("- Improve diet for better digestion")

if stress > 6:
    st.write("- Practice breathing exercises (Pranayama)")

if energy < 5:
    st.write("- Improve sleep and nutrition")
