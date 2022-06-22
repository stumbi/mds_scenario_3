import pandas as pd
import numpy as np
import os

# function to read all data of a patient in a dataframe or array to make work easier
def read_data(patient_path):

    # make list of modalities and their paths
    modality_list = os.listdir(patient_path)

    modality_frames = []

    # iterate over modalities and create dataframe for each one
    for modality in modality_list:
        modality_frames.append(pd.read_csv(patient_path + '/' + modality, skiprows=1, names=[modality[:-4]]))
    # concat dataframes
    df = pd.concat(modality_frames, axis=1)

    return df

df = read_data('data/Exercises_SS22/sleeplab_dataset/sleep_lab_data/patient 29, male, 7 years')

print(df)

df.to_csv('/Users/manuel/Desktop/test.csv')
