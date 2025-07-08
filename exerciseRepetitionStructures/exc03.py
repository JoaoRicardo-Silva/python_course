#3. Para tratar uma quantidade de 15 dados de avaliações de pessoas usuárias de um serviço da empresa, precisamos verificar se as notas são válidas. Então, escreva um programa que vai receber a nota de 0 a 5 de todos os dados e verificar se é um valor válido. Caso seja inserido uma nota acima de 5 ou abaixo de 0, repita até que a pessoa usuária insira um valor válido.

for i in range(15):
    while True:
        try:
            nota = float(input(f"Digite a nota (0 a 5) para o dado {i + 1}:"))
            if 0 <= nota <= 5:
                print(f"Nota válida: {nota}")
                break  # Sai do loop se a nota for válida
            else:
                print("Nota inválida. Por favor, insira um valor entre 0 e 5.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")
        