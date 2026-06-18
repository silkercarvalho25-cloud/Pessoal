"""
🌶️🌶️🌶️ Desafio 3: O RPG dos Monstros (Avançado)
Contexto: Vamos criar o esqueleto de um sistema de combate de RPG de texto.

O que fazer:

Crie um dicionário para o jogador com as chaves: 'nome', 'hp' (vida), e 'ataque'.

Crie um dicionário para o monstro com as mesmas chaves.

Crie um loop while que continuará rodando enquanto o hp do jogador E o hp do monstro forem maiores que 0.

A cada turno, o usuário deve escolher uma ação através de um menu (if/elif/else):

1. Atacar: Causa o valor de 'ataque' do jogador no hp do monstro.

2. Curar: Recupera um valor fixo de hp do jogador (mas gasta o turno).

3. Fugir: Encerra o jogo imediatamente.

Se o monstro sobreviver ao turno do jogador, ele ataca o jogador automaticamente, reduzindo o hp do jogador com o valor de 'ataque' do monstro.

Use if/else para verificar quem morreu primeiro e exibir a mensagem de "Vitória" ou "Game Over".
"""

jogador = {
    "nome": "Silker",
    "hp":100,
    "ataque": 1
}

monstro = {
    "nome": "Monstro",
    "hp":100,
    "ataque": 1
}

while monstro["hp"] > 0 and jogador["hp"] > 0:
    print("""
 Oque vc deseja fazer agora no monstro?
1 - Atacar (-1 de Vida Monstro)
2 - Curar (+1 de Vida Jogador)
3 - Fugir (encerra o jogo)
""")
resposta = input("Qual opçao voce escolhe?:")