
import streamlit as st
import joblib
import numpy as np

model = joblib.load("drug_screening_model.joblib")

st.title("🧪 AI-Based Drug Screening")

st.write(
    "This is a simulated educational drug-screening model. "
    "It predicts whether a compound is Active or Inactive."
)

molecular_weight = st.number_input("Molecular Weight")
binding_affinity = st.number_input("Binding Affinity")
solubility_score = st.number_input("Solubility Score")
toxicity_score = st.number_input("Toxicity Score")
feature_5 = st.number_input("Feature 5")
feature_6 = st.number_input("Feature 6")

if st.button("Predict"):

    input_data = np.array([[
        molecular_weight,
        binding_affinity,
        solubility_score,
        toxicity_score,
        feature_5,
        feature_6
    ]])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("🟢 Prediction: ACTIVE COMPOUND")
    else:
        st.error("🔴 Prediction: INACTIVE COMPOUND")
