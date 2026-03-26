"""
Programa de Geração de Personagem de Baldur's Gate 3
Criado por Julia Baptista
"""

import random
from time import sleep

while True:
    print()
    print("--" * 22)
    print("Gerador de Personagem para Baldur's Gate 3!")
    print("--" * 22)
    print("\nCriando Personagem...")

    sleep(3)

    truques = []
    magias = []
   
    # Escolhendo a Raça
    racas = [
        'Elfo', 'Tiefling', 'Drow', 'Humano', 'Githyanki', 'Anão',
        'Meio-Elfo', 'Halfling', 'Gnomo', 'Draconato', 'Meio-Orc'
    ]

    raca = random.choice(racas)
    print()
    print('--' * 22)
    print(f'\nRaça: {raca}')

    # Escolhendo a Sub-raça

    subraca = ''
    subracas = {
        'Elfo': ['Elfo Altaneiro', 'Elfo da Floresta'],
        'Tiefling': ['Tiefling de Asmodeus', 'Tiefling de Mefistófeles', 'Tiefling de Zariel'],
        'Drow': ['Drow Jurado a Lolth', 'Drow Seldarine'],
        'Anão': ['Anão Dourado', 'Anão do Escudo', 'Duergar'],
        'Meio-Elfo': ['Meio-Elfo Altaneiro', 'Meio-Elfo da Floresta', 'Meio-Elfo Drow'],
        'Halfling': ['Halfling Pé-Ligeiro', 'Halfling Robusto'],
        'Gnomo': ['Gnomo das Rochas', 'Gnomo das Florestas', 'Gnomo das Profundezas'],
        'Draconato': ['Negro', 'Azul', 'Latão', 'Bronze', 'Cobre', 'Ouro', 'Verde', 'Vermelho', 'Prata', 'Branco']
    }
    if raca in subracas:
        subraca = random.choice(subracas[raca])
        print('Sub-raça:', subraca)

    # Escolhendo Truques de Sub-raça
    if subraca == 'Elfo Altaneiro':
        truques.append(random.choice([
            'Bolha Ácida', 'Lâmina Estrondosa', 'Corpo Explosivo', 'Toque Necrótico',
            'Raio de Fogo', 'Jato de Veneno', 'Raio de Gelo', 'Toque Chocante',
            'Proteção Contra Lâminas', 'Amigos', 'Luzes Bruxuleantes', 'Luz',
            'Mão Mágica', 'Ilusão Menor', 'Sino da Morte', 'Golpe Certeiro'
        ]))
        print(f'Truques de Sub-raça: {truques}')

    # Escolhendo a Classe
    classes = [
        'Bárbaro', 'Bardo', 'Clérigo', 'Druida', 'Guerreiro',
        'Monge', 'Paladino', 'Patrulheiro', 'Ladino',
        'Feiticeiro', 'Bruxo', 'Mago'
    ]
    
    classe = random.choice(classes)
    print()
    print("--" * 22)
    print(f"\nClasse: {classe}")

    # Escolhendo Truques de Classe
    if classe == 'Bardo':
        truques += random.sample(['Zombaria Perversa', 'Proteção Contra Lâminas', 'Mão Mágica', 'Golpe Certeiro', 'Amigos', 'Luzes Bruxuleantes', 'Luz', 'Ilusão Menor'], 2)
        print(f'Truques de Classe: {truques}')
    elif classe == 'Clérigo':
        truques += random.sample(['Proteção Contra Lâminas', 'Corpo Explosivo', 'Orientação', 'Luz', 'Produzir Chama', 'Resistência','Chama Sagrada', 'Taumaturgia'], 2)
        print(f'Truques de Classe: {truques}')
    elif classe == 'Druida':
        truques += random.sample(['Orientação', 'Jato de Veneno', 'Produzir Chama', 'Resistência', 'Shillelagh', 'Chicote Espinhento'], 2)
        print(f'Truques de Classe: {truques}')
    elif classe == 'Feiticeiro':
        truques += random.sample(['Proteção Contra Lâminas', 'Lâmina Estrondosa', 'Corpo Eplosivo', 'Bolha Ácida', 'Mão Mágica', 'Jato de Veneno', 'Golpe Certeiro', 'Amigos', 'Luzes Bruxuleantes', 'Luz', 'Raio de Gelo', 'Toque Chocante', 'Ilusão Menor', 'Toque Necrótico'], 4)
        print(f'Truques de Classe: {truques}')
    elif classe == 'Bruxo':
        truques += random.sample(['Proteção contra lâminas', 'Lâmina Estrondosa', 'Toque Necrótico', 'Raio Místico', 'Amigos', 'Mão Mágica', 'Ilusão Menor', 'Jato de Veneno', 'Sino da Morte', 'Golpe Certeiro'], 2)
        print(f'Truques de Classe: {truques}')
    elif classe == 'Mago':
        truques += random.sample(['Bolha Ácida', 'Lâmina Estrondosa', 'Corpo Explosivo', 'Toque Necrótico', 'Jato de Veneno', 'Raio de Gelo', 'Toque Chocante', 'Proteção Contra Lâminas', 'Amigos', 'Luzes Bruxuleantes', 'Luz', 'Mão Mágica', 'Ilusão Menor', 'Sino da Morte', 'Golpe Certeiro'], 3)
        print(f'Truques de Classe: {truques}')

    # Escolhendo Magias de Classe
    if classe == 'Bardo':
        magias += random.sample(['Amizade Animal', 'Perdição', 'Enfeitiçar Pessoa', 'Curar Ferimentos', 'Disfarçar-se', 'Sussurros Dissonantes', 'Fogo das Fadas', 'Queda Suave', 'Palavra Curativa', 'Heroísmo', 'Passos Longos', 'Sono', 'Falar com Animais', 'Gargalhada Nefasta de Tasha', 'Onda Trovejante'], 4)
        print(f'Magias de Classe: {magias}')
    elif classe == 'Feiticeiro':
        magias += random.sample(['Mãos flamejantes', 'Enfeitiçar Pessoa', 'Esfera Cromática', 'Leque Cromático', 'Disfarçar-se', 'Recuo Apressado', 'Vitalidade vazia', 'Queda Suave', 'Névoa Obscurecente', 'Faca de Gelo', 'Salto Aprimorado', 'Armadura Arcana', 'Mísseis Mágicos', 'Raio Nauseante', 'Escudo', 'Sono', 'Onda Trovejante', 'Raio de Bruxa'], 2)
        print(f'Magias de Classe: {magias}')
    elif classe == 'Mago':
        magias += random.sample(['Mãos Flamejantes', 'Enfeitiçar Pessoa', 'Esfera Cromática', 'Leque Cromático', 'Disfarçar-se', 'Recuo Apressado', 'Vitalidade Vazia', 'Queda Suave', 'Convocar Familiar', 'Névoa Obscurecente', 'Graxa', 'Faca de Gelo', 'Salto Aprimorado', 'Passos Longos', 'Armadura Arcana','Mísseis Mágicos', 'Proteção Contra o Bem e o Mal', 'Raio Nauseante', 'Escudo', 'Sono', 'Gargalhada Nefasta de Tasha', 'Onda Trovejante', 'Raio de Bruxa'], 6)
        print(f'Magias de Classe: {magias}')

    # Escolhendo a Subclasse
    subclasses = {
        'Clérigo': [ 'Domínio da Morte', 'Domínio do Conhecimento', 'Domínio da Vida', 'Domínio da Luz', 'Domínio da Natureza', 'Domínio da Tempestade', 'Domínio da Enganação', 'Domínio da Guerra'],
        'Paladino' : [ 'Juramento dos Anciãos', 'Juramento da Devoção', 'Juramento da Vingança', 'Juramento da Coroa'],
        'Feiticeiro' : ['Linhagem Dracônica', 'Magia das Trevas', 'Feitiçaria da Tempestade', 'Magia Selvagem'],
        'Bruxo' : ['A Arquifada', 'Ínfero', 'O Grandioso e Antigo', 'Lâmina da Danação']
    }

    subclasse = ''
    if classe in subclasses:
        subclasse = random.choice(subclasses[classe])
        print('Subclasse:', subclasse)

    # Escolhendo Truques de Subclasse
    if subclasse == 'Domínio da Morte':
        truques.append(random.choice(['Corpo explosivo', 'Toque Necrótico', 'Sino da Morte']))
        print(f'Truques de Subclasse: {truques}')
    elif subclasse == 'Domínio da Natureza':
        truques.append(random.choice(['Jato de Veneno', 'Produzir Chama', 'Shillelagh', 'Chicote espinhento']))
        print(f'Truques de Subclasse: {truques}')

    # Escolhendo Magias de Subclasse
    if subclasse == 'A Arquifada':
        magias += random.sample(['Armadura de Agathys', 'Braços de Hadar', 'Enfeitiçar Pessoa', 'Recuo Apressado', 'Fogo das Fadas', 'Repreensão Diabólica', 'Danação', 'Proteção Contra o Bem e o Mal', 'Sono', 'Raio de Bruxa'], 2)
        print(f'Magias de Subclasse: {magias}')
    elif subclasse == 'Ínfero':
        magias += random.sample(['Armadura de Agathys', 'Braços de Hadar', 'Mãos Flamejantes', 'Enfeitiçar Pessoa', 'Comando', 'Recuo Apressado', 'Repreensão Diabólica', 'Danação', 'Proteção Contra o Bem e o Mal', 'Raio de Bruxa'], 2)
        print(f'Magias de Subclasse: {magias}')
    elif subclasse == 'O Grandioso e Antigo':
        magias += random.sample(['Armadura de Agathys', 'braços de Hadar', 'Enfeitiçar Pessoa', 'Sussurros Dissonantes', 'Recuo Apressado', 'Repreensão Diabólica', 'Danação', 'Proteção Contra o Bem e o Mal', 'Gargalhada Nefasta de Tahsha', 'Raio de Bruxa'], 2)
        print(f'Magias de Subclasse: {magias}')
    elif subclasse == 'Lâmina da Danação':
        magias += random.sample(['Armadura de Agathys', 'Braços de Hadar', 'Enfeitiçar Pessoa', 'Recuo Apressado', 'Repreensão Diabólica', 'Danação', 'Proteção Contra o Bem e o Mal', 'Escudo', 'Raio de Bruxa', 'Destruição Colérica'], 2)
        print(f'Magias de Subclasse: {magias}')

    # Escolhendo Peculiaridades
    if classe == "Bardo":
        print()
        print("--" * 22)
        print("\nInstrumento inicial:", random.choice([
            "Tambor de Mão", "Flauta", "Alaúde", "Lira", "Violino"
        ]))

    elif classe == "Clérigo":
        print()
        print("--" * 22)
        print("\nDivindade:", random.choice([
            "Selûne", "Bahamut", "Tempus", "Tyr", "Helm", "Ilmater",
            "Mystra", "Oghma", "Kelemvor", "Moradin", "Corellon Larethian",
            "Garl Glória D'ouro", "Yondalla", "Lolth", "Gruumsh", "Tiamat"
        ]))

    if subclasse == "Linhagem Dracônica":
        print()
        print("--" * 22)
        print("\nAncestralidade:", random.choice([
            "Vermelho (Fogo)", "Preto (Ácido)", "Azul (Elétrico)",
            "Branco (Frio)", "Verde (Veneno)", "Ouro (Fogo)",
            "Prata (Frio)", "Bronze (Elétrico)",
            "Cobre (Ácido)", "Latão (Fogo)"
        ]))

    print()

    # Escolhendo o Histórico
    historicos = [
        "Acólito", "Charlatão", "Criminoso", "Artista", "Herói do Povo",
        "Artesão de Guilda", "Nobre", "Forasteiro", "Sábio", "Soldado", "Pivete"
    ]

    print("--" * 22)
    print("\nHistórico:", random.choice(historicos))
    print()
    print("--" * 22)

    # Confirmação
    while True:
        opcao = input('Deseja gerar outra família? (S/N): ').upper().strip()
        if opcao == 'S':
            break
        elif opcao == 'N':
            print('\nPrograma encerrado! Boa gameplay! 🎮✨\n')
            exit()
        else:
            print('\nDigite apenas S para sim ou N para não!\n')
