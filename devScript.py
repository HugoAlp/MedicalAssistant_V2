""" Imports des librairies """
from tableone import TableOne
import os
import pandas as pd

""" 
    Notes :
    
    - Variables catégorielles :
        On réalise un Chi2.
        Condition d'application, au  moins 5 individus dans chaque groupe (ok).

    - Variables numériques :
        On réalise un t-test.
        Conditions d'application, indépendance des deux groupes (ok), échantillon aléatoire (pas possible), normalité (TCL la suppose) visuelle (pas ok donc transfo données), homoscédasticité.

"""


""" Importation des données (fichier .csv) """
data = pd.read_csv(os.path.join("assets", "heart_2020_cleaned.csv"))

""" Séparation des données selon HeartDisease """
data_hd_yes = data[data['HeartDisease'].isin(['Yes'])]
data_hd_no = data[data['HeartDisease'].isin(['No'])]

""" Définition des types de colonnes """
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

# Visuel car grand nombre d'échantillons suppose la normalité (Théorème Central Limite)
# fig, axs = plt.subplots(2, 2)
# axs[0, 0].hist(data_hd_yes['BMI'], edgecolor = 'black', bins = 50)
# axs[0, 0].set_title('BMI')
# axs[0, 1].hist(data_hd_yes['PhysicalHealth'], edgecolor = 'black', bins = 50)
# axs[0, 1].set_title('PhysicalHealth')
# axs[1, 0].hist(data_hd_yes['MentalHealth'], edgecolor = 'black', bins = 50)
# axs[1, 0].set_title('MentalHealth')
# axs[1, 1].hist(data_hd_yes['SleepTime'], edgecolor = 'black', bins = 50)
# axs[1, 1].set_title('SleepTime')
# plt.show()

# fig, axs = plt.subplots(2, 2)
# axs[0, 0].hist(data_hd_no['BMI'], edgecolor = 'black', bins = 50)
# axs[0, 0].set_title('BMI')
# axs[0, 1].hist(data_hd_no['PhysicalHealth'], edgecolor = 'black', bins = 50)
# axs[0, 1].set_title('PhysicalHealth')
# axs[1, 0].hist(data_hd_no['MentalHealth'], edgecolor = 'black', bins = 50)
# axs[1, 0].set_title('MentalHealth')
# axs[1, 1].hist(data_hd_no['SleepTime'], edgecolor = 'black', bins = 50)
# axs[1, 1].set_title('SleepTime')
# plt.show()

# """ Ajustement des variables PhysicalHealth et MentalHealth """
# data['PhysicalHealth_0'] = [1 if x == 0 else 0 for x in data['PhysicalHealth'].tolist()]
# data['PhysicalHealth_1_29'] = [1 if x > 0 and x < 30 else 0 for x in data['PhysicalHealth'].tolist()]
# data['PhysicalHealth_30'] = [1 if x == 30 else 0 for x in data['PhysicalHealth'].tolist()]
# 
# data['MentalHealth_0'] = [1 if x == 0 else 0 for x in data['MentalHealth'].tolist()]
# data['MentalHealth_1_29'] = [1 if x > 0 and x < 30 else 0 for x in data['MentalHealth'].tolist()]
# data['MentalHealth_30'] = [1 if x == 30 else 0 for x in data['MentalHealth'].tolist()]
# 
# data = data.drop(columns = ["PhysicalHealth", "MentalHealth"])
# 
# """ Nouvelle séparation des données selon HeartDisease """
# data_hd_yes = data[data['HeartDisease'].isin(['Yes'])]
# data_hd_no = data[data['HeartDisease'].isin(['No'])]
# 
# allcols = ['HeartDisease', 'BMI', 'Smoking', 'AlcoholDrinking', 
#           'Stroke', 'DiffWalking', 'Sex', 'AgeCategory', 'Race', 
#           'Diabetic', 'PhysicalActivity', 'GenHealth', 'SleepTime', 
#           'Asthma', 'KidneyDisease', 'SkinCancer', 'PhysicalHealth_0', 
#           'PhysicalHealth_1_29', 'PhysicalHealth_30', 'MentalHealth_0', 
#           'MentalHealth_1_29', 'MentalHealth_30']
# 
# categorical = ['Smoking', 'AlcoholDrinking', 'Stroke', 
#                'DiffWalking', 'Sex', 'AgeCategory', 'Race', 'Diabetic', 
#                'PhysicalActivity', 'GenHealth', 'Asthma', 'KidneyDisease', 
#                'SkinCancer', 'PhysicalHealth_0', 'PhysicalHealth_1_29', 
#                'PhysicalHealth_30', 'MentalHealth_0', 'MentalHealth_1_29', 
#                'MentalHealth_30']
# 
# numeric = ['BMI', 'SleepTime']
# 
# """ Réalisation préliminaire des tests """
# mytable = TableOne(data,
#                    columns = allcols,
#                    categorical = categorical,
#                    groupby = ['HeartDisease'],
#                    pval = True, missing = False, overall = False)
# 
# print(mytable.tabulate(tablefmt = "fancy_grid"))

""" Test de l'homogénéité des variances (on s'en affranchi car groupes non aléatoires) """
from scipy.stats import bartlett

bartlett(data_hd_yes["BMI"], data_hd_no["BMI"]) # Pas de différence significative
bartlett(data_hd_yes["SleepTime"], data_hd_no["SleepTime"])

""" One Hot Encoding """
categorical = ['HeartDisease', 'Smoking', 'AlcoholDrinking', 'Stroke', 
               'DiffWalking', 'Sex', 'AgeCategory', 'Race', 'Diabetic', 
               'PhysicalActivity', 'GenHealth', 'Asthma', 'KidneyDisease', 
               'SkinCancer']

for i in categorical :
    if i in ["HeartDisease", "Smoking", "AlcoholDrinking", "Stroke", "DiffWalking", "Sex", "PhysicalActivity", "Asthma", "KidneyDisease", "SkinCancer"] :
        data[i] = [1 if x in ['Yes', 'Female'] else 0 for x in data[i].tolist()]
    elif i == 'AgeCategory' :
        for j in range(0, len(data["AgeCategory"])) :
            if data["AgeCategory"][j] in ["18-24","25-29"] : data["AgeCategory"][j] == "18-29"
            elif data["AgeCategory"][j] in ["30-34","35-39"] : data["AgeCategory"][j] == "30-39"
            elif data["AgeCategory"][j] in ["40-44","45-49"] : data["AgeCategory"][j] == "40-49"
            elif data["AgeCategory"][j] in ["50-54","55-59"] : data["AgeCategory"][j] == "50-59"
            elif data["AgeCategory"][j] in ["60-64","65-69"] : data["AgeCategory"][j] == "60-69"
            elif data["AgeCategory"][j] in ["70-74","75-79"] : data["AgeCategory"][j] == "70-79"
        for j in ["18-29", "30-39", "40-49", "50-59", "60-69", "70-79", "80 or older"] :
            data[f'{i}_{"_".join(j.split(" "))}'] = [1 if x == j else 0 for x in data[i].tolist()]
    elif i == 'Race' :
        for j in ['American Indian/Alaskan Native', 'Asian', 'Black', 'Hispanic', 'Other', 'White'] :
            data[f'{i}_{"_".join(j.split(" "))}'] = [1 if x == j else 0 for x in data[i].tolist()]
    elif i == 'Diabetic' :
        for j in ['No', 'No, borderline diabetes', 'Yes', 'Yes (during pregnancy)'] :
            data[f'{i}_{"_".join(j.split(" "))}'] = [1 if x == j else 0 for x in data[i].tolist()]
    elif i == 'GenHealth' :
        for j in ['Excellent', 'Fair', 'Good', 'Poor', 'Very good'] :
            data[f'{i}_{"_".join(j.split(" "))}'] = [1 if x == j else 0 for x in data[i].tolist()]
data.drop(columns = categorical)    

# data.groupby(['HeartDisease']).size()
    


