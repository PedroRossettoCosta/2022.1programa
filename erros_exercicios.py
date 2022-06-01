'''
PRogramação Estruturada
2022.1
25/05/2022
Trateamento de Erros e Exceções
'''



#try / except

while True:
    try:
        cpf = int(input("Informe o seu CPF: "))
        break
    except ValueError:
        print("Informe apenas números.")
    else: # only runs if it doesnt go into any except
        break

try:
    arq = open("teste.py")
except FileNotFoundError:
    arq = open("readme.md", "w")
    arq.close()
except FileExistsError:
    print("O arquivo já existe!")
finally: # executes independently of the excepts because it will happen either way
    #escrever (arq, "bom dia")
    if arq:
        arq.close()
    print("-" * 40)

total_notas = 5
divisor = float(input("Informe um numero: "))
try:
    print(total_notas / divisor)
except ZeroDivisionError:
    print("ERRO FATAL - mensagem de erro explicando o erro que ocorreu")
    exit()

def func1(num):
    print(5/num)

def func2():
    func1(0)

def func3():
    func2()

func3()


meses