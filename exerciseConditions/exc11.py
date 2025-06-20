# 11. Escreva um programa que peça à pessoa usuária três números que representam os lados de um triângulo. O programa deve informar se os valores podem ser utilizados para formar um triângulo e, caso afirmativo, se ele é equilátero, isósceles ou escaleno. Tenha em mente algumas dicas:

# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes.

def verificar_triangulo(lado1, lado2, lado3):
    if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
        if lado1 == lado2 == lado3:
            return "Triângulo Equilátero: todos os lados são iguais."
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            return "Triângulo Isósceles: dois lados são iguais."
        else:
            return "Triângulo Escaleno: todos os lados são diferentes,"
    else:
        return "Os valores informados não podem formar um triângulo."
    
def main():
    try:
        lado1 = float(input("Digite o comprimento do primeiro lado do triângulo: "))
        lado2 = float(input("Digite o comprimento do segundo lado do triângulo: "))
        lado3 = float(input("Digite o comprimento do terceiro lado do triângulo: "))
    except ValueError:
        print("Valor inválido! Por favor, digite números válidos.")
        return

    resultado = verificar_triangulo(lado1, lado2, lado3)
    print(resultado)
if __name__ == "__main__":
    main()