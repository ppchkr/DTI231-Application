import pygame

# เริ่มต้น Pygame
pygame.init()

# กำหนดขนาดหน้าจอ
SCREEN_W = 350
SCREEN_H = 600
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

# ชื่อเกม
pygame.display.set_caption("rooproop")

# โหลดภาพพื้นหลัง (แก้ชื่อไฟล์หรือเส้นทางให้ถูกต้อง)
background_image = pygame.image.load("picture/aa00.png")  # ใส่ชื่อไฟล์ที่ถูกต้อง
background_image = pygame.transform.scale(background_image, (SCREEN_W, SCREEN_H))  # ปรับขนาดภาพให้พอดีกับหน้าจอ

# สถานะของเกม
running = True

# วนลูปหลักของเกม
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # วาดภาพพื้นหลังลงบนหน้าจอ
    screen.blit(background_image, (0, 0))

    # อัปเดตหน้าจอ
    pygame.display.flip()

# ออกจาก Pygame
pygame.quit()
