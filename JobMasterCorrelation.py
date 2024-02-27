import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(r'C:\Users\Pedro\Documents\Analisis de Datos\StackOverflow\survey_results_public.csv')

df_nuevo = pd.DataFrame()

df_nuevo['Employed'] = np.where(df['Employment'].str.contains('Employed') , 1 , 0)

df_nuevo['Education'] = np.where(df['EdLevel'].str.contains('Master') , 1 , 0)

df_nuevo['Correlation'] = np.where(df_nuevo['Employed']==df_nuevo['Education'] , 1 , 0)

df_nuevo['Correlation2'] = np.where((df_nuevo['Employed']==1) & (df_nuevo['Education']==1) , 1 , 0)

sum_df_nuevo = np.sum(df_nuevo , axis=0)

print(sum_df_nuevo)

sum_df_nuevo.plot(kind='bar')