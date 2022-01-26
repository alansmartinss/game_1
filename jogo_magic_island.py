
import random
import time

time.sleep(1)
print('1')
time.sleep(1)
print('2')
time.sleep(1)
print('3')
time.sleep(1)
print('4')
time.sleep(1)
print('5')
time.sleep(1)
print('6')


print(f'-----------||||||||||||||||||||-----------\n'
    'Olá aventureiro(a)! '
      'Qual seu nome?')

nome = input('Digite seu nome:')

print(f'-----------||||||||||||||||||||-----------\n'
    f'Muito bem {nome} vamos começar nosso jogo!\n')
time.sleep(5)
print('Eu me chamo Alan, serei seu guia e mestre nesta jornada. \n')
time.sleep(5)
print('O objetivo neste teste é levar você á uma aventura semelhante a um')
print(f'RPG de mesa, onde serão disponibilizados algumas possibilidades de')
print(f'escolha de classe de personagem, e escolhas de tomadas de decisão.\n')
time.sleep(5)
print(f'Entretanto fique atento, pretendo lançar atualizações e melhorias,')
print(f'principalmente nos sistemas de atributos e ítens.\n')
time.sleep(5)
print(f'{nome}, primeiro passo, vamos escolher sua classe de jogador, elas são as seguintes:')
time.sleep(1)
print(f'1 - Guerreiro (personagem com foco em força e vitalidade)')
time.sleep(0.5)
print(f'2 - Mago (personagem com foco em mágia e poções de cura)')
time.sleep(0.5)
print(f'3 - Peso-morto (personagem sem foco em nenhuma habilidade, recomendado\n'
    f'apenas se quiser ter uma experiência de jogo com maior dificuldade) \n')

time.sleep(3)



classe = 0

def classejogador():
    global classe
    while True:
        try:
            classe = int(input('Digite o número de classe do personagem que você deseja jogar:'))
        except:
            print('Você não digitou um número')
            continue
        else:
            print('Ok, vamos nessaaaaaa!')
            break
        finally:
            print('...')
    print('...')


classejogador()


if classe == 1:
    forca = 20
    vitalidade = 20
    magia = 8
    pocao = 5

elif classe == 2:
    forca = 5
    vitalidade = 12
    magia = 16
    pocao = 15

elif classe == 3:
    forca = 3
    vitalidade = 5
    magia = 1
    pocao = 1

else:
    print('Você não escolheu uma classe!')

#Puxando o nome da classe para os demais passos

clas = classe
clas1 = 0

if clas == 1:
    clas1 = 'Gerreiro'

elif clas == 2:
    clas1 = 'Mago'

elif clas == 3:
    clas1 = 'Peso-morto'

elif clas != 1 or clas != 2 or clas != 3:
    print('Opção invalida!')
    time.sleep(2)
    print('Encerrando jogo')
    quit()

print('\n'
      '\n')
print(f'-----------||||||||||||||||||||-----------\n'
    f'Muito bem {nome}, agora você é um {clas1}! \n')
time.sleep(1)
print(f'Seus atributos são:')
time.sleep(1)
print(f'Força: {forca}')
time.sleep(1)
print(f'Vitalidade: {vitalidade}')
time.sleep(1)
print(f'Mágia: {magia}')
time.sleep(1)
print(f'Conhecimento em poções: {pocao}')


time.sleep(3)
print(f'Agora, então, {nome}, nós iremos nos teletransportar para uma terra distante, \n')
time.sleep(2)
print('onde o plano mistico, e o plano astral se convergem, e todo tipo de criatura mágica \n'
      'vive.')
time.sleep(3)
print('Alguns dos seres que você encontrar nesta jornada, podem ser passificos, com a \n'
      'intenção de ajudar, mas cuidado, alguns podem ser traiçoeiros, violentos ou imprudentes')
time.sleep(5)
print('...\n')
time.sleep(1)
print('...\n')
time.sleep(1)
print('...\n')
time.sleep(1)
print(f'Nobre {clas1}, agora vos convido a imaginar o cenários para que estamos indo')
time.sleep(2)
print('Uma ilha, com clima tropical....')
time.sleep(2)
print('O sol escaldante de um verão infernal')
time.sleep(2)
print('Que lhe causa nauseas pelo excesso de calor, e \n'
      'lhe faz sentir sede e cançasso extremo a qualquer esforço')
time.sleep(5)
print('Você está sozinho!')
time.sleep(2)

arma = 0

if clas == 1:
    arma = 'Machado'
elif clas == 2:
    arma = 'Grimório'
else:
    arma = 'Pedaço de madeira podre'

print(f'Leva consigo apenas seu {arma}')
time.sleep(15)
print('Como tentativa de sobrevivência, entra para dentro da ilha onde')
time.sleep(3)
print('se pode ver a entrada de uma floresta')
time.sleep(3)
print('Ao entrar na floresta você se depara com um Ork')
time.sleep(3)
print('...')
time.sleep(3)
print('...')
time.sleep(3)
print('Orks são criaturas violentas e semi-irracionais')
time.sleep(2)
print('Você terá de ataca-lo, ou correr para fugir!')
time.sleep(3)
print('O que você fará?')
time.sleep(2)
print('...')
time.sleep(1)
print('...')
time.sleep(1)
print('...')
time.sleep(1)

acao1 = 0

def ato1():
    global acao1
    while True:
        try:
            acao1 = int(input('Digite 1 para enfrenta-lo ou 2 para fugir:'))
        except:
            print('Você não digitou um número')
            continue
        else:
            print('Ok, vamos nessaaaaaa!')
            break
        finally:
            print('...')
    print('...')


ato1()

if acao1 == 2:
    print('Ao tentar fugir seu inimigo joga um pedregulho em sua direção,'
          'e você morre esmagado!')
    time.sleep(3)
    print(f'{clas1}, sua escolha não foi sábia \n '
          f'fugir de um inimigo é um ato covarde até mesmo para\n'
          f'doentes e moribundos')
    print('...')
    time.sleep(3)
    print(f'SUA JORNADA ACABA AQUI, ADEUS {nome}')
    quit()

elif acao1 == 1:
    print(f'Então, você avança com seu {arma}, para cima do inimigo!')
    time.sleep(2)
    print('...')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('...')
    time.sleep(1)

else:
    print('Você não tomou nenhuma opção que lhe foi concedida?' )
    time.sleep(3)
    print('Porque?')
    time.sleep(2)
    print('Seu inimigo o avista distraído e o devora!')
    time.sleep(2)
    print('...')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print(f'{nome} este é o fim de sua jornada! \n'
          f'ADEUS!')
    quit()

inimigo1 = 4

print(f'Quando se aproxima, percebe que o inimigo possui apenas {inimigo1} pontos de vida \n'
      f'Você possuí {vitalidade} pontos de vitalidade.')
print('...')
time.sleep(1)
print('...')
time.sleep(1)
print('...')
time.sleep(1)

print('Então você o ataca!')

inimigo1 = inimigo1 - forca

while True:
    if inimigo1 > 0:
        print('Ele ainda não morreu, então ele te golpeia de volta te causando dano!')
        vitalidade = vitalidade - 1
        print(f'Você possuí {vitalidade} pontos de vitalidade.')
        time.sleep(1)
        print('Mas você ataca novamente!')
        time.sleep(1)
        print('...')
        time.sleep(1)
        print('...')
        time.sleep(1)
        print('...')
        inimigo1 = inimigo1 - forca

        if vitalidade == 0:
            print(f'Nobre {clas1} você foi derrotado em combate!')
            time.sleep(2)
            print('Sua jornada acaba aqui! ADEUS!')
            quit()

    else:
        print('Muito bem derrotamos nosso primeiro inimigo')
        break

time.sleep(3)
print('...')
time.sleep(1)
print('...')
time.sleep(1)
print('...')
time.sleep(1)
print('...')
time.sleep(1)
print('...')
time.sleep(1)
print('Então você continua a caminhar...')
time.sleep(2)
print('Quando de repente, se depara com uma criatura estranha')
time.sleep(2)
print('Pequenina como um anão, mas magra como um elfo....')
time.sleep(3)
print('A criatura, então, com uma expressão doce,')
time.sleep(2)
print('Lhe oferece um frasco com um líquido vermelho dentro')
time.sleep(2)
print('Você aceita beber deta poção? - pergunta a criatura com uma voz amedrontada')
time.sleep(4)

def decisao1():
    global escolha1
    while True:
        try:
            escolha1 = int(input('Digite 1 para aceitar, ou 2 para negar: '))
        except:
            print('Você não digitou um número')
            continue
        else:
            print('Ok!')
            break
        finally:
            print('...')
    print('...')

decisao1()

time.sleep(3)

if escolha1 == 1:
    print(f'Ao beber a poção você percebe que aquilo era um tônico de cura')
    time.sleep(3)
    print(f'Seus atributos que eram: \n'
          f'Vitalidade: {vitalidade}')
    time.sleep(3)
    vitalidade = vitalidade + random.randrange(1,5)
    print(f'Passam a ser:\n'
          f'Vitalidade = {vitalidade}')
    time.sleep(2)
    print(f'Então a criatura desaparece diante dos seus olhos')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print(f'Ao fundo você consegue ouvir um sussuro:')
    time.sleep(1)
    print(f'Te desejo sorte nesta jornada, ó nóbre {clas1}!')

elif escolha1 == 2:
    print('Ao negar a poção, acriatura desaparece diante dos seus olhos')

else:
    print('Por sua indecisão na escolha a criatura foge para mata adentro...')

time.sleep(1)
print('...')
time.sleep(1)
print('...')
time.sleep(1)
print('...')
time.sleep(1)
print('...')
time.sleep(1)
print('...')
time.sleep(1)
print('...')
time.sleep(1)
print('...')
time.sleep(1)
print('...')
time.sleep(1)
print('...')
time.sleep(1)
print('Caminhando, mais afrente, você se depara com um Espectro')
time.sleep(1)
print('Estas criaturas, que não pertencem ao plano físico, só podem \n'
      'ser derrotados com o uso de mágia ')
time.sleep(3)
print(f'Você irá enfrenta-lo {nome}?')
time.sleep(2)

escolha2 = 0

def decisao2 ():
    global escolha2
    while True:
        try:
            escolha2 = int(input('Digite 1 para enfrenta-lo '
                             'ou 2 para fugir: '))
        except:
            print('Você, não digitou um número')
            continue
        else:
            print('OK!')
            break
        finally:
            print('...')

decisao2()

if escolha2 == 1:
    print(f'Muito bem, então você ataca seu inimigo com seu {arma}')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('...')

    inimigo2 = 16
    inimigo2 = inimigo2 - magia

    while True:
        if inimigo2 > 0:
            print('Ele ainda não morreu, então ele te golpeia de volta te causando dano!')
            vitalidade = vitalidade - 3
            print(f'Você possuí {vitalidade} pontos de vitalidade.')
            time.sleep(1)
            print('Mas você ataca novamente!')
            time.sleep(1)
            print('...')
            time.sleep(1)
            print('...')
            time.sleep(1)
            print('...')
            inimigo2 = inimigo2 - magia

            if vitalidade == 0:
                print(f'Nobre {clas1} você foi derrotado em combate!')
                time.sleep(2)
                print('Sua jornada acaba aqui! ADEUS!')
                quit()

        else:
            print('Muito bem derrotamos o inimigo')
            break


elif escolha2 == 2 and clas ==3:
    print(f'Muito bem {nome}, você sabe que é um inutil,\n'
          'desta vez foi sábia a decisão de fugir!')

elif escolha2 == 2 and clas != 3:
    print(f'{nome}, fuga é uma decisão para fracos!\n'
          f'Este jogo não é´para covardes')
    time.sleep(2)
    print('Sua escolha o torna indigno de continuar!\n'
          'A jornada termina aqui!\n'
          'ADEUS')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print(f'Que neste reino, o nome de {nome} fique conhecido como sinônimo de covardia!')
    time.sleep(1)
    print('GAME OVER')
    quit()

else:
    print('Sua indecisão ao escolher da brecha ao inimigo!')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('Enquanto você etá distraido ele te ataca e sua jornada aqui termina')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print(f'Procure ser mais atencioso em sua próxima jornada {clas1}')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('ADEUS!')
    quit()

time.sleep(1)
print('...')
time.sleep(1)
print('...')
time.sleep(1)
print('...')
time.sleep(1)
print('...')
time.sleep(1)
print('...')
time.sleep(1)
print('...')

print('Caminhando um pouco mais, você se depara com uma bruxa')
time.sleep(3)
print('Ela então começa a falar:')
time.sleep(3)
print(f'Nóbre {clas1}, vejo que está perdido, está é uma ilha amaldiçoada')
time.sleep(3)
print('existem dois caminhos, subir até a colina e encontrar')
time.sleep(3)
print('o cálice que contém a agua dívina, que ao toma-la, será levado para casa,')
time.sleep(3)
print('ou, posso eu mesma te levar para casa com esta poção que tenho aqui...')
time.sleep(3)
print('O que você deseja, aventureiro?')

escolha3 = 0

def decisao3 ():
    global escolha3
    while True:
        try:
            escolha3 = int(input('Digite 1 para se aventurar em busca do cálice \n'
                             'ou 2 para tomar a poção oferecida: '))
        except:
            print('Você, não digitou um número')
            continue
        else:
            print('...')
            break
        finally:
            print('\n')

decisao3()

if escolha3 == 1:
    time.sleep(2)
    print('Então a bruxa diz: Muito bem!')
    time.sleep(2)
    print('Siga a diante, no topo da montanha deve se encontrar o Cálice')
    time.sleep(2)
    print(f'{nome}, você tem coragem e escolhe sabiamente, lhe lancarei um feitiço')
    time.sleep(2)
    print('que melhorará seus atributos')
    time.sleep(2)
    print('(Palavras ditas numa lingua desconhecida)')
    time.sleep(2)
    print(f'Seus atributos que eram:\n'
          f'Vitalidade = {vitalidade}\n'
          f'Força = {forca}\n'
          f'Magia = {magia}\n')
    vitalidade = vitalidade + random.randrange(1,3)
    forca = forca + random.randrange(1,3)
    magia = magia + random.randrange(1,3)
    time.sleep(3)
    print(f'Passam a ser:\n'
          f'Vitalidade = {vitalidade}\n'
          f'Força = {forca}\n'
          f'Magia = {magia}\n')
elif escolha3 == 2:
    print('A bruxa então: Muito bem aventureiro sua jornada acaba aqui')
    time.sleep(2)
    print('Lhe dá a poção...')
    time.sleep(2)
    if pocao == 15:
            print('Como bom mago você vê que é uma possão de veneno,e não atoma')
            time.sleep(3)
            print('Então a bruxa diz: Muito bem, você é sábio')
            time.sleep(2)
            print('siga até o topo da montanha, lá estará o cálice!')
    else:
            escolha4 = 0
            def decisao4 ():
                global escolha4
                while True:
                    try:
                        escolha4 = int(input('Digite 1 para tomar, ou 2 para largar, \n'
                                             'e correr em direção a uma colina que você avista ao longe: '))
                    except:
                        print('Você não gigitou uma opção valida!')
                        continue
                    else:
                        break
                    finally:
                        print('\n')
            decisao4()
            if escolha4 == 1:
                print('Ao tomar a poção você sente seu corpo queimar,\n'
                      'e percebe que na verdade aquilo era um veneno')
                time.sleep(3)
                print('Sua jornada acaba aqui aventureiro,')
                time.sleep(3)
                print('lhe foi avisado que alguns seres aqui eram traiçoeiros')
                time.sleep(3)
                print('ADEUS\nGAME OVER')
                quit()
            elif escolha4 == 2:
                print('Então você larga a poção e corre em direção a colina')
            else:
                print(f'{nome} sua indecisão a esta altura da aventura')
                print(f'o torna indigno de continuar!')
                print(f'ADEUS')
                print(f'GAME OVER')
                quit()
else:
    print('Sua indecisão ao escolher irrta a bruxa!')
    time.sleep(2)
    print('Então ela lança sobre você um feitiço')
    time.sleep(2)
    print('Que o transforma em pedra')
    time.sleep(3)
    print('Agora você está preso aqui para sempre')
    time.sleep(3)
    print('Este é o fim de sua jornada, adeus aventureiro')
    time.sleep(2)
    quit()

time.sleep(3)
print('...')
time.sleep(1)
print('...')
time.sleep(1)
print('...')
time.sleep(1)
print('...')
time.sleep(1)
print('...')
time.sleep(1)
print('Chegando lá, você avista um altar')
time.sleep(3)
print('Em cima do altar há um calice')
time.sleep(3)
print('Ao ir em direção ao altar...repentinamente surge um drgão')
time.sleep(3)
print(f'{nome}, você terá de enfrenta-lo para poder beber do cáice \n'
      f'e assim poder sair desta ilha!')
time.sleep(3)
print(f'Você o enfrentará?')


escolha4 = 0

def decisao4 ():
    global escolha4
    while True:
        try:
            escolha4 = int(input('Digite 1 para enfrenta-lo \n'
                             'ou 2 para tentar fugir: '))
        except:
            print('Você, não digitou um número')
            continue
        else:
            print('OK!')
            break
        finally:
            print('\n')

decisao4()

if escolha4 == 1:
    print('Então você avança para cima do inimigo!')
    time.sleep(2)
    print('...')
    time.sleep(2)
    print('...')
    time.sleep(2)
    print('...')

elif escolha4 == 2:
    print('Ao tentar fugir o dragão te ataca pelas costas')
    time.sleep(2)
    print('Nobre aventureiro, sua aventura acaba aqui')
    time.sleep(4)
    print('Obrigado por jogar \nGAME OVER')
    quit()
else:
    print('Não é hora para indecisão')
    time.sleep(3)
    print('Você não é digno de continuar')
    time.sleep(2)
    print('GAME OVER')
    quit()


dragvit = 40
dragmaf = 30

while True:
    if dragvit > 0 or dragmaf > 0:
        print('Ele ainda não morreu, então ele te golpeia de volta te causando dano!')
        vitalidade = vitalidade - 4
        print(f'Você possuí {vitalidade} pontos de vitalidade.')
        time.sleep(1)
        print('Mas você ataca novamente!')
        time.sleep(1)
        print('...')
        time.sleep(1)
        print('...')
        time.sleep(1)
        print('...')
        dragvit = dragvit - forca
        dragmaf = dragmaf - magia
        print(dragvit)
        print(dragmaf)

        if vitalidade < 0:
            print(f'Nobre {clas1} você foi derrotado em combate!')
            time.sleep(2)
            print('Sua jornada acaba aqui! ADEUS!')
            quit()

    else:
        print('Muito bem derrotamos o dragão')
        break

time.sleep(3)
print('...')
time.sleep(1)
print('...')
time.sleep(1)
print('...')
time.sleep(1)
print('...')
time.sleep(1)
print('Agora vpcê pode beber do cálice!')
time.sleep(3)
print('Este na verdade é a magia que te levará de volta ao seu mundo!')
time.sleep(3)
print('Aqui é o final de sua jornada!')
time.sleep(3)
print('Se tiver interesse, refaça sua aventura,')
time.sleep(3)
print('faça escolhas diferentes!')
time.sleep(3)
print('Muito obrigado por participar desta jornada!')
time.sleep(3)
print('Se hover idéias, de melhorias, ajustes e/ou problemas a reportar,')
time.sleep(3)
print('peço que entre em contato com o email: alan.martins.silva@outlook.com')
time.sleep(3)
print('Espero que tenha aproveitado a brincadira')
time.sleep(3)
quit()
