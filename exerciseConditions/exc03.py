# 3. Escreva um programa que determine se uma letra fornecida pela pessoa usuária é uma vogal ou consoante.

letra = input("Digite uma letra: ").lower()

if letra in 'aeiou':
    print(f"A letra '{letra}' é uma vogal.")
elif letra.isalpha():
    print(f"A letra '{letra}' é uma consoante.")
else:
    print("O caractere digitado não é uma letra válida.")