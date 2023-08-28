""" Imports des librairies """
import os
import pandas as pd
import sys
from scripts.models import MongoDBSingleton
from scripts.utils import ALL_COLL
from tableone import TableOne

""" Accession au singleton """
tmp_path = os.getcwd().split("MedicalAssistant_V2")[0]
target_path = os.path.join(tmp_path, 'MedicalAssistant_V2')
sys.path[:0] = [target_path]

""" Création d'une instance """
db = MongoDBSingleton.get_instance()

""" Importation des données """
data = pd.DataFrame(list(db.get_collection("heart").find({}, {'_id' : 0})))

""" Transformations """

for i in ALL_COLL :
    if i in ['HeartDisease', 'Smoking', 'AlcoholDrinking', 'Stroke', 'DiffWalking', 'Sex', 'PhysicalActivity', 'Asthma', 'KidneyDisease', 'SkinCancer'] :
        data[i] = [1 if x in ['Yes', 'Female'] else 0 for x in data[i].tolist()]
        data = data.drop(columns = i)
    elif i == 'AgeCategory' :
        for j in range(0, len(data['AgeCategory'])) :
            if data['AgeCategory'][j] in ['18-24','25-29'] : data['AgeCategory'][j] == '18-29'
            elif data['AgeCategory'][j] in ['30-34','35-39'] : data['AgeCategory'][j] == '30-39'
            elif data['AgeCategory'][j] in ['40-44','45-49'] : data['AgeCategory'][j] == '40-49'
            elif data['AgeCategory'][j] in ['50-54','55-59'] : data['AgeCategory'][j] == '50-59'
            elif data['AgeCategory'][j] in ['60-64','65-69'] : data['AgeCategory'][j] == '60-69'
            elif data['AgeCategory'][j] in ['70-74','75-79'] : data['AgeCategory'][j] == '70-79'
            else : continue
        for j in ['18-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80 or older'] :
            data[f'{i}_{"_".join(j.split(" "))}'] = [1 if x == j else 0 for x in data[i].tolist()]
        data = data.drop(columns = i)
    elif i == 'Race' :
        for j in ['American Indian/Alaskan Native', 'Asian', 'Black', 'Hispanic', 'Other', 'White'] :
            data[f'{i}_{"_".join(j.split(" "))}'] = [1 if x == j else 0 for x in data[i].tolist()]
        data = data.drop(columns = i)
    elif i == 'Diabetic' :
        for j in ['No', 'No, borderline diabetes', 'Yes', 'Yes (during pregnancy)'] :
            data[f'{i}_{"_".join(j.split(" "))}'] = [1 if x == j else 0 for x in data[i].tolist()]
        data = data.drop(columns = i)
    elif i == 'GenHealth' :
        for j in ['Excellent', 'Fair', 'Good', 'Poor', 'Very good'] :
            data[f'{i}_{"_".join(j.split(" "))}'] = [1 if x == j else 0 for x in data[i].tolist()]
        data = data.drop(columns = i)
    elif i in ['PhysicalHealth', 'MentalHealth'] :
        for j in range(0, len(data[i])) :
            if data[i][j] == 0 : data[i][j] == '0'
            elif data[i][j] in list(range(1, 30)) : data[i][j] == '1-29'
            elif data[i][j] == 30 : data[i][j] == '30'
            else : 
                continue
        for j in ['0', '1-29', '30'] :
            data[f'{i}_{"_".join(j.split(" "))}'] = [1 if x == j else 0 for x in data[i].tolist()]
        data = data.drop(columns = i)
    else : 
        continue

# data.to_excel("assets/transformed_data.xlsx")
