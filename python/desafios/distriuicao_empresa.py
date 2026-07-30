class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def trabalhar(self):
        pass  # Funçao de cada um

class Gerente (Funcionario):
    def trabalhar(self):
        print("O gerente está administrando a equipe.")

class Programador (Funcionario):
    def trabalhar(self):
        print("O programador está escrevendo código.")

class Designer (Funcionario):
    def trabalhar(self):
        print("O designer está criando interfaces.")


gerente1 = Gerente("Douglas",3520)
print(f"o gerente da vez é o {gerente1.nome}")
gerente1.trabalhar()

programador1 = Programador("Silker", 2560)
print(f"o programador da vez é o {programador1.nome}")
programador1.trabalhar()

designer1 = Designer("Victor",2550)
print(f"o designer da vez é o {designer1.nome}")
designer1.trabalhar()