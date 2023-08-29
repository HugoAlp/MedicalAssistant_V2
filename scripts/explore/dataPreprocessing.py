def dataPreprocessing() :

    """ Imports des librairies """
    import os
    import pandas as pd
    import sys

    """ - """
    tmp_path = os.getcwd().split("MedicalAssistant_V2")[0]
    target_path = os.path.join(tmp_path, 'MedicalAssistant_V2')
    sys.path[:0] = [target_path]

    """ Imports des librairies """
    from scripts.models import MongoDBSingleton
    from scripts.utils import ALL_COLL
    
    """ Création d'une instance """
    db = MongoDBSingleton.get_instance()

    """ Importation des données """
    data = pd.DataFrame(list(db.get_collection("heart").find({}, {'_id' : 0})))

    """ Transformations """
    for i in ALL_COLL :
        print(i)
        if i in ['HeartDisease', 'Smoking', 'AlcoholDrinking', 'Stroke', 'DiffWalking', 'Sex', 'PhysicalActivity', 'Asthma', 'KidneyDisease', 'SkinCancer'] :
            data[i] = [1 if x in ['Yes', 'Male'] else 0 for x in data[i].tolist()]
        elif i == 'AgeCategory' :
            dict_remplace = {'18-24':'18-29','25-29':'18-29',
                             '30-34':'30-39','35-39':'30-39',
                             '40-44':'40-49','45-49':'40-49',
                             '50-54':'50-59','55-59':'50-59',
                             '60-64':'60-69','65-69':'60-69',
                             '70-74':'70-79','75-79':'70-79'}
            data['AgeCategory'].map(dict_remplace)

            # for j in range(0, len(data['AgeCategory'])) :
                # if not j%20000: print(j)
                

                # if data.loc[j,'AgeCategory'] in ['18-24','25-29'] : data.loc[j,'AgeCategory'] = '18-29'
                # elif data.loc[j,'AgeCategory'] in ['30-34','35-39'] : data.loc[j,'AgeCategory'] = '30-39'
                # elif data.loc[j,'AgeCategory'] in ['40-44','45-49'] : data.loc[j,'AgeCategory'] = '40-49'
                # elif data.loc[j,'AgeCategory'] in ['50-54','55-59'] : data.loc[j,'AgeCategory'] = '50-59'
                # elif data.loc[j,'AgeCategory'] in ['60-64','65-69'] : data.loc[j,'AgeCategory'] = '60-69'
                # elif data.loc[j,'AgeCategory'] in ['70-74','75-79'] : data.loc[j,'AgeCategory'] = '70-79'
                # else : continue
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
            keys = list(range(1,30))
            vals = ['1-29']*29
            dict_remplace = dict(zip(keys, vals))
            dict_remplace[0] = '0'
            dict_remplace[30] = '30'
            data[i].map(dict_remplace)
            # for j in range(0, len(data[i])) :
            #     if data.loc[j, i] == 0 : data.loc[j, i] = '0'
            #     elif data.loc[j, i] in list(range(1, 30)) : data.loc[j, i] = '1-29'
            #     elif data.loc[j, i] == 30 : data.loc[j, i] = '30'
            #     else : continue
            for j in ['0', '1-29', '30'] :
                print(j)
                data[f'{i}_{"_".join(j.split(" "))}'] = [1 if x == j else 0 for x in data[i].tolist()]
            data = data.drop(columns = i)
        else : continue

    return(data)


if __name__ == '__main__':
    data = dataPreprocessing()