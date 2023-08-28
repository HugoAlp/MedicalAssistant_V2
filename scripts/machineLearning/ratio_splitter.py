import pandas as pd

def ratio_splitter(df, y_ratio):
    dftrue = df[df["HeartDisease"]==1]
    dffalse = df[df["HeartDisease"]==0]

    ratio_true = len(dftrue) / len(dffalse)
    ratio_false = 1 - ratio_true

    nb_target_true = 