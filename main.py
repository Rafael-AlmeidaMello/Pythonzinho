#1° exercício
#nome = input("Digite seu nome ")
#print("Seja bem-vindo",nome)

#2° exercício
#numero = float(input("Digite um número "))
#print("O dobro de ",numero, "é ",numero*2)

#3° exercício
#numero1 = float(input("Digite um número "))
#numero2 = float(input("Digite o segundo número "))
#print("A soma dos valores é igual a", numero1+numero2)

#4° exercício
#from datetime import date
#ano_nascimento = int(input("Digite o ano do seu nascimento "))
#idade = date.today().year - ano_nascimento
#print("Sua idade é", idade)

#5° exercício
#salario = float(input("Digite seu salário: "))
#aumento = salario /10
#salario_aumentado = salario + aumento
#print("Seu salário foi aumentado: R$",(salario_aumentado))

#6° exercício
#celsius = float(input("Digite um valor em graus celsius: "))
#fahrenheit = (celsius * 9/5) + 32
#resultado = print(celsius, "Convertido para fahrenheit é igual a:", fahrenheit)

#7° exercício

#nome = input("Insira seu nome: ")
#idade = input("Insira sua idade: ")
#cidade = input("Insira sua cidade: ")
#print(f"Seu nome é {nome}, você tem {idade} anos e mora em {cidade}")

#8° exercício
numero1 = float(input("digite o primeiro número: "))
numero2 = float(input("digite o segundo número: "))

operacao = input("digite a operação( +,  -,  *,  / ): ")

match operacao:
    case "+":
        resposta = numero1 + numero2
    case "-":
        resposta = numero1 - numero2
    case "*":
        resposta = numero1 * numero2
    case "/":
        resposta = numero1 / numero2
        
print(f"o resultado é: {resposta}")