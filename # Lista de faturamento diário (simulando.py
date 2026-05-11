#analise_dados.py
faturamento = [1500, 2300, 800, 4500, 1200, 3100, 500]

# Calcula o faturamento total usando a funcao sum()
total = sum(faturamento)

# Calcula a quantidade de dias
quantidade = len(faturamento)

# Calcula a media de faturamento
media = total / quantidade

# Exibe o relatorio
print("Relatorio de Performance:")
print(f"Faturamento Total: R$ {total:.2f}")
print(f"Media Diaria: R$ {media:.2f}")
print("-" * 30)

# Analisa cada valor
for valor in faturamento:
    if valor > media:
        print(f"Destaque Positivo: R$ {valor} (Acima da media)")
    else:
        print(f"Dia Normal: R$ {valor}")
