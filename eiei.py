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
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 650
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("GrabFood Queue Manager")

# Font for text
font = pygame.font.Font(None, 36)
font_small = pygame.font.Font(None, 28)

# Food items for menu
menu_items = [
    {"name": "Burger", "price": 5, "rect": pygame.Rect(100, 100, 200, 50)},
    {"name": "Pizza", "price": 8, "rect": pygame.Rect(100, 200, 200, 50)},
    {"name": "Sushi", "price": 10, "rect": pygame.Rect(100, 300, 200, 50)},
    {"name": "Pasta", "price": 7, "rect": pygame.Rect(100, 400, 200, 50)},
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
    for item in menu_items:
        pygame.draw.rect(screen, BLUE, item["rect"])
        draw_text(f"{item['name']} - ${item['price']}", WHITE, item["rect"].x + 20, item["rect"].y + 10)

def draw_order():
    draw_text("Your Order:", BLACK, 500, 50)
    if not order:
        draw_text("No items ordered yet.", BLACK, 500, 100)
    else:
        y_offset = 100
        total_price = 0
        for name, details in order.items():
            draw_text(f"{name} x {details['quantity']} - ${details['quantity'] * details['price']:.2f}", BLACK, 500, y_offset)
            y_offset += 40
            total_price += details['quantity'] * details['price']
        draw_text(f"Total: ${total_price:.2f}", RED, 500, y_offset + 20)

def draw_queue():
    screen.fill(WHITE)
    draw_text("Order Queue", BLACK, 50, 50)
    y_offset = 100
    if not queue:
        draw_text("No orders in queue.", BLACK, 50, y_offset)
    else:
        for i, queued_order in enumerate(queue):
            draw_text(f"Order {i+1}: {queued_order}", BLACK, 50, y_offset)
            y_offset += 40
    # Draw Serve button
    serve_rect = pygame.Rect(50, 500, 150, 50)
    pygame.draw.rect(screen, RED, serve_rect)
    draw_text("Serve", WHITE, 70, 510, font_small)
    return serve_rect

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

            if game_state == "main":
                if bt_Start_rect.collidepoint(pos):
                    game_state = "menu"
            
            elif game_state == "menu":
                if show_queue:
                    serve_rect = draw_queue()
                    if serve_rect.collidepoint(pos):
                        serve_order()
                else:
                    for item in menu_items:
                        if item["rect"].collidepoint(pos):
                            handle_click(pos)  # Add item to order
                    place_order_button = pygame.Rect(600, 500, 150, 50)
                    if place_order_button.collidepoint(pos):
                        place_order()
                    view_queue_button = pygame.Rect(50, 500, 150, 50)
                    if view_queue_button.collidepoint(pos):
                        show_queue = True

            if show_queue:
                view_menu_button = pygame.Rect(300, 500, 150, 50)
                if view_menu_button.collidepoint(pos):
                    show_queue = False

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
