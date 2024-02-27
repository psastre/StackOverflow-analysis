import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\Pedro\Documents\Analisis de Datos\StackOverflow\survey_results_public.csv')

#####FIRST ANALYSIS: search the most popular study method
    #First we need to eliminate all the NaN data from LearnCode column

df = df.dropna(subset=['LearnCode'])

    #Create a new empty dataframe

df_first_analysis = pd.DataFrame()

    #Create all the columns with the conditions,  if the 'df' dataframe contains an especific text, add a row with 1, else 0

df_first_analysis['Books / Physical media'] = np.where(df['LearnCode'].str.contains('Books / Physical media'), 1, 0)
df_first_analysis['Coding Bootcamp'] = np.where(df['LearnCode'].str.contains('Coding Bootcamp'), 1, 0)
df_first_analysis['Colleague'] = np.where(df['LearnCode'].str.contains('Colleague'), 1, 0)
df_first_analysis['Friend or family member'] = np.where(df['LearnCode'].str.contains('Friend or family member'), 1, 0)
df_first_analysis['Hackathons (virtual or in-person)'] = np.where(df['LearnCode'].str.contains('Hackathons \(virtual or in-person\)'), 1, 0)

df_first_analysis['Online Courses or Certification'] = np.where(df['LearnCode'].str.contains('Online Courses or Certification'), 1, 0)
df_first_analysis['On the job training'] = np.where(df['LearnCode'].str.contains('On the job training'), 1, 0)
df_first_analysis['Other online resources (e.g., videos, blogs, forum)'] = np.where(df['LearnCode'].str.contains('Other online resources \(e.g., videos, blogs, forum\)'), 1, 0)
df_first_analysis['School (i.e., University, College, etc)'] = np.where(df['LearnCode'].str.contains('School \(i.e., University, College, etc\)'), 1, 0)


    # add all the rows from all the columns 
sum_per_column = np.sum(df_first_analysis, axis=0)

    # Make a bar graph that show the results, and you can see the most popular study method

sum_per_column.plot(kind='bar')


#####SECOND ANALYSIS: Correlation between job and master
    #Create a new empty dataframe
    #Create all the columns with the conditions,  if the 'df' dataframe contains an especific text, add a row with 1, else 0

df_second_analysis = pd.DataFrame()
df_second_analysis['Employed'] = np.where(df['Employment'].str.contains('Employed') , 1 , 0)
df_second_analysis['Education'] = np.where(df['EdLevel'].str.contains('Master') , 1 , 0)

    #To understand and see the correlation between this two columns I create a new column that will fill with 1 
    #if the two columns are equal, but this is wrong because it will not only take the rows that are in the two cases 1
    # also it will take the ones with 0
#df_second_analysis['Correlation'] = np.where(df_second_analysis['Employed']==df_second_analysis['Education'] , 1 , 0)

    #To correct that i create a new condition that will fill with 1 if the two columns are equal to 1.
df_second_analysis['Correlation'] = np.where((df_second_analysis['Employed']==1) & (df_second_analysis['Education']==1) , 1 , 0)

    #Once we have the "Correlation" column we can sum, and we can see all the personas that have Employment and Master

sum_per_column_second = np.sum(df_second_analysis , axis=0)

print(sum_per_column_second)

    # Make a bar graph that show the results, and you can see the correlation and comparation between al the column 

sum_per_column_second.plot(kind='bar')




