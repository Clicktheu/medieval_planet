import random
from loja import barganhar

def batalhar(personagem, inimigo):
    print(f"Você está enfrentando o {inimigo['nome']} - {inimigo['titulo']}")
   
    while personagem["vida"] > 0 and inimigo["vida"] > 0:
        print(f"Vida de {personagem['nome']}: {personagem['vida']}")
        print(f"Vida do {inimigo['nome']}: {inimigo['vida']}")
        print(f"Moedas possuídas: {personagem['dinheiro']}")
        
        print("Pressione Enter para começar o seu turno de batalha...")
        
        print("Opções:")
        print("[1] - Atacar com espada")
        print("[2] - Fugir")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            
            dano_do_personagem = random.randint(10, 30)
            
            is_critical = random.random() < 0.4  
            if is_critical:
                dano_do_personagem *= 2
                print("DANO CRÍTICO!")
            inimigo["vida"] -= dano_do_personagem
            print(f"{personagem['nome']} ataca {inimigo['nome']} e causa {dano_do_personagem} de dano.")
            
            
            if random.random() < 0.05:  
                moedas_encontradas = random.randint(20, 50)
                print(f"Você encontrou um baú de moedas! Ganhou {moedas_encontradas} moedas!")
                personagem["dinheiro"] += moedas_encontradas
        elif escolha == "2":
            print("Você fugiu da batalha!")
            return False
        else:
            print("Opção inválida! Perdeu o turno.")

            
        if inimigo["vida"] <= 0:
            print(f"Você derrotou o {inimigo['nome']}!")
            moedas_ganhas = random.randint(10, 20)  
            print(f"Você ganhou {moedas_ganhas} moedas!")
            personagem["dinheiro"] += moedas_ganhas
            return True
       
        
        if random.random() < 0.3:  
            print(f"{inimigo['nome']} errou o ataque!")
        else:
            dano_do_inimigo = random.randint(8, 12)
            personagem["vida"] -= dano_do_inimigo
            print(f"{inimigo['nome']} ataca {personagem['nome']} e causa {dano_do_inimigo} de dano.")
       
        if personagem["vida"] <= 0:
            print("Você foi derrotado!")
            return False

def batalhar_rei(personagem, rei):
    print(f"Você está enfrentando o Rei {rei['nome']} - {rei['titulo']}")
   
    while personagem["vida"] > 0 and rei["vida"] > 0:
        print(f"Vida de {personagem['nome']}: {personagem['vida']}")
        print(f"Vida do Rei {rei['nome']}: {rei['vida']}")
        print(f"Moedas possuídas: {personagem['dinheiro']}")
        
        print("Pressione Enter para começar o seu turno de batalha...")
        
        print("Opções:")
        print("[1] - Atacar com espada")
        print("[2] - Fugir")
        
        escolha = int(input("Escolha uma opção: "))
        
        if escolha == 1:
            
            dano_do_personagem = random.randint(15, 50)
            
            is_critical = random.random() < 0.5
            if is_critical:
                dano_do_personagem *= 2 
                print("DANO CRÍTICO!")
            rei["vida"] -= dano_do_personagem
            print(f"{personagem['nome']} ataca o Rei {rei['nome']} e causa {dano_do_personagem} de dano.")
        elif escolha == 2:
            print("Você fugiu da batalha!")
            return False
        else:
            print("Opção inválida! Perdeu o turno.")
            
        if rei["vida"] <= 0:
            print(f"Você derrotou o Rei {rei['nome']}!")
            print("Você venceu o jogo! Parabéns!")
            return True
       
        
        dano_do_rei = random.randint(50, 100)
        personagem["vida"] -= dano_do_rei
        print(f"O Rei {rei['nome']} ataca {personagem['nome']} e causa {dano_do_rei} de dano.")
       
        if personagem["vida"] <= 0:
            print("Você foi derrotado pelo Rei!")
            return False

def batalhar_rainha(personagem, rainha):
    print(f"Você está enfrentando a Rainha {rainha['nome']} - {rainha['titulo']}")
   
    while personagem["vida"] > 0 and rainha["vida"] > 0:
        print(f"Vida de {personagem['nome']}: {personagem['vida']}")
        print(f"Vida da Rainha {rainha['nome']}: {rainha['vida']}")
        print(f"Moedas possuídas: {personagem['dinheiro']}")
        
        print("Pressione Enter para começar o seu turno de batalha...")
        
        print("Opções:")
        print("[1] - Atacar com espada")
        print("[2] - Fugir")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            
            dano_do_personagem = random.randint(15, 100)
            
            is_critical = random.random() < 0.5  
            if is_critical:
                dano_do_personagem *= 2  
                print("DANO CRÍTICO!")
            rainha["vida"] -= dano_do_personagem
            print(f"{personagem['nome']} ataca a Rainha {rainha['nome']} e causa {dano_do_personagem} de dano.")
        elif escolha == "2":
            print("Você fugiu da batalha!")
            return False
        else:
            print("Opção inválida! Perdeu o turno.")
            
        if rainha["vida"] <= 0:
            print(f"Você derrotou a Rainha {rainha['nome']}!")
            print("Você venceu o jogo! Parabéns!")
            return True
       
        
        dano_da_rainha = random.randint(40, 80)
        personagem["vida"] -= dano_da_rainha
        print(f"A Rainha {rainha['nome']} ataca {personagem['nome']} e causa {dano_da_rainha} de dano.")
       
        if personagem["vida"] <= 0:
            print("Você foi derrotado pela Rainha!")
            return False

opcoes_dificuldade = {
    "1": {"chance_rainha": 0.2},
    "2": {"chance_rainha": 0.4},
    "3": {"chance_rainha": 0.6}
}

print("Escolha a dificuldade:")
print("1 - Fácil")
print("2 - Médio")
print("3 - Difícil")
dificuldade_escolhida = input("Escolha uma opção: ")

if dificuldade_escolhida not in opcoes_dificuldade:
    print("Opção inválida! O jogo foi encerrado.")
else:
    dificuldade = opcoes_dificuldade[dificuldade_escolhida]
    
    personagem = {
        "nome": "Mano Weber",
        "vida": 100,
        "dinheiro": 50
    }

    guardas = [
        {"nome": "Thorne", "titulo": "O Mestre da Trapaça", "vida": 50},
        {"nome": "Lorde Mortimer", "titulo": "O Perseguidor", "vida": 90},
        {"nome": "Vladrik", "titulo": "(Irmão de Petrick), O Carniceiro Implacável", "vida": 120},
        {"nome": "Petrick", "titulo": "(Irmão de Vladrik), O Vegano Implacável", "vida": 150}
    ]

    venceu_guardas = True  

    for i, guarda in enumerate(guardas, 4):
        last_choice = None 
        while True:
            print("Você tem duas opções:")
            print("[1] - Ir para a loja")
            print("[2] - Enfrentar o próximo guarda")
            escolha = input("Escolha uma opção: ")
            
            if escolha == "1":
                print("O que deseja comprar?")
                personagem = barganhar(personagem)
                  
            elif escolha == "2":
                result = batalhar(personagem, guarda)
        
                if not result:
                    print("Fim de jogo! Tente novamente.")
                    venceu_guardas = False  
                    break 
                else:
                    break 
            else:
                print("Opção inválida! Por favor, escolha uma opção válida.")
                if last_choice is not None:
                    escolha = last_choice  
                    break  
                last_choice = escolha  


if venceu_guardas:
    print("Parabéns! Você se mostrou digno e pode enfrentar o rei, mate-o!")

    rei = {
        "nome": "Rei Malvado",
        "titulo": "O Terrível",
        "vida": 250
    }

    print("Agora é hora de enfrentar o Rei!")

    while True:
        print("Você tem duas opções:")
        print("[1] - Enfrentar o Rei")
        print("[2] - Ir para a loja")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            result_rei = batalhar_rei(personagem, rei)
            if result_rei:
                print("Você venceu o Rei! Agora surgirá outro desafio, venca a Rainha!")
            else:
                print("Você foi derrotado pelo Rei. Tente novamente!")
            break
        elif escolha == "2":
            print("Você foi para a loja e recarregou suas energias.")
            personagem["vida"] = 100
        else:
            print("Opção inválida! Por favor, escolha uma opção válida.")

    if random.random() < dificuldade["chance_rainha"]:
        print("Você teve coragem de enfrentar a terrível Rainha Barrenta!")
        rainha = {
            "nome": "Rainha Barrenta",
            "titulo": "A Lamacenta",
            "vida": 200
        }
        
        last_choice = None 
        while True:
            print("Você tem duas opções:")
            print("[1] - Enfrentar a Rainha")
            print("[2] - Não enfrentar a Rainha")
            escolha = input("Escolha uma opção: ")
            
            if escolha == "1":
                result_rainha = batalhar_rainha(personagem, rainha)
                if result_rainha:
                    print("Parabéns! Você derrotou a Rainha Barrenta e salvou o reino novamente!")
                else:
                    print("Infelizmente, você foi derrotado pela Rainha Barrenta. Tente novamente!")
                break  
            elif escolha == "2":
                print("Você optou por não enfrentar a terrível Rainha Barrenta. Fim de jogo!")
                break  
            else:
                print("Opção inválida! Por favor, escolha uma opção válida.")
                if last_choice is not None:
                    escolha = last_choice 
                    break 
                last_choice = escolha 
    else:
        print("Você optou por não enfrentar a terrível Rainha Barrenta. Fim de jogo!")

