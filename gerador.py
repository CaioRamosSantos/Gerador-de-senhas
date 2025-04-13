import random

print("=== GERADOR DE SENHAS ===")

tamanho = int(input("Quantos caracteres a senha deve ter? "))

letras_maiusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letras_minusculas = "abcdefghijklmnopqrstuvwxyz"
numeros = "0123456789"

todos = letras_maiusculas + letras_minusculas + numeros

senha = ""

for i in range(tamanho):
    senha += random.choice(todos)

print(f"Sua senha gerada é {senha}")