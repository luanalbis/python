import pygame
pygame.mixer.init()
pygame.mixer.music.load('ex021.hp.mp3')
pygame.mixer.music.play()
pygame.event.wait()
input()