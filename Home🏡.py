import streamlit as st
import joblib

model = joblib.load("./models/logistic-reg.joblib")


areas = ['Ophthalmology', 'Hematology', 'Neurology', 'Musculoskeletal',
       'Oncology', 'Pulmonary', 'Metabolic', 'Autoimmune', 'Virology',
       'Cardiovascular']


st.write("# Understanding Gene Therapy through AI 🤖")

"---------------------------------------------------------"

"# 🌞 Select the variables "
"Select the different variables that the experiment whose efficacy you want to predict!"

st.radio(
    label="Therapitic Area",
    options=areas,
)

