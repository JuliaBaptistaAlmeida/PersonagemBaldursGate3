"""
Programa de Geração de Personagem de Baldur's Gate 3
 Criado por Julia Baptista (adaptado para Python)
 """

import random
from time import sleep

while True:
    print()
    print("--" * 18)
    print("Gerador de Personagem para Baldur's Gate 3!")
    print("--" * 18)
    print("\nCriando Personagem...")

    sleep(3)

    # Raças
    racas = [
        "Elfo", "Tiefling", "Drow", "Humano", "Githyanki", "Anão",
        "Meio-Elfo", "Halfling", "Gnomo", "Draconato", "Meio-Orc"
    ]

    raca = random.choice(racas)

    print()
    print("--" * 18)
    print(f"\nRaça: {raca}")

    if raca == "Elfo":
        print("Sub-raça:", random.choice(["Elfo Altaneiro", "Elfo da Floresta"]))

    elif raca == "Tiefling":
        print("Sub-raça:", random.choice([
            "Tiefling de Asmodeus", "Tiefling de Mefistófeles", "Tiefling de Zariel"
        ]))

    elif raca == "Drow":
        print("Sub-raça:", random.choice(["Drow Jurado a Lolth", "Drow Seldarine"]))

    elif raca == "Anão":
        print("Sub-raça:", random.choice(["Anão Dourado", "Anão do Escudo", "Duergar"]))

    elif raca == "Meio-Elfo":
        print("Sub-raça:", random.choice([
            "Meio-Elfo Altaneiro", "Meio-Elfo da Floresta", "Meio-Elfo Drow"
        ]))

    elif raca == "Halfling":
        print("Sub-raça:", random.choice(["Halfling Pé-Ligeiro", "Halfling Robusto"]))

    elif raca == "Gnomo":
        print("Sub-raça:", random.choice([
            "Gnomo das Rochas", "Gnomo das Florestas", "Gnomo das Profundezas"
        ]))

    elif raca == "Draconato":
        print("Sub-raça: Draconato", random.choice([
            "Negro", "Azul", "Latão", "Bronze", "Cobre",
            "Ouro", "Verde", "Vermelho", "Prata", "Branco"
        ]))

    print()

    # Classes
    classes = [
        "Bárbaro", "Bardo", "Clérigo", "Druida", "Guerreiro",
        "Monge", "Paladino", "Patrulheiro", "Ladino",
        "Feiticeiro", "Bruxo", "Mago"
    ]

    classe = random.choice(classes)

    print("--" * 18)
    print(f"\nClasse: {classe}")

    if classe == "Bardo":
        print("Instrumento inicial:", random.choice([
            "Tambor de Mão", "Flauta", "Alaúde", "Lira", "Violino"
        ]))

    elif classe == "Clérigo":
        print("Subclasse:", random.choice([
            "Domínio da Morte", "Domínio do Conhecimento", "Domínio da Vida",
            "Domínio da Luz", "Domínio da Natureza", "Domínio da Tempestade",
            "Domínio da Enganação", "Domínio da Guerra"
        ]))

        print("Divindade:", random.choice([
            "Selûne", "Bahamut", "Tempus", "Tyr", "Helm", "Ilmater",
            "Mystra", "Oghma", "Kelemvor", "Moradin", "Corellon Larethian",
            "Garl Glória D'ouro", "Yondalla", "Lolth", "Gruumsh", "Tiamat"
        ]))

    elif classe == "Paladino":
        print("Subclasse:", random.choice([
            "Juramento dos Anciãos",
            "Juramento da Devoção",
            "Juramento da Vingança",
            "Juramento da Coroa"
        ]))

    elif classe == "Bruxo":
        print("Subclasse:", random.choice([
            "A Arquifada", "Ínfero", "O Grandioso e Antigo", "Lâmina da Danação"
        ]))

    elif classe == "Feiticeiro":
        subclasse = random.choice([
            "Linhagem Dracônica", "Magia das Trevas",
            "Feitiçaria da Tempestade", "Magia Selvagem"
        ])

        print("Subclasse:", subclasse)

        if subclasse == "Linhagem Dracônica":
            print("Ancestralidade:", random.choice([
                "Vermelho (Fogo)", "Preto (Ácido)", "Azul (Elétrico)",
                "Branco (Frio)", "Verde (Veneno)", "Ouro (Fogo)",
                "Prata (Frio)", "Bronze (Elétrico)",
                "Cobre (Ácido)", "Latão (Fogo)"
            ]))

    print()

    # Histórico
    historicos = [
        "Acólito", "Charlatão", "Criminoso", "Artista", "Herói do Povo",
        "Artesão de Guilda", "Nobre", "Forasteiro", "Sábio", "Soldado", "Pivete"
    ]

    print("--" * 18)
    print("\nHistórico:", random.choice(historicos))
    print()
    print("--" * 18)

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
