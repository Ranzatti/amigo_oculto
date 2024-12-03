import random
import time
import urllib
import webbrowser as web
import keyboard as k
import pyautogui
import schedule
from urllib import parse

# import tkinter as tk


def amigo_secreto(participantes):
    random.shuffle(participantes)
    amigo = participantes.copy()
    amigo.append(amigo.pop(0))
    return list(zip(participantes, amigo))


def enviar_zap(participantes):
    for participante in participantes:
        pyautogui.click(1200, 0)

        # espera 60 segundos para enviar a nova mensagem
        time.sleep(60)

        mensagem = f"""
        Querido(a) _*{participante['nome']}*_,

        A época mais mágica do ano está chegando, e é hora de revelar quem terá a alegria de ser o seu Amigo Oculto!
        
        Após um sorteio emocionante, 5 horas de processamento, computadores a mil... o nome que você deverá manter em segredo até a grande troca de presentes é...

        Que rufem os tambores....

        🌟🎄🎁   _*{participante['sorteado'].upper()}*_   🎁🎄🌟

        Agora que o segredo foi revelado, é hora de começar a pensar no presente perfeito para surpreender o seu amigo. 
        
        Lembre-se de que o valor sugerido para o presente é de _*R$60,00*_, mas o mais importante é a criatividade e o carinho envolvidos no gesto.
        
        Prepare-se para uma noite cheia de risadas, alegria e, é claro, presentes incríveis!

        Mantenha o suspense até o dia da troca, e vamos fazer deste Amigo Oculto um momento inesquecível para todos.

        Até lá!
        """

        texto = urllib.parse.quote(mensagem)

        web.open("https://web.whatsapp.com/send?phone=+55" + participante['telefone'] + "&text=" + texto)

        # Posiciona o cursor no botão de envio
        pyautogui.click(2040, 980)

        # espera X segundos para clicar no botão de envio
        time.sleep(30)

        # clica no botão de enviar do zap web
        k.press_and_release('enter')

        print('Enviado com sucesso para: ', participante['nome'])


def enviar_lista_ana(participantes):
    pyautogui.click(1200, 0)
    time.sleep(60)

    mensagem = f"🎅Sorteados do Amigo Oculto 2024🎅\n\n" + "\n".join(
        [f"{item['nome']} → {item['sorteado']}" for item in participantes])

    texto = urllib.parse.quote(mensagem)

    # abre a pagina de whatsapp web
    web.open("https://web.whatsapp.com/send?phone=+5534998723109&text=" + texto)

    # Posiciona o cursor no botão de envio
    pyautogui.click(2040, 980)

    # espera X segundos para clicar no botão de envio
    time.sleep(30)

    # clica no botão de enviar do zap web
    k.press_and_release('enter')

    pyautogui.click(1200, 0)

    print('Enviado Lista dos parcipantes pra Ana com sucesso!')


def criar_arquivo(participantes):
    nome_arquivo = "sorteados.txt"

    # Criando o arquivo e escrevendo os itens da lista
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(f"🎅 Sorteados do Amigo Oculto 2024 🎅\n\n" + "\n".join(
            [f"{item['nome']} → {item['sorteado']}" for item in participantes]) + "\n")

    print(f"Arquivo '{nome_arquivo}' criado com sucesso!")


def gerar_arquivo():
    # Obtém a largura e a altura da tela
    # root = tk.Tk()
    # largura_tela = root.winfo_screenwidth()
    # altura_tela = root.winfo_screenheight()
    # print(largura_tela)
    # print(altura_tela)
    # root.destroy()

    print('Gerando Arquivo...')

    lista_participantes = {
        'Laura': '34996690025',
        'Raquel': '34999830025',
        'Matheus': '34998089988',
        'Ricardo': '34998100025',
        'Fernanda': '61992856117',
        'Cecilia': '61992856117',
        'Milania': '61996993610',
        'Marco Aurélio': '61992164119',
        'Maria Paula': '61998410397',
        'Alba': '34991733739',
        'Galeno': '34997259024',
        'Joyce': '62998651781',
        'Ariane': '67981584772',
        'Marlei': '61991354006',
        'João Gabriel': '61999198248',
        'Alice': '34988614573',
        'Fred': '34996794554',
        'Mário': '34988614573',
        'Marlene': '34988614573',
        'Humilda': '34999796471',
        'Cirlene': '34991141424',
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

        criar_arquivo(lista)
        enviar_zap(lista)
        enviar_lista_ana(lista)

        print('Sorteio realizado com Sucesso!')
        exit()
    else:
        print('Ops! deu ruim')


# programado para começar às 02:50 da manha de sexta
# schedule.every().monday.at("22:30").do(gerar_arquivo)
gerar_arquivo()

while 1:
    schedule.run_pending()
