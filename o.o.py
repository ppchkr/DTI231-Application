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

# Cart icon
cart_icon = pygame.image.load("picture\\cart.png")
cart_icon = pygame.transform.scale(cart_icon, (50, 50))  # Resize icon
cart_icon_rect = cart_icon.get_rect(topright=(SCREEN_WIDTH - 20, 20))

# Function to draw text
def draw_text(text, color, x, y, font_type=font):
    label = font_type.render(text, True, color)
    screen.blit(label, (x, y))

# Function to draw menu items
def draw_menu():
    screen.fill(WHITE)
    draw_text("Restaurant Menu", BLACK, 150, 50)
    for item in menu_items:
        img = pygame.image.load(item["image"])
        img = pygame.transform.scale(img, (130, 130))  # Adjust size
        screen.blit(img, item["rect"])

# Function to draw order summary
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

# Function to draw cart page
def draw_cart_page():
    screen.fill(WHITE)
    draw_text("Your Cart", BLACK, 50, 50)
    y_offset = 100
    total_price = 0

    if not order:
        draw_text("Your cart is empty.", BLACK, 50, y_offset)
    else:
        for name, details in order.items():
            draw_text(f"{name} x {details['quantity']} - ฿{details['quantity'] * details['price']:.2f}", BLACK, 50, y_offset)
            y_offset += 40
            total_price += details['quantity'] * details['price']
        draw_text(f"Total: ฿{total_price:.2f}", RED, 50, y_offset + 20)

    # Back to Menu button
    back_menu_button = pygame.Rect(350, 700, 150, 50)
    pygame.draw.rect(screen, GREEN, back_menu_button)
    draw_text("Back to Menu", WHITE, 360, 710, font_small)

    return back_menu_button

# Function to draw queue
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
            y_offset += 10  # Add space between queues

    # Serve button
    serve_rect = pygame.Rect(50, 700, 150, 50)
    pygame.draw.rect(screen, RED, serve_rect)
    draw_text("Serve", WHITE, 70, 710, font_small)

    # Back to Menu button
    back_menu_button = pygame.Rect(350, 700, 150, 50)
    pygame.draw.rect(screen, GREEN, back_menu_button)
    draw_text("Back to Menu", WHITE, 360, 710, font_small)

    return serve_rect, back_menu_button

# Function to handle clicks on menu items
def handle_click(pos):
    global cart_page, game_state
    if cart_icon_rect.collidepoint(pos) and game_state == "menu":
        cart_page = True
        return

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
        print(f"Serving order: {queue[0]}")  # Debug statement
        queue.popleft()
        print(f"Remaining queue: {list(queue)}")  # Debug remaining queue

# Game state and background images
bg_Main = pygame.image.load("picture\\aa00.png")
bg_Main = pygame.transform.scale(bg_Main, (SCREEN_WIDTH, SCREEN_HEIGHT))

bt_Start = pygame.image.load("picture\\botton1.png")
bt_Start = pygame.transform.scale(bt_Start, (150, 50))
bt_Start_rect = bt_Start.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 130))

running = True
game_state = "main"
cart_page = False
show_queue = False

# Main game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = event.pos

            if cart_page:
                back_menu_button = draw_cart_page()
                place_order_button = pygame.Rect(200, 0, 150, 50)
                if place_order_button.collidepoint(pos):
                    place_order()
                if back_menu_button.collidepoint(pos):
                    cart_page = False
                    game_state = "menu"
            elif game_state == "menu":
                if show_queue:
                    serve_rect, back_menu_button = draw_queue()
                    if serve_rect.collidepoint(pos):
                        serve_order()
                    elif back_menu_button.collidepoint(pos):
                        show_queue = False
                else:
                    handle_click(pos)
                    place_order_button = pygame.Rect(350, 700, 150, 50)
                    if place_order_button.collidepoint(pos):
                        place_order()
                        print("Place ordered")
                    view_queue_button = pygame.Rect(50, 700, 150, 50)
                    if view_queue_button.collidepoint(pos):
                        show_queue = True
            elif game_state == "main" and bt_Start_rect.collidepoint(pos):
                game_state = "menu"

    if cart_page:
        draw_cart_page()
    elif game_state == "main":
        screen.blit(bg_Main, (0, 0))
        screen.blit(bt_Start, bt_Start_rect)
    elif game_state == "menu":
        if show_queue:
            draw_queue()
        else:
            draw_menu()
            #draw_order()
            place_order_button = pygame.Rect(350, 700, 150, 50)
            pygame.draw.rect(screen, GREEN, place_order_button)
            draw_text("Place Order", WHITE, 370, 710, font_small)
            view_queue_button = pygame.Rect(50, 700, 150, 50)
            pygame.draw.rect(screen, GREEN, view_queue_button)
            draw_text("View Queue", WHITE, 60, 710, font_small)

    if game_state == "menu":
        screen.blit(cart_icon, cart_icon_rect)

    pygame.display.flip()
    pygame.time.Clock().tick(30)

pygame.quit()
sys.exit()
