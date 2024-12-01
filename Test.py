import pygame
import sys

# กำหนดข้อมูลเมนูอาหาร
food_items = [
    {"name": "ผัดกะเพรา", "price": "฿35", "image": None},
    {"name": "ผัดซีอิ๊ว", "price": "฿35", "image": None},
    {"name": "ข้าวผัด", "price": "฿35", "image": None},
    {"name": "ผัดไทย", "price": "฿35", "image": None},
    {"name": "ไก่ทอด", "price": "฿30", "image": None},
    {"name": "ผัดพริกแกง", "price": "฿35", "image": None},
    {"name": "ต้มยำ", "price": "฿60", "image": None},
    {"name": "ข้าวเปล่า", "price": "฿30", "image": None},
]

# ตั้งค่าเริ่มต้น
pygame.init()
screen = pygame.display.set_mode((600, 800))
pygame.display.set_caption("Food Menu")
fontWord = pygame.font.Font(r"C:\Users\Python\Desktop\DTI231-Application-main\FontThai.ttf", 20)
clock = pygame.time.Clock()

# สี
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
GRAY = (200, 200, 200)

# ฟังก์ชันสำหรับแสดงข้อความ
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

# ฟังก์ชันสำหรับสร้างปุ่ม
def draw_button(surface, color, rect, text, font, text_color):
    pygame.draw.rect(surface, color, rect)
    draw_text(text, font, text_color, surface, rect[0] + 10, rect[1] + 10)

# วาด UI
def draw_menu():
    screen.fill(WHITE)
    y = 50
    for item in food_items:
        # วาดกรอบเมนู
        pygame.draw.rect(screen, GRAY, (50, y, 500, 80), border_radius=10)
        
        # แสดงชื่อเมนูและราคา
        draw_text(item["name"], fontWord, BLACK, screen, 70, y + 10)
        draw_text(item["price"], fontWord, BLACK, screen, 400, y + 10)
        
        # วาดปุ่ม "สั่งซื้อ"
        draw_button(screen, GREEN, (450, y + 10, 100, 40), "สั่งซื้อ", fontWord, WHITE)
        
        y += 100  # เลื่อนลงสำหรับเมนูถัดไป

# ลูปหลักของแอป
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            y = 50
            for item in food_items:
                # ตรวจสอบว่าคลิกปุ่มสั่งซื้อหรือไม่
                if 450 <= mouse_x <= 550 and y + 10 <= mouse_y <= y + 50:
                    print(f"คุณสั่งซื้อ {item['name']} ราคา {item['price']}")
                y += 100

    draw_menu()
    pygame.display.flip()
    clock.tick(30)
