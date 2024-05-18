#Passos para o projeto bot para preenchimento de dados.
#1- Entrat no sistema da empresa
# https://dlp.hashtagtreinamentos.com/python/intensivao/login
#2- Fazer logim
#3- Importar a base de dados
#4- Cadastrar um produto
#5- Repetir até acabar a base de dados
# RPA = Automação

#1- Entrat no sistema da empresa 
import pyautogui
import time #Traz comandos de tempo
import pandas as pd
#Comandos do pyautogui, clicar-> pyautogui.click, escrever-> pyautogui.write, Apertar uma tecla -> pyautogui.press
#Apertar -> pyautogui.hotkey
pyautogui.PAUSE = 1 #Faz com que cada comando pyautogui espere o tempo determinado para ser executado
#apertar a tecla windows
pyautogui.press('win')
#Digitar o nome do programa
pyautogui.write('microsoft edge')
#Clicar enter
pyautogui.press('enter')
#Escrever olink
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)
pyautogui.press('enter')
#Usar a ferramenta time.sleeo() para pausar apenas no local determinado
time.sleep(5)

#2- Fazer logim
pyautogui.click(x=625, y=391)
pyautogui.write('emailteste.com')
#Passar para area de senha
pyautogui.press('tab')
pyautogui.write('senha digitada')
pyautogui.click(x=682, y=552)

#Agora vamos cadastrar os produtos de acordo com os conhecimentos já realizados.
#Importar a base dos pordutos
tabela = pd.read_csv('produtos.csv')
print(tabela)

for linha in tabela.index:
    pyautogui.click(x=624, y=278)
    pyautogui.write(str(tabela.loc[linha, 'codigo']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'marca']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press('tab')

    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')

    if not pd.isna(tabela.loc[linha, 'obs']): #Verifica se tem informação em obs, caso contrario não preenche.
        pyautogui.write(str(tabela.loc[linha, 'obs']))

    pyautogui.click(x=599, y=570)
    pyautogui.scroll(50000)
    






