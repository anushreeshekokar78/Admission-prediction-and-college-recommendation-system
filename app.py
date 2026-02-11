import streamlit as st

st.set_page_config(page_title="Admission Predictor", layout="centered")

st.title("🎓 Graduate Admission Prediction System")

st.caption("Machine Learning powered admission guidance")

st.markdown("---")

# ----- Hero Section -----
st.subheader("Welcome 👋")

st.write("""
Predict your Masters admission probability and get university recommendations
based on your academic profile.
""")

st.markdown("### 🚀 What can you do here?")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📊 Predict", "Admission Chance")

with col2:
    st.metric("🎯 Recommend", "Universities")

with col3:
    st.metric("📈 Visualize", "Results")

st.markdown("---")

# ----- How it works -----
st.header("⚙ How It Works")

c1, c2, c3 = st.columns(3)

with c1:
    st.success("📝 Enter Scores")

with c2:
    st.success("🤖 ML Prediction")

with c3:
    st.success("🏫 College Suggestion")

st.markdown("---")

# ----- Tech Stack Cards -----
st.header("🛠 Tech Stack")

t1, t2, t3 = st.columns(3)

with t1:
    st.info("🐍 Python")

with t2:
    st.info("🧠 Machine Learning")

with t3:
    st.info("🌐 Streamlit")

st.markdown("---")

st.success("👉 Use the sidebar → **Predict** to get started!")
