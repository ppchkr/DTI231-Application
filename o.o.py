import pygame
import sys
from collections import deque

# Initialize Pygame
pygame.init()

# Define Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("GrabFood Queue Manager")

# Font for text
font = pygame.font.Font("FontThai.ttf", 20)
font_small = pygame.font.Font("FontThai.ttf", 20)

# Food items for menu
menu_items = [
    {"name": "ข้าวผัด", "price": 35, "image": "picture\\ap.png", "rect": pygame.Rect(100, 100, 100, 100)},
    {"name": "ผัดซีอิ๊ว", "price": 35, "image": "picture\\pe.png", "rect": pygame.Rect(250, 100, 100, 100)},
    {"name": "ผัดกะเพรา", "price": 35, "image": "picture\\pp.png", "rect": pygame.Rect(100, 250, 100, 100)},
    {"name": "ผัดไทย", "price": 35, "image": "picture\\pt.png", "rect": pygame.Rect(250, 250, 100, 100)},
]

# Order and queue management
order = {}
queue = deque()

def draw_text(text, color, x, y, font_type=font):
    label = font_type.render(text, True, color)
    screen.blit(label, (x, y))

def draw_menu():
    screen.fill(WHITE)
    draw_text("Restaurant Menu", BLACK, 300, 50)

    # วาดเมนูรูปภาพ
    for item in menu_items:
        img = pygame.image.load(item["image"])
        img = pygame.transform.scale(img, (100, 100))  # ปรับขนาด
        screen.blit(img, item["rect"])

def draw_order():
    draw_text("Your Order:", BLACK, 500, 50)
    if not order:
        draw_text("No items ordered yet.", BLACK, 500, 100)
    else:
        y_offset = 100
        total_price = 0
        for name, details in order.items():
            draw_text(f"{name} x {details['quantity']} - ฿{details['quantity'] * details['price']:.2f}", BLACK, 500, y_offset)
            y_offset += 40
            total_price += details['quantity'] * details['price']
        draw_text(f"Total: ฿{total_price:.2f}", RED, 500, y_offset + 20)

def draw_queue():
    screen.fill(WHITE)
    draw_text("Order Queue", BLACK, 50, 50)
    y_offset = 100
    if not queue:
        draw_text("No orders in queue.", BLACK, 50, y_offset)
    else:
        for i, queued_order in enumerate(queue):
            draw_text(f"Queue {i+1}:", BLACK, 50, y_offset)
            y_offset += 20
            for name, details in queued_order.items():
                draw_text(f"{name} x {details['quantity']}", BLACK, 50, y_offset)
                y_offset += 20
            y_offset += 10  # เพิ่มช่องว่างระหว่างแต่ละคิว
    # Draw Serve button
    serve_rect = pygame.Rect(50, 500, 150, 50)
    pygame.draw.rect(screen, RED, serve_rect)
    draw_text("Serve", WHITE, 70, 510, font_small)
    return serve_rect


def handle_click(pos):
    # ตรวจสอบการคลิกที่ปุ่มเมนูภาพและเพิ่มจำนวนเมนูในออเดอร์
    for item in menu_items:
        if item["rect"].collidepoint(pos):
            if item["name"] in order:
                order[item["name"]]["quantity"] += 1  # เพิ่มจำนวนเมนูที่เลือก
            else:
                order[item["name"]] = {"quantity": 1, "price": item["price"]}

def place_order():
    if order:
        queue.append(order.copy())
        order.clear()

def serve_order():
    if queue:
        queue.popleft()

# Main Menu and Game State Logic
bg_Main = pygame.image.load("picture\\aa00.png")
bg_Main = pygame.transform.scale(bg_Main, (SCREEN_WIDTH, SCREEN_HEIGHT))

bg_menu = pygame.image.load("picture\\bb00.png")
bg_menu = pygame.transform.scale(bg_menu, (SCREEN_WIDTH, SCREEN_HEIGHT))

bt_Start = pygame.image.load("picture\\botton1.png")
bt_Start = pygame.transform.scale(bt_Start, (150, 50))
bt_Start_rect = bt_Start.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 130))

running = True
game_state = "main"

show_queue = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = event.pos
            
            if show_queue:
                # สร้างปุ่ม "View Menu"
                back_menu_button = pygame.Rect(300, 500, 150, 50)
                pygame.draw.rect(screen, GREEN, back_menu_button)  # เปลี่ยนสีปุ่มเป็นสีเขียว
                draw_text("Back to Menu", BLACK, 310, 510, font_small)  # ข้อความในปุ่ม
                
                if back_menu_button.collidepoint(pos):
                    show_queue = False
                    print("back to menu")

            if game_state == "main":
                if bt_Start_rect.collidepoint(pos):
                    game_state = "menu"
            
            elif game_state == "menu":
                if show_queue:
                    serve_rect = draw_queue()
                    if serve_rect.collidepoint(pos):
                        serve_order()
                else:
                    handle_click(pos)  # เพิ่มเมนูตามการคลิกที่รูป
                    place_order_button = pygame.Rect(600, 500, 150, 50)
                    if place_order_button.collidepoint(pos):
                        place_order()
                    view_queue_button = pygame.Rect(50, 500, 150, 50)
                    if view_queue_button.collidepoint(pos):
                        show_queue = True

    


    if game_state == "main":
        screen.blit(bg_Main, (0, 0))  # Main Menu Background
        screen.blit(bt_Start, bt_Start_rect)  # Start Button
    elif game_state == "menu":
        if show_queue:
            draw_queue()
        else:
            draw_menu()
            draw_order()
            # Buttons for placing order and viewing queue
            place_order_button = pygame.Rect(600, 500, 150, 50)
            pygame.draw.rect(screen, GREEN, place_order_button)
            draw_text("Place Order", WHITE, 610, 510, font_small)
            view_queue_button = pygame.Rect(50, 500, 150, 50)
            pygame.draw.rect(screen, GREEN, view_queue_button)
            draw_text("View Queue", WHITE, 60, 510, font_small)

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()
