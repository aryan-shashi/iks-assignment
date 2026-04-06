import streamlit as st

st.title("🌿 Ayurvedic Lifestyle Optimizer")

st.write("Analyze your daily habits based on Ayurveda (Dinacharya)")

# Inputs
wake_time = st.slider("Wake-up Time (hour)", 4, 10, 7)
sleep_time = st.slider("Sleep Time (hour)", 20, 2, 23)
screen_time = st.slider("Screen Time (hours/day)", 0, 12, 5)
activity = st.slider("Physical Activity (minutes/day)", 0, 120, 30)
meals = st.selectbox("Do you eat meals at regular times?", ["Yes", "No"])
energy = st.slider("Energy Level (1-10)", 1, 10, 5)

# Scoring
score = 0

if wake_time <= 7:
    score += 15

if sleep_time <= 23 or sleep_time <= 2:
    score += 15

if screen_time <= 4:
    score += 15

if activity >= 30:
    score += 20

if meals == "Yes":
    score += 15

score += energy * 2

# Classification
if score >= 80:
    category = "Healthy ✅"
elif score >= 50:
    category = "Moderate ⚠️"
else:
    category = "Needs Improvement ❌"

# Output
st.subheader(f"Your Score: {score}/100")
st.subheader(f"Lifestyle Category: {category}")

# Suggestions
st.write("### 🧘 Ayurvedic Suggestions:")

if wake_time > 7:
    st.write("- Try waking up earlier (Brahma Muhurta)")

if sleep_time > 23:
    st.write("- Sleep before 11 PM for better recovery")

if screen_time > 4:
    st.write("- Reduce screen time to calm the mind")

if activity < 30:
    st.write("- Include yoga or walking daily")

if meals == "No":
    st.write("- Maintain regular meal timings")

if energy < 5:
    st.write("- Practice meditation and balanced diet")
