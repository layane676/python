# def boas_vindas():
#     print("Seja bem vindo")

# boas_vindas()

# nome = input("Digite seu nome: ")
# def saudacoes(nome):
#     print(f"Olá, {nome}!")

# saudacoes(nome)

# def soma(a, b):
#     return a+b

# resultado=soma(5, 7)
# print(resultado)

# def consumo_combustivel():
#     nome=input("Digite seu nome: ")
#     kg=float(input("Digite quantos quilômetros você percorreu:"))
#     gasolina=float(input("Digite quantos litros de gasolina você gastou:"))

#     consumo=kg/gasolina

#     if consumo >= 15:
#         situacao="Econômico"
#     elif consumo < 15 and consumo >= 10:
#         situacao="Regular"
#     else:
#         situacao="Alto consumo"

#     print(f"Motorista: {nome}")
#     print(f"Consumo: {consumo}km/l")
#     print(f"Situação: {situacao}")

# consumo_combustivel() 


# def imc():
#     nome=input("Digite seu nome: ")
#     peso=float(input("Qual é o seu peso:"))
#     altura=float(input("Digite sua altura em metros:"))

#     imc= peso/(altura*2)


#     if imc >= 30:
#         situacao="Obesidade"
#     elif imc < 25 and imc >= 29.9:
#         situacao="Sobrepeso"
#     elif imc <18.5 and imc >= 24.9:
#         situacao="Peso normal"
#     else:
#         situacao="Abaixo do peso"

#     print(f"Motorista: {nome}")
#     print(f"Imc: {imc}")
#     print(f"Situação: {situacao}")

# imc() 

# def velocidade():
#     nome=input("Digite seu nome: ")
#     velocidade=float(input("Digite a velocidade média em km/h:"))
#     limite = 80

#     if velocidade >= 100:
#         situacao="Acima do limite (grave)"
#     elif velocidade < 81 and velocidade > 100 :
#         situacao="Acima do limite (leve)"
#     elif velocidade == limite:
#         situacao="Dentro do limite"
#     else:
#         situacao="Abaixo do limite"

#     print(f"Motorista: {nome}")
#     print(f"Velocidade: {velocidade}km/h")
#     print(f"Situação: {situacao}")

# velocidade()

# def soma(a, b):
#     nome= input("Digite seu nome:")
#     a = float(input("digite o promeiro numero:"))
#     b = float(input("Digite o segundo numero:"))
#     print(f"Olá {nome}, o resultado da soma é: {a + b}")

# soma(0,0) 

numeros = [1,2,3,4]
numeros.append(5)
print(numeros)
