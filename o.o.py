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

# Screen dimensions
SCREEN_WIDTH = 450
SCREEN_HEIGHT = 750
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("GrabFood Queue Manager")

# Font for text
font = pygame.font.Font("FontThai.ttf", 20)
font_small = pygame.font.Font("FontThai.ttf", 20)

# Food items for menu
menu_items = [
    {"name": "ข้าวผัด", "price": 35, "image": "picture\\15.png", "rect": pygame.Rect(20, 100, 130, 130)},
    {"name": "ผัดซีอิ๊ว", "price": 35, "image": "picture\\14.png", "rect": pygame.Rect(160, 100, 130, 130)},
    {"name": "ผัดกะเพรา", "price": 35, "image": "picture\\13.png", "rect": pygame.Rect(20, 240, 130, 130)},
    {"name": "ผัดไทย", "price": 35, "image": "picture\\16.png", "rect": pygame.Rect(160, 240, 130, 130)},
    {"name": "ไก่ทอด", "price": 30, "image": "picture\\17.png", "rect": pygame.Rect(20, 380, 130, 130)},
    {"name": "ข้าวเปล่า", "price": 15, "image": "picture\\18.png", "rect": pygame.Rect(160, 380, 130, 130)},
    {"name": "ต้มยำกุ้ง", "price": 60, "image": "picture\\19.png", "rect": pygame.Rect(20, 520, 130, 130)},
    {"name": "ผัดพริกแกง", "price": 35, "image": "picture\\20.png", "rect": pygame.Rect(160, 520, 130, 130)},
]   

# Order and queue management
order = {}
queue = deque()

# Load cart icon
cart_icon = pygame.image.load("picture\\basket.png")
cart_icon = pygame.transform.scale(cart_icon, (50, 50))  # Resize icon
cart_icon_rect = cart_icon.get_rect(topright=(SCREEN_WIDTH - 20, 20))

def draw_text(text, color, x, y, font_type=font):
    label = font_type.render(text, True, color)
    screen.blit(label, (x, y))

def draw_menu():
    screen.fill(WHITE)
    draw_text("Restaurant Menu", BLACK, 150, 50)
    for item in menu_items:
        img = pygame.image.load(item["image"])
        img = pygame.transform.scale(img, (130, 130))  # Adjust size
        screen.blit(img, item["rect"])

    # Draw cart icon
    screen.blit(cart_icon, cart_icon_rect)

    # Display item count in cart
    total_items = sum(details['quantity'] for details in order.values())
    draw_text(f"{total_items}", RED, cart_icon_rect.left - 20, cart_icon_rect.top + 15)

def draw_order():
    draw_text("Your Order:", BLACK, 300, 100)
    if not order:
        draw_text("No items ordered yet.", BLACK, 300, 150)
    else:
        y_offset = 150
        total_price = 0
        for name, details in order.items():
            draw_text(f"{name} x {details['quantity']} - ฿{details['quantity'] * details['price']:.2f}", BLACK, 300, y_offset)
            y_offset += 40
            total_price += details['quantity'] * details['price']
        draw_text(f"Total: ฿{total_price:.2f}", RED, 300, y_offset + 20)

def draw_queue():
    screen.fill(WHITE)
    draw_text("Order Queue", BLACK, 50, 50)
    y_offset = 100
    if not queue:
        draw_text("No orders in queue.", BLACK, 50, y_offset)
    else:
        for i, queued_order in enumerate(queue):
            draw_text(f"Queue {i + 1}:", BLACK, 50, y_offset)
            y_offset += 20
            for name, details in queued_order.items():
                draw_text(f"{name} x {details['quantity']}", BLACK, 50, y_offset)
                y_offset += 20
            y_offset += 10  # เพิ่มช่องว่างระหว่างแต่ละคิว

    # Draw Serve button
    serve_rect = pygame.Rect(50, 700, 150, 50)
    pygame.draw.rect(screen, RED, serve_rect)
    draw_text("Serve", WHITE, 70, 710, font_small)

    # Draw Back button
    back_menu_button = pygame.Rect(350, 700, 150, 50)
    pygame.draw.rect(screen, GREEN, back_menu_button)
    draw_text("Back to Menu", BLACK, 360, 710, font_small)

    return serve_rect, back_menu_button

def handle_click(pos):
    for item in menu_items:
        if item["rect"].collidepoint(pos):
            if item["name"] in order:
                order[item["name"]]["quantity"] += 1
            else:
                order[item["name"]] = {"quantity": 1, "price": item["price"]}

def place_order():
    if order:
        queue.append(order.copy())
        order.clear()

def serve_order():
    if queue:
        queue.popleft()

# Game state and background images
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
cart_page = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = event.pos
            
            if cart_page:
                back_menu_button = draw_cart()
                if back_menu_button.collidepoint(pos):
                    cart_page = False
                    game_state = "menu"
            elif show_queue:
                serve_rect, back_menu_button = draw_queue()
                if back_menu_button.collidepoint(pos):
                    show_queue = False

            if game_state == "main" and bt_Start_rect.collidepoint(pos):
                game_state = "menu"
            
            elif game_state == "menu":
                if cart_icon_rect.collidepoint(pos):
                    cart_page = True
                elif show_queue and serve_rect.collidepoint(pos):
                    serve_order()
                else:
                    handle_click(pos)
                    place_order_button = pygame.Rect(350, 700, 150, 50)
                    if place_order_button.collidepoint(pos):
                        place_order()
                    view_queue_button = pygame.Rect(50, 700, 150, 50)
                    if view_queue_button.collidepoint(pos):
                        show_queue = True

    if game_state == "main":
        screen.blit(bg_Main, (0, 0))
        screen.blit(bt_Start, bt_Start_rect)
    elif game_state == "menu":
        if show_queue:
            draw_queue()
        else:
            draw_menu()
            draw_order()
            place_order_button = pygame.Rect(350, 700, 150, 50)
            pygame.draw.rect(screen, GREEN, place_order_button)
            draw_text("Place Order", WHITE, 370, 710, font_small)
            view_queue_button = pygame.Rect(50, 700, 150, 50)
            pygame.draw.rect(screen, GREEN, view_queue_button)
            draw_text("View Queue", WHITE, 60, 710, font_small)

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()
