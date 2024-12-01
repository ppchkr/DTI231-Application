import pygame

# เริ่มต้น Pygame
pygame.init()

# กำหนดขนาดหน้าจอ
SCREEN_W = 800
SCREEN_H = 600
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

# ชื่อเกม
pygame.display.set_caption("rooproop")

# กำหนดสีพื้นหลัง (RGB)
BACKGROUND_COLOR = (0, 0, 0)  # สีดำ

# สถานะของเกม
running = True

# วนลูปหลักของเกม
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # เติมสีพื้นหลัง
    screen.fill(BACKGROUND_COLOR)

    # อัปเดตหน้าจอ
    pygame.display.flip()

# ออกจาก Pygame
pygame.quit()
