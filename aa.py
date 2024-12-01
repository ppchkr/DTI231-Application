import pygame

# เริ่มต้น Pygame
pygame.init()

# กำหนดขนาดหน้าจอ
SCREEN_W = 400
SCREEN_H = 650
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))

# ชื่อเกม
pygame.display.set_caption("foodfood")

# หน้า Main
bg_Main = pygame.image.load("picture\\aa00.png") 
bg_Main = pygame.transform.scale(bg_Main, (SCREEN_W, SCREEN_H))

# หน้า menu
bg_menu = pygame.image.load("picture\\bb00.png") 
bg_menu = pygame.transform.scale(bg_menu, (SCREEN_W, SCREEN_H))

# กำหนดปุ่ม 
bt_Start = pygame.image.load("picture\\botton1.png") 


# ปรับขนาดปุ่มให้เล็กลง
bt_Start = pygame.transform.scale(bt_Start, (150, 50))  # ปรับขนาดปุ่ม Start

# กำหนดตำแหน่งของปุ่ม
bt_Start_rect = bt_Start.get_rect(center=(SCREEN_W // 2, SCREEN_H // 2 + 130))


# สถานะ
running = True
game_state = "main"  # กำหนดค่าเริ่มต้นเป็น "main_menu"

# วนลูปหลัก
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # ตรวจสอบการคลิกที่ปุ่ม
        if game_state == "main":
            mouse_pos = pygame.mouse.get_pos()

            screen.blit(bg_Main, (0, 0))  # วาดพื้นหลังหลัก
            screen.blit(bt_Start, bt_Start_rect)  # วาดปุ่ม Start
            

            # ตรวจสอบการคลิกที่ปุ่ม
            if event.type == pygame.MOUSEBUTTONDOWN:
                if bt_Start_rect.collidepoint(mouse_pos):
                    game_state = "menu"  # เปลี่ยนไปยังโหมดเมนู
                
 
        elif game_state == "menu":
            bt_ap = pygame.image.load("picture\\ap.png")
            bt_pe = pygame.image.load("picture\\pe.png")
            bt_pp = pygame.image.load("picture\\pp.png") 
            bt_pt = pygame.image.load("picture\\pt.png")

            # ปรับขนาดปุ่มให้เล็กลง
            bt_ap = pygame.transform.scale(bt_ap, (100, 100))
            bt_pe = pygame.transform.scale(bt_pe, (100, 100))
            bt_pp = pygame.transform.scale(bt_pp, (100, 100))
            bt_pt = pygame.transform.scale(bt_pt, (100, 100))

            # กำหนดตำแหน่งของปุ่ม
            bt_ap_rect = bt_ap.get_rect(center=(SCREEN_W // 3, SCREEN_H // 4 ))
            bt_pe_rect = bt_pe.get_rect(center=(SCREEN_W // 1.5, SCREEN_H // 4))
            bt_pp_rect = bt_pp.get_rect(center=(SCREEN_W // 2, SCREEN_H // 2))
            bt_pt_rect = bt_pt.get_rect(center=(SCREEN_W // 1.5, SCREEN_H // 2.3))

            screen.blit(bg_menu, (0, 0))  # วาดพื้นหลังของหน้าถัดไป
            screen.blit(bt_ap, bt_ap_rect)
            screen.blit(bt_pe, bt_pe_rect)
            screen.blit(bt_pp, bt_ap_rect)
            screen.blit(bt_pt, bt_pt_rect)

    # อัปเดตหน้าจอ
    pygame.display.flip()

# ออกจาก Pygame
pygame.quit()
