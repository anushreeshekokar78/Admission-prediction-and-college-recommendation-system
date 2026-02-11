import streamlit as st
import numpy as np
import joblib
import matplotlib.pyplot as plt
from colleges import recommend_colleges

model = joblib.load("admission_model.pkl")

st.set_page_config(page_title="Admission Predictor", layout="centered")

st.title("🎓 Masters Admission Prediction System")
st.caption("Enter your academic details")

st.markdown("---")

# ---------- INPUT FORM ----------
st.subheader("📄 Academic Profile")

gre = st.text_input("GRE Score (out of 340)", "300", key="gre")
toefl = st.text_input("TOEFL Score (out of 120)", "100", key="toefl")
uni = st.text_input("University Rating (1–5)", "3", key="uni")
sop = st.text_input("SOP Strength (1–5)", "3", key="sop")
lor = st.text_input("LOR Strength (1–5)", "3", key="lor")
cgpa = st.text_input("CGPA (out of 10)", "8", key="cgpa")
research = st.radio("Research Experience", ["No", "Yes"], key="research")

# Safe conversion
try:
    gre = float(gre)
    toefl = float(toefl)
    uni = float(uni)
    sop = float(sop)
    lor = float(lor)
    cgpa = float(cgpa)
except:
    st.warning("⚠ Please enter valid numeric values.")
    st.stop()

research_val = 1 if research == "Yes" else 0

st.markdown("---")

# ---------- PREDICTION ----------
if st.button("🎯 Predict Admission Chance"):

    with st.spinner("Analyzing your profile..."):
        import time
        time.sleep(1)

    user_data = np.array([[gre, toefl, uni, sop, lor, cgpa, research_val]])

    chance = model.predict(user_data)[0]
    percent = round(chance * 100, 2)

    st.success(f"🎯 Admission Probability: {percent}%")
    st.progress(min(int(percent), 100))

    # Probability graph
    fig = plt.figure()
    plt.bar(["Admission Chance"], [percent])
    plt.ylim(0, 100)
    plt.title("Admission Probability (%)")
    st.pyplot(fig)

    # College recommendation
    tier, colleges = recommend_colleges(chance)
    st.subheader(tier)

    for c in colleges:
        st.write("✅", c)

    st.balloons()
