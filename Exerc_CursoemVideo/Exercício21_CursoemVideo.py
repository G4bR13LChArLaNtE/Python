#Exercício21

from pygame import mixer #importa a biblioteca pygame e o modulo mixer(controlador de som)

mixer.init()#Inicia o mixer 

mixer.music.load('Música.mp3') #Carrega a música a ser tocada 

mixer.music.play() #Inicia a música 

mixer.music.set_volume(0.5)#Comando que define o volume percentual, sendo 0 para 0% e 1 para 100%

import time #importa o módulo de tempo

time.sleep(360) #Coloca o programa para dormir por 360ms para tirar o erro de reprodução. 
