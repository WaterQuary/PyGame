import random

def Random_audio():
    for i in range(1,4):
        keyword = f"audio/ReachTarget{i}.mp3"
    return keyword

audio_mass = [Random_audio()]
random_choice = random.choice(audio_mass)
print(random_choice)
print(audio_mass)
import pygame
import time

pygame.mixer.init()
click_sound = pygame.mixer.Sound(str(random_choice))

click_sound.play()


click_sound.set_volume(0.5)


time.sleep(10)
pygame.mixer.music.stop()