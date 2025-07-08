#2. Escreva um programa para calcular quantos dias levará para a colônia de uma bactéria A ultrapassar ou igualar a colônia de uma bactéria B, com base nas taxas de crescimento de 3% e 1,5% respectivamente. Considere que a colônia A inicia com 4 elementos e a B com 10.

# Inicialização das variáveis
bacteria_a = 4
bacteria_b = 10
dias = 0

# Cálculo do crescimento das bactérias usando while
while bacteria_a < bacteria_b:  # Continua enquanto a colônia A for menor que a B 
    bacteria_a *= 1.03  # Crescimento de 3%
    bacteria_b *= 1.015  # Crescimento de 1,5%
    dias += 1  # Incrementa o contador de dias

# Exibe o resultado
print(f"A colônia de bactérias A ultrapassará ou igualará a colônia de bactérias B em {dias} dias.")