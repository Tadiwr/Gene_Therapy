# This file contains code for the entry page when the streamlit app is run
# When you visit the website streamlit cloud will run this app first


from sys import path

# for streamlit to recognise the existence of python modules defined 
# there is need to need to add then to the system path
 
path.append("./models/X_model.py")
path.append("./transform_data.py")

import streamlit as st
import joblib
from models.X_model import XModel
from transform_data import transformData

reg_model = joblib.load("./models/logistic-reg.joblib")

# Create an instance of the XModel class
x_model = XModel()


# Possible options that a user can select

statuses = ['Active, not recruiting', 'Recruiting', 'Completed', 'Terminated',
       'Unknown status']

phases = ['Phase 1/2', 'Phase 3', 'Phase 1', 'Phase 2', 'Phase 2/3']

areas = ['Ophthalmology', 'Hematology', 'Neurology', 'Musculoskeletal',
       'Oncology', 'Pulmonary', 'Metabolic', 'Autoimmune', 'Virology',
       'Cardiovascular']

routes = ['Subretinal', 'Intravenous', 'Intracranial', 'Intramuscular',
       'Intraparotidal', 'Intranasal', 'Intraarticular', 'Intravitreal',
       'Intracoronary', 'Subfoveal', 'Intrathecal']

drugs = ['SPK-7001', 'AMT-061', 'BIIB-111', 'AMT-090', 'VYAADC-01',
       'Luxturna', 'SPK-9001', 'A-001', 'CERE-120', 'GT-AADC ',
       'BIIB-112', 'AAV1-gammasarcoglycan', 'A-00X', 'AAV-CFTR',
       'rAAV1-CMV- hGAA', 'rAAV2-CB- hRPE65', 'AAV2CUhCLN2', 'NLX-P101',
       'ART-102', 'AGTC-0106', 'BIIB-087', 'scAAV2- P1ND4v2',
       'AAV2/8-HLP- FVIII-V3', 'rAAV1-PG9DP', 'Mydicar', 'SB-525',
       'DTX-101', 'RGX-314', 'rAAV 2/2. hRPE65p. hRPE65', 'AT-GTX-501',
       'Valrox', 'rAAV2-CBSB- hRPE65', 'AMT-110', 'AAV2/8.TBG.hARSB',
       'CERE-110', 'rAAV2.REP1', 'ADVM-043', 'rAAV1.CMV.huFollistatin344',
       'MYO-102', 'Zolgensma', 'Glybera', 'GS-010', 'MYO-101']

vectors = ['AAV2', 'AAV5', 'AAV1', 'AAV8', 'AAV2/5', 'AAV2/8', 'AAVrh10',
       'scAAV9', 'AAV9', 'SPK100', 'AAVrh74']

st.write("# Understanding Gene Therapy through AI 🤖")
"Download link for nature media dataset that powers this model: [Download Dataset!](https://media.nature.com/original/magazine-assets/d41573-021-00017-7/18790666)"

"---------------------------------------------------------"

"# 🌞 Select the variables "
"Select the different variables that the experiment whose efficacy you want to predict!"

x_model.area =  st.radio(
    label="Therapitic Area",
    options=areas,
)

"# Administration Therapuetic Route"
x_model.route =  st.selectbox(
    label="Route",
    options=routes
)

"# Select the drug that will be used in the trial"

x_model.drug_id = st.selectbox(
    label="Drug (ID)",
    options=drugs
)

"# Points"
x_model.points = st.number_input(
    label="Points",
    step=1
)

"# Vector that will be used"
x_model.vector = st.selectbox(
    label="Vector",
    options=vectors
)

"# Safety Met or Not"

x_model.safety_met = st.radio(
    label="Was Safety Met?",
    options=["Yes", "No"]
)


"# Phase of the trial"
x_model.phase = st.selectbox(
    label="Phase of trial",
    options=phases
)

"# Status of the trial"
x_model.status = st.selectbox(
    label="Select the status",
    options= statuses
)

"# Year in which trial will be completed"
x_model.completion = st.number_input(
    label="Year",
    min_value=2000,
    max_value=2050,
    step=1
)

def predict_on_click():
    X = transformData(x_model)

    prediction = reg_model.predict(X)[0]
    des = ""
    print("The prediction is: ", prediction)

    with st.sidebar:
        if prediction == 1:
            prediction = "Yes"
            des = "be successful"
            st.success(f"Predicted result is: {prediction}, your trial will , {des}")
        elif prediction == 0:
            prediction = "No"
            des = "will not be successful"
            st.warning(f"Predicted result is: {prediction}, your trial will {des}")

with st.sidebar:

    # Predict your Trial
    st.button(
        label="Predict!",
        type="primary",
        on_click=predict_on_click
    )

""