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
#numero1 = float(input("digite o primeiro número: "))
#numero2 = float(input("digite o segundo número: "))
#operacao = input("digite a operação( +,  -,  *,  / ): ")

#match operacao:
#   case "+":
#    resposta = numero1 + numero2
#   case "-":
#    resposta = numero1 - numero2
#   case "*":
#    resposta = numero1 * numero2
#   case "/":
#    if numero2 == 0:
#         resposta = "não é possivel dividir por zero"
#      else:
#           resposta = numero1 / numero2      
#   print(f"o resultado é: {resposta}")

#9° exercício
#valor_hora = float(input("Quanto você ganha por hora? "))
#horas_trabalhadas = float(input("Quantas horas você trabalhou?"))
#salario = valor_hora * horas_trabalhadas
#desconto_inss = salario * 0.11
#salario_liquido = salario - desconto_inss
#print(f"Seu salário final é R${salario_liquido}")

#10° exercício
#real = float(input("Quanto você gostaria de converter para dólar?"))
#cotacao = 5.27
#dolares = real / cotacao
#print((f"O valor em reais convertidos em dólares é igual a ${dolares:.2f}"))

#11° exercício
#numero = float(input("Digite um número: "))
#if numero >= 0:
#        print(f"O número {numero} é positivo")
#else:
#        print(f"O número {numero} é negativo")

#12° exercício
#numero = float(input("Digite um número: "))
#if numero % 2 == 0:
#        print(f"O número {numero} é par")
#else:
#        print(f"O número {numero} é ímpar")

#13° exercício
#nota1 = float(input("Digite sua primeira nota: "))
#nota2 = float(input("Digite a segunda nota: "))
#media = (nota1 + nota2) / 2
#if media >= 7:
#    print(f"O aluno está aprovado, nota final: {media}")
#else:
#    print(f"O aluno está reprovado, {media}")

#14° exercício
#usuario = input("Crie um nome para seu usuário: ")
#password = input("Crie uma senha para seu usuário: ")
#validacao_usuario = input("Digite o nome do seu usuário criado: ")
#validacao_senha = input("Digite a senha do seu usuário: ")
#if usuario == validacao_usuario and password == validacao_senha:
#    print(f"Login efetuado! Seja bem vindo {usuario}")
#else:
#    print(f"Usuário ou senha incorretos")

#15° exercício
nome = input("Digite seu nome: ")
idade = float(input("Digite sua idade: "))
salario = float(input("Informe seu salário: "))

if idade >= 18 and salario >= 2000:
    print("Parabéns! Você já pode financiar um carro.")
else:
    print("Você ainda não tem condições pra financiar um carro")