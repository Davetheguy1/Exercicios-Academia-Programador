# Versão com os eventos especiais programados, porém não funcionais

import random


def main_menu():
    # menu principal

    print('\n*Corrida de Dados*\n')
    menu_request = input('1. Jogar\n2. Sair\n')
    if (menu_request == "1"):
       secondary_menu()
    elif (menu_request == "2"):
        print('\nFinalizando o Programa...'), exit()   
    else: print('\nFavor escolher uma opção válida')


def secondary_menu():
    # menu de seleção da duração da corrida
    
    print('\nEscolha a duração da corrida:\n')
    secondary_request = input('1. Curta (20 Casas)\n 2. Média (35 Casas)\n 3. Longa (50 Casas)\n4. Voltar ao Menu Principal\n')
    if (secondary_request == "1"):
        game(1,1,1,20)
    elif (secondary_request == "2"):
        game(1,1,1,35)
    elif (secondary_request == "3"):
        game(1,1,1,50)
    elif (secondary_request == "4") :
        main_menu()  
    
    

def game(turn,player1,player2,length) :
    # o jogo em si
    
    if (player1 >= length):
        print('\nVitória do Jogador 1!')
        end_screen()
    elif (player2 >= length):
        print('\nVitória do Jogador 2!')
        end_screen()
    else : pass

    # Eventos Especiais para o Jogador 1
    if (player1 == 2 or player1 == 21 or player1 == 24 or player1 == 37 or player1 == 47) :
        print('\n*EVENTO ESPECIAL*\nAvançe 3 Casas\n'), player1 == player1 + 3
    elif (player1 == 12 or player1 == 15 or player1 == 22 or player1 == 34 or player1 == 44) :
        print('\n*EVENTO ESPECIAL*\nVolte 2 Casas\n'), player1 == player1 - 2
    else: pass    

    # Eventos Especiais para o Jogador 2
    if (player2 == 2 or player2 == 21 or player2 == 24 or player2 == 37 or player2 == 47) :
        print('\n*EVENTO ESPECIAL*\nAvançe 3 Casas\n'), player2 == player2+ 3
    elif (player2 == 12 or player2 == 15 or player2 == 22 or player2 == 34 or player2 == 44) :
        print('\n*EVENTO ESPECIAL*\nVolte 2 Casas\n'), player2 == player2 - 2
    else : pass    

    print('\n\n*CORRIDA*\n\n')
    print(f'Jogador 1 (Você): {player1} de {length} casas')
    print(f'Jogador 2: {player2} de {length} casas')
    

    input('Pressione Enter para Continuar')
   
    if (turn == 1) :
        print('Vez do Jogador 1\n')
        roll_1(player1,player2,length)
    elif (turn == 2) :
        print('Vez do Jogador 2\n')
        roll_2(player1,player2,length)
    else : pass
  
               




# sistema talvez extra-complicado para rodar o dado e mudar de quem é o turno

def roll_1(p1,p2,length) :
    turn = 1
    generated_num = random.randint(1,6)
    p1 = p1 + generated_num
    if (generated_num == 6):
        print('O dado caiu no 6! um turno extra será concedido ao Jogador 1')
        input('Pressione Enter para continuar\n')
    else : turn = 2

    print(f'O Jogador 1 andará {generated_num} casas')
    input('Pressione Enter para continuar\n')

    game(turn,p1, p2, length)

def roll_2(p1,p2,length) : 
    turn = 2
    generated_num = random.randint(1,6)
    p2 = p2 + generated_num
    if (generated_num == 6):
        print('O dado caiu no 6! um turno extra será concedido ao Jogador 2\n')
    else : turn = 1

    print(f'O Jogador 2 andará {generated_num} casas')

    game(turn,p1, p2, length)   

    
def end_screen():
    # roda quando o jogo acaba
    
    answer = input('Jogo finalizado, quer jogar novamente? (y/n)\n')
    if (answer == "y"):
        main_menu()
    elif (answer == "n") :
        print('Finalizando o Programa'), exit()
    else: print('Digite uma opção válida')        
    


def main() :
    main_menu()


if __name__ == '__main__':
    main()