from Classes import *
import os

hotel = Hotel("Enchanted Echo Resort")

def descrição_hotel(hotel):
    print("Nosso hotel: \n \n Bem-vindo ao Enchanted Echo Resort, onde a magia encontra o conforto. \n Situado em um cenário deslumbrante, nosso resort oferece uma experiência encantadora que combina luxo com natureza. \n Cada detalhe do nosso espaço, desde a arquitetura até os jardins bem cuidados, é projetado para criar uma atmosfera mágica e relaxante. \n Nossos quartos e suítes foram concebidos para serem verdadeiros refúgios, com decoração elegante e conforto incomparável. \n As vistas panorâmicas da natureza exuberante que nos rodeia são um espetáculo à parte. \n O Enchanted Echo Resort é o lugar perfeito para se desconectar do mundo e se conectar com a serenidade da natureza. \n")

def serviços(hotel):
    print("No coração de uma paisagem deslumbrante, onde a natureza encontra o luxo, convidamos você a vivenciar uma experiência única. \nCom uma mistura perfeita de encanto e conforto, nosso resort é um refúgio verdadeiramente mágico para os viajantes mais exigentes. \nAqui, sua jornada começa em um lugar onde cada detalhe foi cuidadosamente planejado para criar memórias inesquecíveis.")
    print("\n \n Serviços Exclusivos: \n \n 1. Acomodações de Sonho: Nossos quartos são um oásis de relaxamento, com uma variedade de opções para atender às suas necessidades.  \n Desde os quartos aconchegantes até as suítes luxuosas, cada espaço é projetado para combinar conforto e estilo. \n \n 2. Gastronomia de Classe Mundial: Deleite-se com uma experiência culinária excepcional em nossos restaurantes requintados. \n Nossos chefs talentosos combinam ingredientes frescos e sabores inspiradores para criar pratos que cativam os sentidos. \n \n 3. Spa do Éden: Mime-se no nosso spa de classe mundial, onde a tranquilidade encontra a renovação. \n Com uma gama de tratamentos relaxantes e terapêuticos, você vai emergir rejuvenescido e revigorado. \n \n 4. Atividades ao Ar Livre: Explore a beleza natural que nos rodeia através de atividades emocionantes. \n Trilhas, passeios de bicicleta e passeios pela natureza estão disponíveis para todos os amantes da aventura. \n \n 5. Piscinas e Recreação: Relaxe à beira da piscina sob o sol cintilante ou desfrute de nossas instalações recreativas para \n momentos divertidos em família. \n Há algo para todos, desde nadar até jogos emocionantes. \n \n 6. Eventos Inesquecíveis: Seja um casamento de conto de fadas ou uma reunião de negócios sofisticada, \n nossos espaços versáteis e serviços de planejamento garantirão que seu evento seja memorável e perfeitamente executado. \n \n 7. Equipe Atenciosa: Nossa equipe dedicada está à disposição para atender a todas as suas necessidades, \n garantindo que cada momento da sua estadia seja excepcional. \n \n \n Desperte a Magia: \n \n \n No Enchanted Echo Resort, nossos serviços transcendem a hospitalidade comum. \n Cada detalhe foi pensado para criar uma experiência onde você possa se desconectar do mundo exterior e se conectar com a beleza, \n o conforto e a serenidade que nos cercam. \n Seja uma escapada romântica, uma celebração especial ou uma pausa relaxante, embarque em uma jornada encantadora no Enchanted Echo Resort, onde a magia é mais do que uma palavra, é uma realidade que você pode viver.")

def listar_apartamentos(hotel):
    quartos_disponiveis = hotel.listar_quartos_disponiveis()
    for quarto in quartos_disponiveis:
        print(quarto.obter_detalhes_quarto())


def simples():
    for numero_quarto in range(1, 5):
        hotel.adicionar_quarto(ApartamentoSimples(numero_quarto))
    return hotel
def simplescasal():
    for numero_quarto in range(1, 5):
        hotel.adicionar_quarto(ApartamentoSimplesCasal(numero_quarto))
def duplo():
    for numero_quarto in range(1, 5):
        hotel.adicionar_quarto(ApartamentoDuplo(numero_quarto))
def duplocasal():
    for numero_quarto in range(1, 5):
        hotel.adicionar_quarto(ApartamentoDuploCasal(numero_quarto))
def luxo():
    for numero_quarto in range(1, 5):
        hotel.adicionar_quarto(ApartamentoLuxo(numero_quarto))
def master():
    for numero_quarto in range(1, 5):
        hotel.adicionar_quarto(ApartamentoMaster(numero_quarto))

def fazer_reserva(hotel):
    nome_cliente = input("Digite seu nome: ")
    quant_dias = int(input("Duração da estadia (em dias): "))
    quarto_desejado =  int(input("Qual quarto deseja: "))

    quartos_disponiveis = hotel.listar_quartos_disponiveis()
    
    if quartos_disponiveis:
        quarto_escolhido = quartos_disponiveis[quarto_desejado]  # Escolhe o primeiro quarto disponível
        valor_total = quarto_escolhido.preco * quant_dias
        quarto_escolhido.esta_reservado = True

        print(f"Olá, {nome_cliente}! Sua reserva foi feita por R${valor_total}. Tenha uma ótima estadia!")
    else:
        print("Quartos indisponíveis")


def main():
    while True:
        try:
            print("+------------------------------------------+ \n | BEM VINDO(A) AO ENCHANTED ECHO RESORT! | \n+------------------------------------------+ \n [1] Descrição do Hotel \n [2] Serviços disponíveis \n [3] Apartamentos disponíveis \n [4] Realizar reserva \n [5] Cancelar reserva \n [6] Sair")

            escolha = int(input("> "))

            if escolha == 1:
                os.system("cls")
                descrição_hotel(hotel)
                os.system("pause")
                os.system("cls")

            elif escolha == 2:
                os.system("cls")
                serviços(hotel)
                os.system("pause")
                os.system("cls")

            elif escolha == 3:
                os.system("cls")
                try:
                    menu_listar = int(input("Qual quarto deseja ver?\n[1] - Quarto Simples\n[2] - Quarto Simples Casal\n[3] - Quarto Duplo\n[4] - Quarto Duplo Casal\n[5] - Quarto de Luxo\n[6] - Quarto Master\n> "))
                
                    if menu_listar == 1:
                        simples()
                    elif menu_listar == 2:
                        simplescasal()
                    elif menu_listar == 3:
                        duplo()
                    elif menu_listar == 4:
                        duplocasal()
                    elif menu_listar == 5:
                        luxo()
                    elif menu_listar == 6:
                        master()
                    else:
                        print("Opção Invalida!")
                except ValueError:
                    print("Erro de Digito, digite um número de 1 a 6!")
                os.system("pause")
                os.system("cls")

            elif escolha == 4:
                os.system("cls")
                fazer_reserva(hotel)
                os.system("pause")
                os.system("cls")

            else:
                print("Opção inválida.")


        except ValueError:
            print('Problema: Digito não correspondente/ Opção Indisponível')