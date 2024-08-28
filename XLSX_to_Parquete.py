import pandas as pd


#base XLSX
path_caso_estudos = r"C:\Users\wisley\Desktop\Udemy\Análise de Dados com Python e Machine Learning\dataBase\caso_estudo.xlsx" 

#Path para salvar
destino = r"C:\Users\wisley\Desktop\Udemy\Análise de Dados com Python e Machine Learning\dataBase"

# Carrega o arquivo XLSX
df = pd.read_excel(path_caso_estudos, engine='openpyxl')

# Salva no formato Parquet
df.to_parquet(destino+r'aaaaa.parquet', engine='pyarrow')
