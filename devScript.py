""" Imports des librairies """
from tableone import TableOne
import os
import pandas as pd

""" Importation des données (fichier .csv) """
data = pd.read_csv(os.path.join("assets", "heart_2020_cleaned.csv"))

""" Séparation des données selon HeartDisease """
data_hd_yes = data[data['HeartDisease'].isin(['Yes'])]
data_hd_no = data[data['HeartDisease'].isin(['No'])]

""" Définition des types de colonnes """00
allcols = ['HeartDisease', 'BMI', 'Smoking', 'AlcoholDrinking', 
          'Stroke', 'PhysicalHealth', 'MentalHealth', 'DiffWalking', 
          'Sex', 'AgeCategory', 'Race', 'Diabetic', 'PhysicalActivity', 
          'GenHealth', 'SleepTime', 'Asthma', 'KidneyDisease', 'SkinCancer']

categorical = ['Smoking', 'AlcoholDrinking', 'Stroke', 
               'DiffWalking', 'Sex', 'AgeCategory', 'Race', 'Diabetic', 
               'PhysicalActivity', 'GenHealth', 'Asthma', 'KidneyDisease', 
               'SkinCancer']
numeric = ['BMI', 'PhysicalHealth', 'MentalHealth', 'SleepTime']

""" Réalisation préliminaire des tests """
mytable = TableOne(data, 
                   columns = allcols, 
                   categorical = categorical, 
                   groupby = ['HeartDisease'],
                   pval = True)

print(mytable.tabulate(tablefmt = "fancy_grid"))

""" Tests de normalité """
from scipy.stats import shapiro
import matplotlib.pyplot as plt

# Visuel
for i in numeric :
    plt.hist(data_hd_yes[i], edgecolor = 'black', bins = 50)
    plt.title(i)
    plt.show()
# Shapiro