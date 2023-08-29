
data = {'Smoking': 'Yes',
 'AlcoholDrinking': 'Yes',
 'Stroke': 'Yes',
 'DiffWalking': 'Yes',
 'Sex': 'Female',
 'AgeCategory': '18-29',
 'Race': 'White',
 'Diabetic': 'Yes',
 'PhysicalActivity': 'Yes',
 'GenHealth': 'Very good',
 'Asthma': 'Yes',
 'KidneyDisease': 'Yes',
 'SkinCancer': 'Yes',
 'BMI': 50,
 'PhysicalHealth': 15,
 'MentalHealth': 15,
 'SleepTime': 8}

import os
tmp_path = os.getcwd().split("MEDICALASSISTANT_V2")[0]
target_path = os.path.join(tmp_path, 'MEDICALASSISTANT_V2')
import sys
sys.path[:0] = [target_path]
import streamlit as st
import pandas as pd
import numpy as np
# from scripts.utils import *
import time as t
from scripts.explore.dataPreprocessing import dataPreprocessing
import pandas as pd
from joblib import load


processed = dataPreprocessing(data)
model = load('scripts/machineLearning/knn_opti.joblib')
print(model.feature_names_in_)
