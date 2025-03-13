def main_menu():
 # menu principal

 print('\n*Jogo de Triângulos*\n')
 pl_answer = input('Escolha uma opção:\n1. Calcular um Triângulo\n2. Sair da Aplicação\n')
 if (pl_answer == "1"):
     value_input()
 elif(pl_answer == "2"):
     print('Finalizando o Programa'), exit() 
 else : print('\nEscolha uma Opção Válida'), main_menu()       
 


def value_input():
    # pega os três valores e chama o resto do código

    x_value = float(input('\nDeclare a medida do primeiro lado:\n')) 
    y_value = float(input('Declare a medida do segundo lado:\n'))
    z_value = float(input('Declare a medida do terceiro lado:\n'))

    validate_triangle(x_value,y_value,z_value)
    
    calc_permimeter(x_value,y_value,z_value)

    classify_triangle(x_value,y_value,z_value)

    enquire()


def calc_permimeter(x,y,z):
    # calcula o perímetro e arredonda ele caso seja decimal

    result = (x+y+z)
    rounded_result = round(result, 2)
    print(f'Perímetro : {rounded_result}\n')

def validate_triangle(x,y,z):
    # faz as validações pra garantir que o triângulo é de fato válido

    if (x <= 0 or y <= 0 or z <=0) :
        print('Medidas Inválidas, todos os valores devem ser diferentes ou maiores do que zero\n')
        enquire()
    elif (x + y < z or x + z < y or y + z < x) :
        print('Medidas Inválidas, a soma de quaisquer dois lados deve ser maior que o terceiro lado\n')
        enquire()
    else : print('\nO Triângulo é Válido\n')

def classify_triangle(x,y,z):
    # classifica o triângulo
    
    if (x == y == z):
        print('Tipo do Triângulo : Equilátero\n')
    elif (x == y != z):
        print('Tipo do Triângulo : Isósceles\n')
    elif (x == z != y):
        print('Tipo do Triângulo : Isósceles\n')
    elif (z == y != x):
        print('Tipo do Triângulo : Isósceles\n')  
    elif (x != y != z):
        print('Tipo do Triângulo : Escaleno\n') 
    else : print('Triãngulo Inválido\n'), enquire()


def enquire():
    resp = input('Voltar Ao Início? (y/n)\n')
    if (resp == "y"):
        main()
    elif (resp == "n"):
        print('Finalizando o Programa...')
        exit()      
    else : print('\nFavor fazer uma Escolha Válida\n'), enquire()
           

   
def main() :
    main_menu()


if __name__ == '__main__':
    main()