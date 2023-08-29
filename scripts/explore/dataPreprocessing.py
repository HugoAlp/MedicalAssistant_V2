def dataPreprocessing() :

    """ Positionnement du curseur d'importation des librairies internes au projet """
    import os
    import pandas as pd
    import sys
    tmp_path = os.getcwd().split("MedicalAssistant_V2")[0]
    target_path = os.path.join(tmp_path, 'MedicalAssistant_V2')
    sys.path[:0] = [target_path]

    """ Imports des librairies """
    from scripts.models import MongoDBSingleton
    from scripts.utils import ALL_COLL
    from sklearn.preprocessing import MinMaxScaler

    """ Création d'une instance """
    db = MongoDBSingleton.get_instance()

    """ Importation des données """
    data = pd.DataFrame(list(db.get_collection("heart").find({}, {'_id' : 0})))

    """ Transformations """
    for i in ALL_COLL :
        print(i)
        if i in ['HeartDisease', 'Smoking', 'AlcoholDrinking', 'Stroke', 'DiffWalking', 'Sex', 'PhysicalActivity', 'Asthma', 'KidneyDisease', 'SkinCancer'] :
            data[i] = [1 if x in ['Yes', 'Male'] else 0 for x in data[i].tolist()]
        elif i in ['SleepTime', 'BMI']:
            minmaxscaler = MinMaxScaler()
            data[i] = minmaxscaler.fit_transform(data[[i]])
        elif i == 'AgeCategory' :
            dict_remplace = {'18-24':'18-29','25-29':'18-29',
                             '30-34':'30-39','35-39':'30-39',
                             '40-44':'40-49','45-49':'40-49',
                             '50-54':'50-59','55-59':'50-59',
                             '60-64':'60-69','65-69':'60-69',
                             '70-74':'70-79','75-79':'70-79'}
            data['AgeCategory'] = data['AgeCategory'].map(dict_remplace)
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
            data[i] = data[i].map(dict_remplace)
            for j in ['0', '1-29', '30'] :
                print(j)
                data[f'{i}_{"_".join(j.split(" "))}'] = [1 if x == j else 0 for x in data[i].tolist()]
            data = data.drop(columns = i)
        else : continue

    return(data)


if __name__ == '__main__':
    data = dataPreprocessing()