""" Importation des librairies """
from scripts.explore.dataPreprocessing import dataPreprocessing
from sklearn.model_selection import StratifiedShuffleSplit

""" Importation des données """
data = dataPreprocessing()

""" Définition des features et de la target """
features = data.drop(columns = ['HeartDisease'], axis = 1)
target = data['HeartDisease']

""" Split """
from sklearn.model_selection import StratifiedShuffleSplit

sss = StratifiedShuffleSplit(n_splits = 1, test_size = 0.2, random_state = 29)
for i, (train_index, test_index) in enumerate(sss.split(features, target)) : sample_indices = test_index.tolist()
features_sample = features.iloc[sample_indices]
target_sample = target.iloc[sample_indices]






for train_index, test_index in sss.split(features, target):
    X_train, X_test = features[train_index], features[test_index]
    y_train, y_test = target[train_index], target[test_index]
    # rf.fit(X_train, y_train)
    # pred = rf.predict(X_test)
    # scores.append(accuracy_score(y_test, pred))

for train_index in sss.split(features, target):
    print(train_index)


target_sample.value_counts()