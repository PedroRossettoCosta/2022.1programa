from ast import NodeTransformer


numeros = []

#montar uma função que fique lendo 
#numeros do usuario, até que seja
# pressionado ENTER

def le_numeros(numeros):
    while True:
        valor = input("informe um numero: ")
        if valor == "":
            break

        numeros.append(float(valor))

notas = []

le_numeros(notas)

print(notas)

#min/max/sum
print(max(notas))
print(min(notas))
print(sum(notas))

#sorted = makes new list / sort = re-arranges list so you lose the initial information of the list you first
notas_ordenadas = sorted(notas)
print(notas_ordenadas)

notas.sort()
print(notas)

# count = count amount of times the number is on the list
print(notas.count(5))

#reverse = after you use sorted on the list the sort it according to the resverse = True then the list will be reversed into a big to small order

notas_decrescentes = sorted(
    notas,
    reverse = True
)
notas.sort(reverse = True)
print(notas)
print(notas_decrescentes)

#estruturas  imutaveis


def pilha_insere(lista,valor):
    lista.append(valor)

def pilha_remove(lista):
    return lista.pop()

def pilha_testa():
    pilha = []
    pilha_insere(pilha,4)
    pilha_insere(pilha,7)
    pilha_insere(pilha,9)
    print(pilha)
    for _ in range(2):
        pilha_remove(pilha)
print(pilha)

pilha_testa()

def fila_remove(lista):
    if lista:
        return lista.pop(8)

buffer_dados = []
    