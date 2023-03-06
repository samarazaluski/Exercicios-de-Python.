print ("Seu imc")

Peso = float(input("Digite seu peso em kg: "))
Altura = float(input("Digite sua altura em metro: "))
Altura2 = float(input("Digite sua altura em metro novamente: "))

imc = Peso / (Altura * Altura2)

print(f"Seu IMC  eh: {imc: .2f}")