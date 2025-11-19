import random
import time
import urllib
import webbrowser as web
import keyboard as k
import pyautogui
import schedule
from urllib import parse

import tkinter as tk

POSICAO_X_MOUSE_INICIAL = 1200  # na horizontal
POSICAO_X_MOUSE_FINAL = 2350  # na horizontal
POSICAO_Y_MOUSE_INICIAL = 0  # na vertical
POSICAO_Y_MOUSE_FINAL = 980  # na vertical

def amigo_secreto(participantes):
    random.shuffle(participantes)
    amigo = participantes.copy()
    amigo.append(amigo.pop(0))
    return list(zip(participantes, amigo))


def enviar_zap(participantes):
    for participante in participantes:
        pyautogui.click(POSICAO_X_MOUSE_INICIAL, POSICAO_Y_MOUSE_INICIAL)

        # espera 60 segundos para abrir a pagina e enviar a nova mensagem
        time.sleep(60)

        mensagem = f"""
        Querido(a) _*{participante['nome']}*_,

        A época mais mágica do ano está chegando, e é hora de revelar quem terá a alegria de ser o seu Amigo Oculto!
        
        Após um sorteio emocionante, 5 horas de processamento, computadores a mil... o nome que você deverá manter em segredo até a grande troca de presentes é...

        Que rufem os tambores....

        🌟🎄🎁   _*{participante['sorteado'].upper()}*_   🎁🎄🌟

        Agora que o segredo foi revelado, é hora de começar a pensar no presente perfeito para surpreender o seu amigo. 
        
        Lembre-se de que o valor sugerido para o presente é de _*R$70,00*_, mas o mais importante é a criatividade e o carinho envolvidos no gesto.
        
        Prepare-se para uma noite cheia de risadas, alegria e, é claro, presentes incríveis!

        Mantenha o suspense até o dia da troca, e vamos fazer deste Amigo Oculto um momento inesquecível para todos.

        Até lá!
        """

        texto = urllib.parse.quote(mensagem)

        web.open("https://web.whatsapp.com/send?phone=+55" + participante['telefone'] + "&text=" + texto)

        # Posiciona o cursor no botão de envio
        pyautogui.click(POSICAO_X_MOUSE_FINAL, POSICAO_Y_MOUSE_FINAL)

        # espera X segundos para clicar no botão de envio
        time.sleep(10)

        # clica no botão de enviar do zap web
        # k.press_and_release('enter')
        pyautogui.press('enter')

        print('Enviado com sucesso para: ', participante['nome'])


def enviar_lista_contemplados(participantes):
    # essa etapa envia o arquivo de todos os sorteados para uma pessoa como backup e possivel conferencia
    pyautogui.click(POSICAO_X_MOUSE_INICIAL, POSICAO_Y_MOUSE_INICIAL)
    time.sleep(60)

    mensagem = f"🎅Sorteados do Amigo Oculto 2025🎅\n\n" + "\n".join(
        [f"{item['nome']} → {item['sorteado']}" for item in participantes])

    texto = urllib.parse.quote(mensagem)

    # abre a pagina de whatsapp web
    web.open("https://web.whatsapp.com/send?phone=+5534998100025&text=" + texto)

    # Posiciona o cursor no botão de envio
    pyautogui.click(POSICAO_X_MOUSE_FINAL, POSICAO_Y_MOUSE_FINAL)

    # espera X segundos para clicar no botão de envio
    time.sleep(30)

    # clica no botão de enviar do zap web
    # k.press_and_release('enter')
    pyautogui.press('enter')

    pyautogui.click(POSICAO_X_MOUSE_INICIAL, POSICAO_Y_MOUSE_INICIAL)

    print('Enviado Lista dos parcipantes pra Ana com sucesso!')


def criar_arquivo_contemplados(participantes):
    nome_arquivo = "sorteados.txt"

    # Criando o arquivo e escrevendo os itens da lista
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(f"🎅 Sorteados do Amigo Oculto 2025 🎅\n\n" + "\n".join(
            [f"{item['nome']} → {item['sorteado']}" for item in participantes]) + "\n")

    print(f"Arquivo '{nome_arquivo}' criado com sucesso!")


def gerar_arquivo():
    # essas linhas comentadas serve para vc ver qual o tamanho da sua tela para configurar a posição do mouse - obtém a largura e a altura da tela
    # root = tk.Tk()
    # largura_tela = root.winfo_screenwidth()
    # altura_tela = root.winfo_screenheight()
    # print(largura_tela)
    # print(altura_tela)
    # root.destroy()

    print('Gerando Arquivo...')

    # lista_participantes = {
    #     'Laura': '34996690025',
    #     'Raquel': '34999830025',
    #     'Matheus': '34998089988',
    #     'Ricardo': '34998100025',
    #     'Ana': '34998723109',
    #     'James': '34984438013',
    # }

    lista_participantes = {
        'Cecília': '61991743074',
        'James': '34984438013',
        'Ricardo': '34998100025',
        'Vovó Nene': '34991733739',
        'Marcus Vinícius': '61982055633',
        'Vovô Mário': '34991733739',
        'Milânia': '61996993610',
        'Marco Aurélio': '61992164119',
        'Joyce': '62998651781',
        'Fernanda': '61992856117',
        'Raquel': '34999830025',
        'Guilherme': '67992641716',
        'Laura': '34996690025',
        'Joelma': '62985889078',
        'João Gabriel': '61999198248',
        'Marlei': '61991354006',
        'Maria Paula': '61998410397',
        'Eduardo': '67993090917',
        'Beatriz': '11952998748',
        'Mariana': '67993244203',
        'Maria Eduarda': '67993244203',
        'Ariane': '67981584772',
        'Galeno': '34997259024',
        'Ana Luiza': '34998723109',
        'Alba': '34991733739',
        'Peixoto': '61995204803',
        'Matheus': '34998089988'
    }

    participantes = []
    telefone_participantes = []

    for key, value in lista_participantes.items():
        participantes.append(key)
        telefone_participantes.append(value)

    # Chamar a função amigo_secreto
    nomes = amigo_secreto(participantes)

    tudoOk = True
    # verificando se a pessoa saiu com ela mesmo
    for nome in nomes:
        if nome[0] == nome[1]:
            print('Sujeito Saiu com ele mesmo, faz de novo: ', nome[0])
            tudoOk = False

    # verificando se o numero de telefone é valido
    for telefone in telefone_participantes:
        if len(telefone) != 11:
            print('Telefone errado:', telefone, len(telefone))
            tudoOk = False

    if tudoOk:
        # criando uma lista com o nomes, telefones e sorteados
        lista = []
        for nome in nomes:
            lista.append({"nome": nome[0], "telefone": lista_participantes.get(nome[0]), "sorteado": nome[1]})

        criar_arquivo_contemplados(lista)
        enviar_zap(lista)
        enviar_lista_contemplados(lista)

        print('Sorteio realizado com Sucesso!')
        exit()
    else:
        print('Ops! deu ruim')


# programado para começar às 02:50 da manha de sexta
# schedule.every().monday.at("22:30").do(gerar_arquivo)
gerar_arquivo()

while 1:
    schedule.run_pending()
