class Comida:
    def __init__(self,qualidade,ano_validade,nome_alimento):
        self.qualidade = qualidade
        self.ano_validade = ano_validade
        self.nome_alimento = nome_alimento

    print(""" <=== SUPER CLASSIFICADOR DE ALIMENTOS ===>
Seja Bem - Vindo ao Super Classificadopr 
          de Alimentos 2026
            """)
    
class Frutas(Comida):
    def __init__(self, qualidade, ano_validade, nome_alimento,validade):
        super().__init__(qualidade, ano_validade, nome_alimento)
        self.validade = validade
    
    def vendo_validade(self):
        print(f"{"VENCEU" if self.validade < 2026 else "NAO VENCEU"}")

class Legumes(Comida):
    pass

class Carnes(Comida):
    pass

maça = Frutas("nova",2028,"maça",2028)
print(f"""NOME FRUTA:{maça.nome_alimento} 
QUALIDADE:{maça.qualidade}
ANO DA VALIDADE:{maça.ano_validade}
""")
maça.vendo_validade()
print("=" * 20)
feijao = Legumes("Bom",2026,"feijao")
print(f"""NOME LEGUME:{feijao.nome_alimento} 
QUALIDADE:{feijao.qualidade}
ANO DA VALIDADE:{feijao.ano_validade}
""")
print("=" * 20)

bisteca = Carnes("Ruim",2024,"bisteca")
print(f"""NOME FRUTA:{bisteca.nome_alimento} 
QUALIDADE:{bisteca.qualidade}
ANO DA VALIDADE:{bisteca.ano_validade}
""")