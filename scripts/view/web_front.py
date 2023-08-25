import os
tmp_path = os.getcwd().split("MEDICALASSISTANT_V2")[0]
target_path = os.path.join(tmp_path, 'MEDICALASSISTANT_V2')
import sys
sys.path[:0] = [target_path]
import streamlit as st
import pandas as pd
import ydata_profiling
from streamlit_pandas_profiling import st_profile_report
import numpy as np
from scripts.utils import *
import seaborn as sns
import matplotlib.pyplot as plt

st.title('Databradors du futur')

form = st.form("my_form")
# # Using object notation
# add_selectbox = st.sidebar.selectbox(
#     "How would you like to be contacted?",
#     ("Email", "Home phone", "Mobile phone")
# )
# age = st.sidebar.slider('How old are you?', 0, 130, 25)
# st.write("I'm ", age, 'years old')
if "visibility" not in st.session_state:
    st.session_state.horizontal = True
with st.sidebar.form(key ='Form1'):
    R_heartDisease = st.radio("Heart disease",('Off','Yes', 'No'),horizontal=st.session_state.horizontal),
    R_smoking = st.radio("Smoking",('Off','Yes', 'No'),horizontal=st.session_state.horizontal),
    R_AlcoholDrinking = st.radio("Alcohol drinking",('Off','Yes', 'No'),horizontal=st.session_state.horizontal),
    R_Stroke = st.radio("Stroke",('Off','Yes', 'No'),horizontal=st.session_state.horizontal),
    R_DiffWalking = st.radio("Walking difficulty",('Off','Yes', 'No'),horizontal=st.session_state.horizontal),
    R_Sex = st.radio("Sex",('Off','Female', 'Male'),horizontal=st.session_state.horizontal),
    SB_AgeCategory = st.selectbox("Age Category",('Off','18-24','25-29', '30-34','35-39','40-44', '45-49', '50-54','55-59', '60-64', '65-69', '70-74', '75-79', '80 or older')),
    SB_Race = st.selectbox("Race",('Off','White', 'Black', 'Asian', 'American Indian/Alaskan Native', 'Other', 'Hispanic')),
    SB_Diabetic = st.selectbox("Diabetic",('Off','Yes', 'No', 'No, borderline diabetes', 'Yes (during pregnancy)')),
    R_PhysicalActivity = st.radio("Physical activity",('Off','Yes', 'No'),horizontal=st.session_state.horizontal),
    SB_GenHealth= st.selectbox("General health",('Off','Very good', 'Fair', 'Good', 'Poor', 'Excellent')),
    R_Asthma = st.radio("Asthma",('Off','Yes', 'No'),horizontal=st.session_state.horizontal),
    R_KidneyDisease = st.radio("Kidney disease",('Off','Yes', 'No'),horizontal=st.session_state.horizontal),
    R_SkinCancer = st.radio("Skin cancer",('Off','Yes', 'No'),horizontal=st.session_state.horizontal),
    S_PhysicalHealth = st.slider('Physical health', 0, 30, 15),
    S_MentalHealth = st.slider('Mental health', 0, 30, 15),
    S_BMI = st.slider('Mental health', 1, 100, 50),

    st.form_submit_button("Submit")

df = pd.read_csv("assets\heart_2020_light.csv")

plots = []
for column in df.columns:
    extractedData = df[column]
    if column in NUM_COLUMNS:
        plot = plt.hist(extractedData, stat = "count", color = "indianred", alpha = 0.5)
        plot.set(ylabel = 'Count', title = f'{COLNAMES_DICT[column]}')

        if column == "BMI" : plot.set(xlabel = 'Index')
        elif column == "SleepTime" : plot.set(xlabel = 'Hours')
        else : plot.set(xlabel = 'Days since')

        plots.append(plot)



# pr = df.profile_report()
# st_profile_report(pr)

# python -m streamlit run scripts/view/web_front.py

