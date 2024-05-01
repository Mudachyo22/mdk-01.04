import pandas as pd
import numpy as np

df = pd.read_csv(r"E:\Programming\Python\mdk01.04\train.csv")
survived_passengers = df['Survived'].values
total_survived = np.sum(survived_passengers)

print(f"Общее количество выживших пассажиров: {total_survived}")