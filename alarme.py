from datetime import date, datetime
from time import sleep
import pygame

hora = input('Hora: ')
minuto = input('Minuto: ')
print('Alarme: {}:{}'.format(hora, minuto))


while True:
    sleep(1)
    if datetime.today().strftime('%H') == hora and datetime.today().strftime('%M') == minuto:
        print('Acorda!!! Horário = {}:{}'.format(hora, minuto))
        pygame.init()
        pygame.mixer.music.load('toque.mp3')
        pygame.mixer.music.play() 
        sleep(10)
        pygame.event.wait()

        break
