import pygame 
import random

pygame.init()
pygame.mixer.init()

# ชื่อเกม
pygame.display.set_caption("rooproop")

def matrix(n):
    cal = n//5
    if  cal < 5 :
        r,c = cal,5
        return r,c
    else:
        r,c = 5,cal
        return r,c 

#กำหนดขนาดหน้าจอ
SCREEN_W = 800
SCREEN_H = 600
screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))

# พื้นหลัง
bg_Main = pygame.transform.scale(pygame.image.load("background/Main.png"), ( (SCREEN_W, SCREEN_H)))
bg_Mode = pygame.transform.scale(pygame.image.load("background/Mode.png"), (SCREEN_W, SCREEN_H))
bg_Setting = pygame.transform.scale(pygame.image.load("background/Setting.png"), (SCREEN_W, SCREEN_H))