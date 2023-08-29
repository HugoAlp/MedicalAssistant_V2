""" Importation des librairies """
from scripts.explore.dataPreprocessing import dataPreprocessing
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np
from sklearn.model_selection import StratifiedKFold,StratifiedShuffleSplit

""" Importation des données """
data = pd.read_csv('assets\nouv_transformed-no_index.csv')

"""Définition de X et y"""
X = data.drop(columns = ['HeartDisease'])
y = data['HeartDisease']

skf1 = StratifiedKFold(n_splits=5,shuffle=True, random_state=24)
skf1.get_n_splits(X, y)


sss = StratifiedShuffleSplit(n_splits = 1, test_size = 0.2, random_state = 29)

for i, (train_index, test_index) in enumerate(sss.split(X, y)) : tata = test_index.tolist()

reglog = LogisticRegression(penalty=None).fit(X,y)