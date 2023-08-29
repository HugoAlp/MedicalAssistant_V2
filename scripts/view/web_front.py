import os
tmp_path = os.getcwd().split("MEDICALASSISTANT_V2")[0]
target_path = os.path.join(tmp_path, 'MEDICALASSISTANT_V2')
import sys
sys.path[:0] = [target_path]
import streamlit as st
import pandas as pd
import numpy as np
from scripts.utils import *
import time as t
from pprint import pprint
from scripts.explore.dataPreprocessing import dataPreprocessing
#import ydata_profiling
#from streamlit_pandas_profiling import st_profile_report
#import seaborn as sns
#import matplotlib.pyplot as plt
res_form ={}
elementFormNames= {0:'R_heartDisease',1:'R_smoking',3:'R_AlcoholDrinking',2:'R_Stroke',3:'R_DiffWalking',4:'R_Sex',5:'SB_AgeCategory',
                   6:'SB_Race',7:'SB_Diabetic',8:'R_PhysicalActivity',9:'SB_GenHealth',10:'R_Asthma',11:'R_KidneyDisease',12:'R_SkinCancer',
                   13:'S_PhysicalHealth',14:'S_MentalHealth',15:'S_BMI'}
st.title('Databradors du futur')

form = st.form("my_form",clear_on_submit =True)


with st.form(key ='Form1'):
    st.session_state.R_smoking = st.radio("Smoking",( 'Yes', 'No')  ),
    st.session_state.R_AlcoholDrinking = st.radio("Alcohol drinking",( 'Yes', 'No')  ),
    st.session_state.R_Stroke = st.radio("Stroke",( 'Yes', 'No')  ),
    st.session_state.R_DiffWalking = st.radio("Walking difficulty",( 'Yes', 'No')  ),
    st.session_state.R_Sex = st.radio("Sex",('Female', 'Male')  ),
    st.session_state.SB_AgeCategory = st.selectbox("Age Category",('18-29', '30-39','40-49', '50-59', '60-69', '70-79', '80 or older')),
    st.session_state.SB_Race = st.selectbox("Race",( 'White', 'Black', 'Asian', 'American Indian/Alaskan Native', 'Other', 'Hispanic')),
    st.session_state.SB_Diabetic = st.selectbox("Diabetic",('Yes', 'No', 'No, borderline diabetes', 'Yes (during pregnancy)')),
    st.session_state.R_PhysicalActivity = st.radio("Physical activity",( 'Yes', 'No')  ),
    st.session_state.SB_GenHealth= st.selectbox("General health",('Very good', 'Fair', 'Good', 'Poor', 'Excellent')),
    st.session_state.R_Asthma = st.radio("Asthma",('Yes', 'No')  ),
    st.session_state.R_KidneyDisease = st.radio("Kidney disease",( 'Yes', 'No')  ),
    st.session_state.R_SkinCancer = st.radio("Skin cancer",('Yes', 'No')  ),
    st.session_state.S_PhysicalHealth = st.slider('Physical health', 0, 30, 15),
    st.session_state.S_MentalHealth = st.slider('Mental health', 0, 30, 15),
    st.session_state.S_BMI = st.slider('BMI', 1, 100, 50),
    st.session_state.S_Sleep = st.slider('Sleeptime', 1, 24, 8),
    sub = st.form_submit_button("Submit")
# if sub:
#     tut=st.session_state

#     st.write(tut)
#     i=0
result = {'Smoking':  st.session_state.R_smoking[0],
        'AlcoholDrinking': st.session_state.R_AlcoholDrinking[0],
        'Stroke': st.session_state.R_Stroke[0],
        'DiffWalking': st.session_state.R_DiffWalking[0],
        'Sex': st.session_state.R_Sex[0],
        'AgeCategory': st.session_state.SB_AgeCategory[0],
        'Race': st.session_state.SB_Race[0],
        'Diabetic':  st.session_state.SB_Diabetic[0],
        'PhysicalActivity': st.session_state.R_PhysicalActivity[0],
        'GenHealth': st.session_state.SB_GenHealth[0],
        'Asthma': st.session_state.R_Asthma[0],
        'KidneyDisease': st.session_state.R_KidneyDisease[0],
        'SkinCancer': st.session_state.R_SkinCancer[0],
        'BMI':st.session_state.S_BMI[0],
        'PhysicalHealth':st.session_state.S_PhysicalHealth[0],
        'MentalHealth':st.session_state.S_MentalHealth[0],
        'SleepTime':st.session_state.S_Sleep[0]}
pprint(result, sort_dicts=False)

    #for i in range (0 ,len(elementFormNames)):
        # val= st.write(elementFormNames[list(elementFormNames.keys())[i]])
        # st.write(val)
        # res_form = {ALL_COLL[i],val}
        # i=i+1

        # with st.spinner('Wait for it...'):
        #     t.sleep(5)
        # st.success('Done!')


df = pd.read_csv("assets\heart_2020_light.csv")

# plots = []
# for column in df.columns:
#     extractedData = df[column]
#     if column in NUM_COLUMNS:
#         plot = plt.hist(extractedData, stat = "count", color = "indianred", alpha = 0.5)
#         plot.set(ylabel = 'Count', title = f'{COLNAMES_DICT[column]}')

#         if column == "BMI" : plot.set(xlabel = 'Index')
#         elif column == "SleepTime" : plot.set(xlabel = 'Hours')
#         else : plot.set(xlabel = 'Days since')

#         plots.append(plot)



# pr = df.profile_report()
# st_profile_report(pr)

# python -m streamlit run scripts/view/web_front.py

