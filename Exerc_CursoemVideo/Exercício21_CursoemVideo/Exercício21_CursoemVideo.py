#Exercício 21 #

from pygame import mixer  #Importa a biblioteca pygame e o modulo mixer(controlador de som)

mixer.init() #Inicia o mixer

mixer.music.load('Exer21.mp3') #Carrega a música a ser tocada, sempre lembrar de colocar o nome do arquivo e o tipo(.mp3)

mixer.music.play() #inicia a música

mixer.music.set_volume(0.2) #Comando que define o volume percentual, sendo 0 para 0% e 1 para 100%

import time #Importa o módulo de tempo

time.sleep(360) #Coloca o programa em pausa por 360ms para tirar o erro de reprodução.

