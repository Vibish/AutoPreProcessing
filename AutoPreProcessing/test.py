import pandas as pd
from AutoPreProcessing import EDA
df = pd.read_csv('data/DeathRate.csv')
CategoricalFeatures = ['Sex','LifeExpectency','Race','Race2']

#CategoricalFeatures = ['LifeExpectency']
#df = pd.read_csv('Data/sudeste.csv')
#CategoricalFeatures = ['city','prov']
# print(EDA)
eda = EDA(df,CategoricalFeatures,debug = 'YES')
eda.EDAToHTML(out='./HTMLTemplate/dist/output.html')
