import pandas as pd

path_caso_estudos = r"C:\Users\wisley\Desktop\Udemy\Análise de Dados com Python e Machine Learning\dataBase\caso_estudo.xlsx" 


df_caso_estudo = pd.read_excel(path_caso_estudos)

print(df_caso_estudo)