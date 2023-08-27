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
    if i in ["HeartDisease", "Smoking", "AlcoholDrinking", "Stroke", "DiffWalking", "PhysicalActivity", "Asthma", "KidneyDisease", "SkinCancer"] :
        data[f'{i}_yes'] = [1 if x == 'Yes' else 0 for x in data[i].tolist()]
        data[f'{i}_no'] = [1 if x == 'Yes' else 0 for x in data[i].tolist()]
    elif i == 'Sex' :
        pass
    elif i == 'AgeCategory' :
        pass
    elif i == 'Race' :
        pass
    elif i == 'Diabetic' :
        pass
    elif i == 'GenHealth' :
        pass
    else :
        pass

data['PhysicalHealth_0'] = [1 if x == 0 else 0 for x in data['PhysicalHealth'].tolist()]
data['PhysicalHealth_1_29'] = [1 if x > 0 and x < 30 else 0 for x in data['PhysicalHealth'].tolist()]
data['PhysicalHealth_30'] = [1 if x == 30 else 0 for x in data['PhysicalHealth'].tolist()]

data['MentalHealth_0'] = [1 if x == 0 else 0 for x in data['MentalHealth'].tolist()]
data['MentalHealth_1_29'] = [1 if x > 0 and x < 30 else 0 for x in data['MentalHealth'].tolist()]
data['MentalHealth_30'] = [1 if x == 30 else 0 for x in data['MentalHealth'].tolist()]



from sklearn.preprocessing import OneHotEncoder
X = [['Yes', 1], ['No', 0]]

np.array(data['HeartDisease']).OneHotEncoder()


one_hot_encoded_data = pd.get_dummies(data, columns = ['HeartDisease'])
print(one_hot_encoded_data)