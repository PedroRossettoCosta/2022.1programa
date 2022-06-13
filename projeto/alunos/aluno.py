class aluno:

    def __init__(self, matricula, nome, cpf):
        self.matricula = matricula
        self.nome = nome
        self.cpf = cpf
        self.curso = ""
        self.disciplina = []

    def inscrever_curso(self, curso):
        self.curso = curso

    def adicionar_disciplina(self, disciplina):
        self.disciplina.append = disciplina

    def __repr__(self):
        print("exibindo informações do aluno: ")
        return " ".join([self.matricula, self.nome, self.cpf])
    

    