import pyautogui
import time

#saber todas as teclas do teclado = print(pyautogui.KEYBOARD_KEYS)

pyautogui.PAUSE = 0.5

#abrir chrome
pyautogui.press ('win') # pressionar uma tecla do teclado
pyautogui.press ('enter')
pyautogui.write ('chrome') # escrever um texto

#1 entrar no site do sistema
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')
#pyautogui.hotkey apertar o conjunto de teclas (Crtl C, Crtl V, Alt Tab)
#ele pode demorar um pouco para abrir
time.sleep(3)

#2 Fazer login
pyautogui.click(x=682, y=462) #posso usar button='left'
pyautogui.write('teste@gmail.com')
pyautogui.press('tab') #passou para o campo de senha
pyautogui.write('senha123')
pyautogui.press('tab') #passou pro botão de login
pyautogui.press('enter')

time.sleep(3)

#3 importar base de dados

import pandas as pd

tabela = pd.read_csv('produtos.csv')

#4 cadastrar um produto

#index = linhas da tabela na biblioteca pandas
for linha in tabela.index:
    codigo = str(tabela.loc[linha, 'codigo'])
    #CLICAR NO campo do código
    pyautogui.click(x=647, y=326)
    #preencher o campo
    pyautogui.write(codigo)
    #passar pro próximo campo
    pyautogui.press('tab')
    #marca
    pyautogui.write(str(tabela.loc[linha, 'marca']))
    #passar pro próximo campo
    pyautogui.press('tab')
    #tipo
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    #passar pro próximo campo
    pyautogui.press('tab')
    #categoria
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    #passar pro próximo campo
    pyautogui.press('tab')
    #preço
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    #passar pro próximo campo
    pyautogui.press('tab')
    #custo
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    #passar pro próximo campo
    pyautogui.press('tab')
    #obs
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)
    #passar pro próximo campo
    pyautogui.press('tab')
    #apertar o botão
    pyautogui.press('enter')
    pyautogui.scroll(5000)

#5 repetir para cadastrar vários produtos


