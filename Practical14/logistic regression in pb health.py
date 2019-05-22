#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 09:08:17 2019

@author: jefft
"""

import os
os.chdir('/Users/jefft/Desktop/ZJE/IBI(local)/git_repository/IBI1_2018-19/Practical14')
import pandas as pd
df = pd.read_excel('Final_Fluview_Practical_dataset.xlsx')
import statsmodels.api as sm
import statsmodels.formula.api as smf

df.info()
df.head(5) #read first five lines
df_regress = df[['Virus Strain','Age','Gender','Hospitalized?','Swine Contact?','Attended Agricultural Event?']]
df_regress.head(5)
len(df_regress[df_regress.isna().any(axis=1)]) # there are 3 missing values
#df_regress.isna() produce a df with T/F, where T represent NA values (None, NaN both included)

df_regress = df_regress.dropna() #remove NaN values
len(df_regress[df_regress.isna().any(axis=1)]) #confirm that

for column in df_regress:
    print(column, df_regress[column].unique()) #find the set of values that appear across each column - "factors"

#==================categorical value subsitutions==============================
df_regress['Age'] = df_regress['Age'].map({'<18 Years':0, '>=18 Years':1})
print(df_regress['Age'].unique()) # now we only have 0 & 1 factors
"""
Age ['<18 Years' '>=18 Years']
Gender ['Male' 'Female' 'male' 'female']
Hospitalized? ['Yes' 'No' 'no' 'yes']
Swine Contact? ['No' 'Yes' 'yes' 'no']
Attended Agricultural Event? ['No' 'Yes' 'yes' 'no']
Virus Strain ['Influenza A H3N2v' 'Influenza A H1N1v' 'Influenza A H1N2v' 'Influenza A H7N2']
"""
df_regress['Gender'] = df_regress['Gender'].map({'Male':0,'male':0,'Female':1,'female':1})
print(df_regress['Gender'].unique())
df_regress['Hospitalized?'] = df_regress['Hospitalized?'].map({'Yes':1,'yes':1,'no':0,'No':0})
df_regress['Swine Contact?'] = df_regress['Swine Contact?'].map({'No':0,'no':0,'yes':1,'Yes':1})
df_regress['Attended Agricultural Event?'] = df_regress['Attended Agricultural Event?'].map({'No':0,'no':0,'yes':1,'Yes':1})
# Set virus strain to be analysed to 1, and others 0
df_regress['Virus Strain'] = df_regress['Virus Strain'].map({'Influenza A H3N2v':1,'Influenza A H1N1v':0,'Influenza A H1N2v':0,'Influenza A H7N2':0})
#for column in df_regress:
#    print(column, df_regress[column].unique())

#=================logistic regression==========================================
endog = df_regress['Virus Strain'] #endogenous: dependent variable
exog = sm.add_constant(df_regress[['Age','Gender','Hospitalized?','Swine Contact?','Attended Agricultural Event?']]) #exogenous: independent variables
logit = smf.Logit(endog,exog)
result = logit.fit()
print(result.summary())

import numpy as np

print('Odds ratios:')
print(np.exp(result.params))


