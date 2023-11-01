import pandas as pd
import os
currentDir = os.getcwd()
print("currentDir:", currentDir)

objects_path = "FinalProject/StartupData/funds.csv"

dataframe = pd.read_csv(objects_path)

print(dataframe.head())
print(dataframe.columns)