import random
def barganhar(personagem):
    print("Bem-vindo à loja! O que você deseja comprar?")
    print("[1] - Poção de Vida (10 moedas) - Recupera 100 de vida")
    print("[2] - Espada Encantada (10 moedas) - Aumenta o dano do seu ataque")
    print("[3] - Amuleto de Força (20 moedas) - Aumenta seu dano em 50")
    print("[4] - Voltar ao menu principal")
    
    escolha = input("Escolha uma opção: ")
    
    if escolha == "1":
        print("você ganhou 100 de vida!")
        personagem["dinheiro"] >=10
        personagem["vida"] +=20
        personagem["dinheiro"] -= 50

    elif escolha == "2":
       if personagem["dinheiro"] >=10:
          personagem["dinheiro"] -=10
          print("seu dano aumentou!")  
    
    elif escolha == "3":
        if personagem["dinheiro"] >= 20:
            personagem["dinheiro"] -= 20
            print("Você comprou um Amuleto de Força! Seus ataques causarão mais dano.")
        else:
            print("Você não possui moedas suficientes para comprar isso.")
    elif escolha == "4":
        print("Voltando ao menu principal da loja.")
    else:
        print("Opção inválida!")
    
    return personagem
