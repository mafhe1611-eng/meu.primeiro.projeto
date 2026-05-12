import pandas as pd 

dados = pd.read_csv("academia.csv") 

print(dados)

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
print("AS 5 PRIMEIRAS LINHAS:")  
print(dados.head()) 
print("AS ULTIMAS 5 LINHAS:") 
print(dados.tail())
print("QUANTIDADE DE LINHAS E COLUNAS:") 
print(dados.shape)

# Exercicio 2 
print("MEDIA IDADE ALUNOS:")
print(dados["Idade"].mean())
print("MEDIA CALORIAS GASTAS:")
print(dados["Calorias"].mean())
print("MAIOR PESO:")
print(dados["Peso"].max())
print("MENOR PESO:")
print(dados["Peso"].min())