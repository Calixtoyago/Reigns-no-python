import sys
import os
from random import randint, shuffle, choice
from time import sleep


#atributos
class Atributos:
    def __init__(self):
        self.economia = 50
        self.igreja = 50
        self.exercito = 50
        self.populacao = 50

    def exibir_atributos(self):
        print(f'Dificuldade: {modos[int(dificuldade) - 1]}')
        print('-=' * 15)
        print(
            f'Economia = {self.economia} \nIgreja = {self.igreja} \nExército = {self.exercito} \nPopulação = {self.populacao}')
        print('-=' * 15)


# função slowprint
def slowprint(s, tempo):
    for char in (s):
        sys.stdout.write(char)
        sys.stdout.flush()
        if char != '\n':
            sleep(tempo)
        else:
            sleep(0.6)
    sleep(1)


# apagar o terminal
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


# apagar e printar algo
def limpar_e_printar(mensagem):
    clear_screen()
    print(mensagem)


titulo = '''
    ██████╗ ███████╗██╗ ██████╗ ███╗   ██╗███████╗
    ██╔══██╗██╔════╝██║██╔════╝ ████╗  ██║██╔════╝
    ██████╔╝█████╗  ██║██║ ████║██╔██╗ ██║███████╗
    ██╔══██╗██╔══╝  ██║██║   ██║██║╚██╗██║╚════██║
    ██║  ██║███████╗██║╚██████╔╝██║ ╚████║███████║
    ╚═╝  ╚═╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
    '''

atributos = Atributos()
escolha = 0


#os eventos dos npcs
def Padre1():
    escolha = 0
    while escolha != '1' and escolha != '2':
        slowprint('PADRE: Os fiéis querem que você dê uma palavra na Igreja.', 0.05)
        escolha = input('''\n
[1] Não me importo, a fé é para os fracos -> Igreja - / Exercito +
[2] Tudo bem, vou falar com os fiéis -> Igreja + / Exercito -
>>>  ''')
        if escolha == '1':
            atributos.igreja -= randint(menor, maior)
            atributos.exercito += randint(menor, maior)
            break
        elif escolha == '2':
            atributos.exercito -= randint(menor, maior)
            atributos.igreja += randint(menor, maior)
            break


def Rainha():
    escolha = 0
    while escolha != '1' and escolha != '2':
        slowprint('RAINHA: Eu quero que meu trono seja de ouro, providencie isso!', 0.05)
        escolha = input('''\n
[1] Coloque-se no seu lugar, eu sou o Rei aqui -> Economia + / População -
[2] Qualquer coisa para te ver feliz -> Economia - / População +
>>> ''')
        if escolha == '1':
            atributos.economia += randint(menor, maior)
            atributos.populacao -= randint(menor, maior)
            break
        elif escolha == '2':
            atributos.economia -= randint(menor, maior)
            atributos.populacao += randint(menor, maior)
            break


def General1():
    escolha = 0
    while escolha != '1' and escolha != '2':
        slowprint('GENERAL: Tá cheio de pessoas na frente do castelo, o que devemos fazer?', 0.05)
        escolha = input('''\n
[1] Matem todos, não quero ninguém tirando minha paz -> Exército + / População -
[2] Deixem-os entrar, vamos ouvir o que têm a dizer -> Exército - / População +
>>> ''')
        if escolha == '1':
            atributos.exercito += randint(menor, maior)
            atributos.populacao -= randint(menor, maior)
            break
        elif escolha == '2':
            atributos.exercito -= randint(menor, maior)
            atributos.populacao += randint(menor, maior)
            break


def Bruxa():
    escolha = 0
    while escolha != '1' and escolha != '2':
        slowprint('BRUXA: Descobri como transformar pedra em ouro, posso ensinar a população?', 0.05)
        escolha = input('''\n
[1] Vá em frente, precisamos de dinheiro -> Economia + / Igreja -
[2] Jamais, isso é contra as palavras da Igreja -> Economia - / Igreja +
>>> ''')
        if escolha == '1':
            atributos.economia += randint(menor, maior)
            atributos.igreja -= randint(menor, maior)
            break
        if escolha == '2':
            atributos.economia -= randint(menor, maior)
            atributos.igreja += randint(menor, maior)
            break


def Ferreiro():
    escolha = 0
    while escolha != '1' and escolha != '2':
        slowprint('FERREIRO: O estoque de ferro está acabando, devemos comprar do reino vizinho', 0.05)
        escolha = input('''\n
[1] Comprar ferro no reino vizinho -> Economia - / Exército +
[2] Nós temos o bastante, se vire -> Economia + / Exército -
>>> ''')
        if escolha == '1':
            atributos.economia -= randint(menor, maior)
            atributos.exercito += randint(menor, maior)
            break
        if escolha == '2':
            atributos.economia += randint(menor, maior)
            atributos.igreja -= randint(menor, maior)
            break


def General2():
    escolha = 0
    while escolha != '1' and escolha != '2':
        slowprint('GENERAL: Precisamos de reforços, posso recrutar a população?', 0.05)
        escolha = input('''\n
[1] Pode, precisamos de mais forças -> Exército + / População -
[2] Vou fingir que não escutei isso  -> Exército - / População +
>>> ''')
        if escolha == '1':
            atributos.exercito += randint(menor, maior)
            atributos.populacao -= randint(menor, maior)
            break
        if escolha == '2':
            atributos.exercito -= randint(menor, maior)
            atributos.populacao += randint(menor, maior)
            break


def Mendigo():
    escolha = 0
    while escolha != '1' and escolha != '2':
        slowprint('MENDIGO: Muitos estão sofrendo de fome nas ruas.', 0.05)
        escolha = input('''\n
[1] Distribuir comida -> População + / Economia -
[2] Ignorar o problema -> População - / Economia +
>>> ''')
        if escolha == '1':
            atributos.populacao += randint(menor, maior)
            atributos.economia -= randint(menor, maior)
            break
        if escolha == '2':
            atributos.populacao -= randint(menor, maior)
            atributos.economia += randint(menor, maior)
            break


def Mercenario():
    escolha = 0
    while escolha != '1' and escolha != '2':
        slowprint('MERCENÁRIO: Fomos contratados para proteger seu reino, precisamos de pagamento.', 0.05)
        escolha = input('''\n
[1] Pague os mercenários -> Economia - / Exercito +
[2] Não precisamos de mercenários -> Economia + / Exercito -
>>> ''')
        if escolha == '1':
            atributos.economia -= randint(menor, maior)
            atributos.exercito += randint(menor, maior)
            break
        if escolha == '2':
            atributos.economia += randint(menor, maior)
            atributos.exercito -= randint(menor, maior)
            break


def Arcebispo():
    escolha = 0
    while escolha != '1' and escolha != '2':
        slowprint('ARCEBISPO: A igreja deve ter um papel maior no governo.', 0.05)
        escolha = input('''\n
[1] Deixe a igreja governar mais -> Igreja + / População -
[2] Mantenha a separação -> Igreja - / População +
>>> ''')
        if escolha == '1':
            atributos.igreja += randint(menor, maior)
            atributos.populacao -= randint(menor, maior)
            break
        if escolha == '2':
            atributos.igreja -= randint(menor, maior)
            atributos.populacao += randint(menor, maior)
            break


def Templario():
    escolha = 0
    while escolha != '1' and escolha != '2':
        slowprint('TEMPLÁRIO: Precisamos de recursos para proteger os locais sagrados.', 0.05)
        escolha = input('''\n
[1] Financie os templários -> Economia - / Igreja +
[2] Não há fundos disponíveis -> Economia + / Igreja -
>>> ''')
        if escolha == '1':
            atributos.economia -= randint(menor, maior)
            atributos.igreja += randint(menor, maior)
            break
        if escolha == '2':
            atributos.economia += randint(menor, maior)
            atributos.igreja -= randint(menor, maior)
            break


def Evangelista():
    escolha = 0
    while escolha != '1' and escolha != '2':
        slowprint('EVANGELISTA: Desejo fazer uma campanha de conversão entre os soldados.', 0.05)
        escolha = input('''\n
[1] Apoie a campanha -> Igreja + / Exercito -
[2] Os soldados têm outras prioridades -> Igreja - / Exercito +
>>> ''')
        if escolha == '1':
            atributos.igreja += randint(menor, maior)
            atributos.exercito -= randint(menor, maior)
            break
        if escolha == '2':
            atributos.igreja -= randint(menor, maior)
            atributos.exercito += randint(menor, maior)
            break


def Pregador():
    escolha = 0
    while escolha != '1' and escolha != '2':
        slowprint('PREGADOR: Quero pregar nas ruas para aumentar a fé do povo.', 0.05)
        escolha = input('''\n
[1] Espero que mais pessoas se juntem a Igreja -> Igreja + / População -
[2] Não queremos tumultos -> Igreja - / População +
>>> ''')
        if escolha == '1':
            atributos.igreja += randint(menor, maior)
            atributos.populacao -= randint(menor, maior)
            break
        if escolha == '2':
            atributos.igreja -= randint(menor, maior)
            atributos.populacao += randint(menor, maior)
            break


def Comerciante():
    escolha = 0
    while escolha != '1' and escolha != '2':
        slowprint('COMERCIANTE: Podemos aumentar os impostos sobre mercadorias importadas?', 0.05)
        escolha = input('''\n
[1] Sim, precisamos de mais dinheiro -> Economia + / População -
[2] Não, a população não vai gostar -> Economia - / População +
>>> ''')
        if escolha == '1':
            atributos.economia += randint(menor, maior)
            atributos.populacao -= randint(menor, maior)
            break
        if escolha == '2':
            atributos.economia -= randint(menor, maior)
            atributos.populacao += randint(menor, maior)
            break


def Cientista():
    escolha = 0
    while escolha != '1' and escolha != '2':
        slowprint('CIENTISTA: Descobri uma nova tecnologia que pode beneficiar o exército.', 0.05)
        escolha = input('''\n
[1] Investir na tecnologia -> Economia - / Exercito +
[2] Ignorar a descoberta -> Economia + / Exercito -
>>> ''')
        if escolha == '1':
            atributos.economia -= randint(menor, maior)
            atributos.exercito += randint(menor, maior)
            break
        if escolha == '2':
            atributos.economia += randint(menor, maior)
            atributos.exercito -= randint(menor, maior)
            break


def Tesoureiro():
    escolha = 0
    while escolha != '1' and escolha != '2':
        slowprint('TESOUREIRO: Devemos investir na construção de uma nova catedral para atrair mais fiéis?', 0.05)
        escolha = input('''\n
[1] Sim, construí-la fortalecerá nossa fé -> Economia - / Igreja +
[2] Não, precisamos desses recursos para outras coisas -> Economia + / Igreja -
>>> ''')
        if escolha == '1':
            atributos.economia -= randint(menor, maior)
            atributos.igreja += randint(menor, maior)
            break
        if escolha == '2':
            atributos.economia += randint(menor, maior)
            atributos.igreja -= randint(menor, maior)
            break


def Sacerdotista():
    escolha = 0
    while escolha != '1' and escolha != '2':
        slowprint('SACERDOTISTA: Devemos realizar um grande festival religioso para unir o povo?', 0.05)
        escolha = input('''\n
[1] Realizar o festival -> Igreja + / População -
[2] Não, é muito caro -> Igreja - / População +
>>> ''')
        if escolha == '1':
            atributos.igreja += randint(menor, maior)
            atributos.populacao -= randint(menor, maior)
            break
        if escolha == '2':
            atributos.igreja -= randint(menor, maior)
            atributos.populacao += randint(menor, maior)


def Cardeal():
    escolha = 0
    while escolha != '1' and escolha != '2':
        slowprint('CARDEAL: Devemos organizar uma benção especial para os soldados antes da batalha?', 0.05)
        escolha = input('''\n
[1] Organizar a benção -> Igreja + / Exercito -
[2] Focar nos preparativos militares -> Igreja - / Exercito +
>>> ''')
        if escolha == '1':
            atributos.igreja += randint(menor, maior)
            atributos.exercito -= randint(menor, maior)
            break
        if escolha == '2':
            atributos.igreja -= randint(menor, maior)
            atributos.exercito += randint(menor, maior)
            break


def Lider_Guilda():
    escolha = 0
    while escolha != '1' and escolha != '2':
        slowprint(
            'LÍDER DA GUILDA: Os comerciantes querem formar uma guarda para proteger suas caravanas. Podemos permitir isso?',
            0.05)
        escolha = input('''\n
[1] Permitir a formação da guarda -> Exercito + / População -
[2] Não, isso é trabalho do exército -> Exercito - / População +
>>> ''')
        if escolha == '1':
            atributos.exercito += randint(menor, maior)
            atributos.populacao -= randint(menor, maior)
            break
        if escolha == '2':
            atributos.exercito -= randint(menor, maior)
            atributos.populacao += randint(menor, maior)
            break


def Populacao():
    escolha = 0
    while escolha != '1' and escolha != '2':
        slowprint(
            'COMERCIANTE: Os habitantes estão clamando por um aumento nos salários para melhorar o padrão de vida.',
            0.05)
        escolha = input('''\n
[1] Aumentar os salários -> População ++
[2] Manter os salários atuais -> População --
>>> ''')
        if escolha == '1':
            atributos.populacao += randint(menosmenos, maismais)
            break
        if escolha == '2':
            atributos.populacao -= randint(menosmenos, maismais)
            break


def Economia():
    escolha = 0
    while escolha != '1' and escolha != '2':
        slowprint(
            'MERCADOR AMBULANTE: Uma rota comercial lucrativa foi descoberta, precisamos enviar caravanas para começar as negociações.',
            0.05)
        escolha = input('''\n
[1] Enviar caravanas -> Economia ++
[2] Não enviar caravanas -> Economia --
>>> ''')
        if escolha == '1':
            atributos.economia += randint(menosmenos, maismais)
            break
        if escolha == '2':
            atributos.economia -= randint(menosmenos, maismais)
            break


def Exercito():
    escolha = 0
    while escolha != '1' and escolha != '2':
        slowprint(
            'CAPITÃO DA GUARDA: Uma oportunidade de treinamento avançado para nossas tropas surgiu, mas isso exigirá um investimento considerável.',
            0.05)
        escolha = input('''\n
[1] Investir no treinamento avançado -> Exército ++
[2] Ignorar a oportunidade de treinamento -> Exército --
>>> ''')
        if escolha == '1':
            atributos.exercito += randint(menosmenos, maismais)
            break
        if escolha == '2':
            atributos.exercito -= randint(menosmenos, maismais)
            break


def Igreja():
    escolha = 0
    while escolha != '1' and escolha != '2':
        slowprint(
            'ABADE: Os fiéis estão pedindo por uma grande peregrinação religiosa, que poderia aumentar a devoção, mas também terá custos significativos.',
            0.05)
        escolha = input('''\n
[1] Organizar a peregrinação -> Igreja ++
[2] Desconsiderar a peregrinação -> Igreja --
>>> ''')
        if escolha == '1':
            atributos.igreja += randint(menosmenos, maismais)
            break
        if escolha == '2':
            atributos.igreja -= randint(menosmenos, maismais)
            break


def Divina():
    escolha = 0
    while escolha != '1':
        slowprint('VISÃO DIVINA: Você recebe uma visão divina que promete prosperidade e proteção ao reino.', 0.05)
        escolha = input('''\n
[1] Aceitar e seguir a orientação da visão -> Todos os atributos ++
>>> ''')
        if escolha == '1':
            atributos.igreja += randint(menosmenos, maismais)
            atributos.exercito += randint(menosmenos, maismais)
            atributos.economia += randint(menosmenos, maismais)
            atributos.populacao += randint(menosmenos, maismais)
            break


def Eclipse():
    escolha = 0
    while escolha != '1':
        slowprint(
            'ECLIPSE APOCALÍPTICO: "Um eclipse sombrio cobre o reino, trazendo consigo presságios de desastres iminentes e incitando o medo e a desconfiança entre o povo.',
            0.05)
        escolha = input('''\n
[1] Realizar rituais sagrados para buscar proteção divina -> Todos os atributos --
>>> ''')
        if escolha == '1':
            atributos.igreja -= randint(menosmenos, maismais)
            atributos.exercito -= randint(menosmenos, maismais)
            atributos.economia -= randint(menosmenos, maismais)
            atributos.populacao -= randint(menosmenos, maismais)
            break


#colocar os npcs dentro de uma lista
npc = [
    Padre1, Rainha, General1, Bruxa, Ferreiro, General2, Mendigo, Mercenario,
    Arcebispo, Templario, Evangelista, Pregador, Comerciante, Cientista, Tesoureiro,
    Sacerdotista, Cardeal, Lider_Guilda, Populacao, Economia, Exercito, Igreja,
]
divino_eclipse = [Divina, Eclipse]
shuffle(npc)  #embaralhar os npcs para ser aleatório

# printar o título do jogo
slowprint(titulo, 0.001)

#menu principal
while True:
    menu = input(f'''{'MENU PRINCIPAL':-^38}
[1] Começar o jogo
[2] Como jogar
[3] Créditos
>>>> ''')
    sleep(1.5)

    #como jogar
    if menu == '1':
        sleep(0.5)
        limpar_e_printar(titulo)
        break
    elif menu == '2':
        slowprint('''--> Em Reigns, você controlará as decisões de um rei dentro de seu castelo.
Seu objetivo principal é sobreviver o máximo de anos que conseguir.
Seu reino possui 4 atributos principais que precisam estar entre 0 e 100, caso algum deles chegue aos extremos, você perderá.
Os residentes do seu reino virão até você para pedir algo e cabe a você decidir o que fazer.
Para escolher sua ação, utilize as teclas 1 e 2 para selecioná-la.
Lembre-se, cada resposta alterará os atributos, então pense bem antes de responder qualquer coisa.
VIDA LONGA AO REI!
''', 0.03)
        qualquer = input('Aperte Enter para continuar: ')
        sleep(0.5)
        limpar_e_printar(titulo)
    elif menu == '3':
        print('=' * 20)
        slowprint(
            '''- André Ávila Cardoso
- Elvio Diodato Miranda da Silveira Diodato
- Erick Castro
- Fabricio de Lima 
- Yago Calixto Carvalho da Silva
''', 0.03
        )
        qualquer = input('Aperte Enter para continuar: ')
        sleep(0.5)
        limpar_e_printar(titulo)
    else:
        print('**Escolha uma das opções válidas**')
        print()

# escolha da dificuldade
dificuldade = ' '
while dificuldade not in '1234':
    print('-=' * 15)
    dificuldade = input('''Escolha o modo de jogo:
[1] Fácil
[2] Normal
[3] Difícil
[4] Impossível
>>>> ''')
    if dificuldade == '1':
        menor = 10
        maior = 15
        menosmenos = 15
        maismais = 20
    elif dificuldade == '2':
        menor = 15
        maior = 20
        menosmenos = 20
        maismais = 30
    elif dificuldade == '3':
        menor = 20
        maior = 30
        menosmenos = 30
        maismais = 40
    elif dificuldade == '4':
        menor = 40
        maior = 53
        menosmenos = maismais = 49
    else:
        print('**Escolha uma das opções válidas**')
        limpar_e_printar(titulo)
    print('-=' * 15)
modos = ['Fácil', 'Normal', 'Difícil', 'Impossível']
limpar_e_printar(titulo)

#ativar os eventos
vitoria = 0
geracoes = 0
while True:
    npc.append(choice(divino_eclipse))
    for evento in npc:
        atributos.exibir_atributos()
        if geracoes > 0:
            print(f'Gerações no poder: {geracoes}')
        print(f'Anos no poder: {vitoria}')
        evento()
        sleep(1.05)
        limpar_e_printar(titulo)

        # condições de derrotas
        if not 0 <= atributos.economia <= 100 or not 0 <= atributos.igreja <= 100 or not 0 <= atributos.exercito <= 100 or not 0 <= atributos.populacao <= 100:
            break

        vitoria += 1

    # Verificar derrota depois de todos os eventos
    if not 0 <= atributos.economia <= 100 or not 0 <= atributos.igreja <= 100 or not 0 <= atributos.exercito <= 100 or not 0 <= atributos.populacao <= 100:
        break

    # sistema de gerações
    geracoes += 1
    print({slowprint(f'Você já está no trono há muito tempo, seu reinado está durando {geracoes} ', 0.07)}, end=' ')
    if geracoes == 1:
        slowprint('geração', 0.07)
    else:
        slowprint('gerações', 0.07)
    continuar = input('\nAperte Enter para continuar: ')
    limpar_e_printar(titulo)

    #embaralhar de novo para continuar
    shuffle(npc)

atributos.exibir_atributos()

# finais
if atributos.economia not in range(0, 101):
    if atributos.economia > 100:
        slowprint('Sua moeda cresceu tanto que a inflação ficou descontrolada \nVOCÊ MORREU', 0.05)
    elif atributos.economia < 0:
        slowprint('A crise atingiu seu reino, a fome se instaurou até dentro do seu castelo \nVOCÊ MORREU ', 0.05)
elif atributos.igreja not in range(0, 101):
    if atributos.igreja > 100:
        slowprint('Os fiéis acredita que Deus é o verdadeiro Rei, eles tomaram o poder do reino \nVOCÊ MORREU', 0.05)
    elif atributos.igreja < 0:
        slowprint('A Igreja determinou suas escolhas como heresia, você foi cruxificado na praça central \nVOCÊ MORREU',
                  0.05)
elif atributos.exercito not in range(0, 101):
    if atributos.exercito > 100:
        slowprint(
            'Os generais não concordaram com suas escolhas, eles invadiram o castelo e tiraram sua vida ainda em cima do trono \nVOCÊ MORREU',
            0.05)
    elif atributos.exercito < 0:
        slowprint(
            'Seu exército ficou muito enfraquecido, os reinos vizinhos invadiram seu castelo enquanto você dormia \nVOCÊ MORREU',
            0.05)
elif atributos.populacao not in range(0, 101):
    if atributos.populacao > 100:
        slowprint('Você deu poder demais à população, agora eles querem tomar seu lugar no trono \nVOCÊ MORREU', 0.05)
    elif atributos.populacao < 0:
        slowprint(
            'A população se sentiu abandonada por suas decisões, eles estão colocando fogo no castelo \nVOCÊ MORREU',
            0.05)

slowprint(f'\nVocê sobreviveu por {vitoria} anos e seu reinado durou {geracoes} gerações completas', 0.05)
print('\nFIM')
