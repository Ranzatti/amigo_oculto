import random
import time
import tkinter as tk
import urllib
import webbrowser as web
import keyboard as k
import pyautogui
import schedule
from urllib import parse


def amigo_secreto(participantes):
    random.shuffle(participantes)
    amigo = participantes.copy()
    amigo.append(amigo.pop(0))
    return list(zip(participantes, amigo))


def enviar_Zap():
    root = tk.Tk()

    # Obtém a largura e a altura da tela
    # largura_tela = root.winfo_screenwidth()
    # altura_tela = root.winfo_screenheight()

    # Fecha a janela tkinter temporária
    root.destroy()

    with open("dados.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    for linha in linhas[1:]:
        campos = linha.strip().split(";")

        pyautogui.click(1200, 0)
        time.sleep(30)

        mensagem = f"""
        Querido(a) _*{campos[0]}*_,

        A época mais mágica do ano está chegando, e é hora de revelar quem terá a alegria de ser o seu Amigo Oculto!
        Após um sorteio emocionante, 5 horas de processamento, computadores a mil... o nome que você deverá manter em segredo até a grande troca de presentes é...

        Que rufem os tambores....

        🌟✨🎄🎉🎁🎅 _*{campos[2].upper()}*_ 🎅🎁🎉🎄✨🌟

        Agora que o segredo foi revelado, é hora de começar a pensar no presente perfeito para surpreender o seu amigo. 
        
        Lembre-se de que o valor sugerido para o presente é de *R$60,00*, mas o mais importante é a criatividade e o carinho envolvidos no gesto.
        
        Prepare-se para uma noite cheia de risadas, alegria e, é claro, presentes incríveis!

        Mantenha o suspense até o dia da troca, e vamos fazer deste Amigo Oculto um momento inesquecível para todos.

        Desejamos a vocês um Natal cheio de amor, harmonia e ótimas lembranças!

        Abraço
        """

        texto = urllib.parse.quote(mensagem)

        web.open("https://web.whatsapp.com/send?phone=+55" + campos[1] + "&text=" + texto)

        # Posiciona o cursor no botão de envio
        pyautogui.click(2040, 980)
        time.sleep(20)

        # clica no botão de enviar do zap web
        k.press_and_release('enter')

        print('Enviado com sucesso para ', campos[0])


def enviar_Lista_Ana(nomes):
    mensagem = f"""
            Participantes do Amigo Oculto 2024:
            
            """ + ", ".join([f"{x} → {y}" for x, y in nomes])

    texto = urllib.parse.quote(mensagem)

    # web.open("https://web.whatsapp.com/send?phone=+5534998723109&text=Participantes do Amigo Oculto 2024: " + ", ".join([f"{x} → {y}" for x, y in nomes]))
    web.open("https://web.whatsapp.com/send?phone=+5534998723109&text=" + texto)
    pyautogui.click(2040, 980)
    time.sleep(20)
    k.press_and_release('enter')
    print('Enviado Lista dos parcipantes pra Ana com sucesso!')


def gerar_arquivo():
    print('Gerando Arquivo...')

    lista_participantes = {
        # 'Laura': '34996690025',
        # 'Raquel': '34999830025',
        # 'Matheus': '34998089988',
        # 'Ricardo': '34998100025',
        'Fernanda': '61992856117',
        'Cecilia': '61992856117',
        'Milania': '61996993610',
        'Marco': '61992164119',
        'Maria Paula': '61998410397',
        'Ricardo': '34998100025',
        'Raquel': '34999830025',
        'Laura': '34996690025',
        'Matheus': '34998089988',
        'Alba': '34991733739',
        'Galeno': '34997259024',
        'Joyce': '62998651781',
        'Ariane': '67981584772',
        'Marlei': '61991354006',
        'João Gabriel': '61999198248',
    }

    participantes = []
    telefone_participantes = []

    for key, value in lista_participantes.items():
        participantes.append(key)
        telefone_participantes.append(value)

    # Chamar a função amigo_secreto
    nomes = amigo_secreto(participantes)

    tudook = True
    # verificando se a pessoa saiu com ela mesmo
    for nome in nomes:
        if nome[0] == nome[1]:
            print('Sujeito Saiu com ele mesmo, faz de novo: ', nome[0])
            tudook = False

    # verificando se o numero de telefone é valido
    for telefone in telefone_participantes:
        if len(telefone) != 11:
            print('Telefone errado:', telefone, len(telefone))
            tudook = False

    if tudook:
        # gravando no arquivo texto com o nome da pessoa, telefone e quem ele foi sorteado
        with open("dados.txt", "w") as arquivo:
            arquivo.write("nome;telefone;sorteado\n")
            for nome in nomes:
                arquivo.write(f"{nome[0]};{lista_participantes.get(nome[0])};{nome[1]}\n")

        enviar_Zap()
        enviar_Lista_Ana(nomes)

        print('Arquivo com os nomes gerado com!')

        exit()
    else:
        print('Ops! deu ruim')


# programado para começar às 02:50 da manha de sexta
# schedule.every().saturday.at("22:25").do(gerar_arquivo)
# gerar_arquivo()

while 1:
    schedule.run_pending()
