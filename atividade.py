import pandas as pd 

dados = pd.read_csv("academia.csv")

print("="*30)
print(" Base de Dados Completa ")
print("="*30)
print(dados)
print("\n")

# Lê o arquivo "academia.csv"
# header=0 indica que a primeira linha do arquivo contém os nomes das colunas
# sep="," indica que os valores estão separados por vírgula
# Os dados são armazenados na variável dados_academy
dados_academy = pd.read_csv ("academia.csv", header=0, sep=",")

# Selecione as colunas Nome,Idade,Peso,Altura,Horas_Treino,Calorias do "academia.csv"
# Esses dados serao a variavel x
nome= ['Nome']
idade= ['Idade']
peso= ['Peso']
altura= ['Altura']
horas_treino= ['Horas_Treino']
calorias= ['Calorias']
x = dados_academy 


# Selecione os numeros do "academia.csv"
# esses numeros serao a variavel y
dados = pd.read_csv("academia.csv")
y = dados_academy 


# Crie uma tabela organizando os dados do "academia.csv" 
# x fica na linha horizontal da tabela
# y fica nas linhas diagonais da tabela de acordo com o x

# Exercicio 1 
print("-" * 20)
print("AS 5 PRIMEIRAS LINHAS:")  
print(dados.head())

print("\n" + "-" * 20)
print("AS ULTIMAS 5 LINHAS:") 
print(dados.tail())

print("-" * 20)
print("QUANTIDADE DE LINHAS E COLUNAS: {dados.shape}") 

# Exercicio 2 
print("MEDIA IDADE ALUNOS: {dados["Idade"].mean() 1.f} anos")

print("MEDIA CALORIAS GASTAS: {dados["Calorias"].mean()} kcal")

print("MAIOR PESO: {dados["Peso"].max()} kg")

print("MENOR PESO: {dados["Peso"].min()}")
