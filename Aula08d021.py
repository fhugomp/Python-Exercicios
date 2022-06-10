from time import sleep
import pygame

print('Tocando Música...')
sleep(1.5)
pygame.init()
pygame.mixer.music.load('Aula08d021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
