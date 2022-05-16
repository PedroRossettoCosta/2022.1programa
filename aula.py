"""

2022.1 - Programação Estruturada
16/05/2022

Listas
"""
# lista = [10, 1.45, "texto", True, False, [] {}]

alunos = ["abc", "def", "ghi"]
print(alunos[1])
print(alunos[-1])

# fatiamento
# slicing
alunos = ["abc", "def", "ghi", "ijk",
          "mno", "pqr", "stu", "vwx"
]

premiados = alunos[0:3]
premiados = alunos[:3]
pares = alunos[1::2]
listas = alunos[::3]
ordem_inversa = alunos [::-1]

print(ordem_inversa)
print(alunos)

alunos.append("yza")
print(alunos)

alunos.insert(4, "aaa")
print(alunos)

alunos.extend(["bbb", "ccc", "ddd"])
print(alunos)

alunos.extend("eee")
print(alunos)

alunos.pop() # remove o ultimo intem da lista
print(alunos)

alunos.pop(4) # revome o intem do indice selecionado
print(alunos)

aluno = alunos.pop()
print(aluno)
print(f"{aluno} foi eliminado")

alunos.remove("ghi")
print(alunos)

# vai subir uma exceção"
# alunos.remove(xpto)

indice = alunos.index("def")
print(indice)

if "xpto" in alunos:
    alunos.remove("xpto")

# evitar esta estrutura!
for indice in range(len(alunos)):
    print(alunos[indice])

wifor indice, aluno in enumerate(alunos):
    print(indice, aluno, sep=" - ")

print("alunos")
print(alunos)

for indice, _ in enumerate(alunos):
    print(indice)

alunos = [
    "abc", "def", "ghi",
    "jkl", "ghi", "mno", "pqr"
    "ghi", "stu", "ghi", "vwx"
]

while "ghi" in alunos:
    alunos.remove("ghi")

