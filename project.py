import pygame

import sys
 
# Initialize pygame

pygame.init()
 
# Screen dimensions

WIDTH, HEIGHT = 400, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Order Food App")
 
# Colors

WHITE = (255, 255, 255)

BLACK = (0, 0, 0)

GRAY = (200, 200, 200)

LIGHT_GREEN = (144, 238, 144)
 
# Fonts

font = pygame.font.Font(None, 36)

small_font = pygame.font.Font(None, 24)
 
# Food menu items

menu_items = [

    {"name": "ผัดกะเพรา", "price": 35},

    {"name": "ผัดซีอิ๊ว", "price": 35},

    {"name": "ข้าวผัด", "price": 35},

    {"name": "ผัดไทย", "price": 35},

    {"name": "ไก่ทอด", "price": 30},

    {"name": "ผัดพริกแกง", "price": 35},

    {"name": "ต้มยำ", "price": 60},

    {"name": "ข้าวเปล่า", "price": 30},

]
 
# Button dimensions

BUTTON_WIDTH = 180

BUTTON_HEIGHT = 50

PADDING = 20
 
# Selected items

selected_items = []
 
def draw_menu():

    screen.fill(WHITE)

    y_offset = PADDING
 
    # Draw menu items

    for item in menu_items:

        # Button rectangle

        button_rect = pygame.Rect(PADDING, y_offset, BUTTON_WIDTH, BUTTON_HEIGHT)

        pygame.draw.rect(screen, LIGHT_GREEN if item in selected_items else GRAY, button_rect)

        pygame.draw.rect(screen, BLACK, button_rect, 2)
 
        # Text

        text = font.render(f"{item['name']} ฿{item['price']}", True, BLACK)

        screen.blit(text, (button_rect.x + 10, button_rect.y + 10))
 
        y_offset += BUTTON_HEIGHT + PADDING
 
    # Draw total price

    total_price = sum(item['price'] for item in selected_items)

    total_text = font.render(f"Total: ฿{total_price}", True, BLACK)

    screen.blit(total_text, (PADDING, y_offset))
 
def handle_click(pos):

    y_offset = PADDING
 
    for item in menu_items:

        button_rect = pygame.Rect(PADDING, y_offset, BUTTON_WIDTH, BUTTON_HEIGHT)

        if button_rect.collidepoint(pos):

            if item in selected_items:

                selected_items.remove(item)  # Deselect item

            else:

                selected_items.append(item)  # Select item

        y_offset += BUTTON_HEIGHT + PADDING
 
# Main loop

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            handle_click(event.pos)
 
    draw_menu()

    pygame.display.flip()
 
pygame.quit()

sys.exit()
 
import pygame

import sys
 
# Initialize pygame

pygame.init()
 
# Screen dimensions

WIDTH, HEIGHT = 400, 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Order Food App")
 
# Colors

WHITE = (255, 255, 255)

BLACK = (0, 0, 0)

GRAY = (240, 240, 240)

GREEN = (34, 139, 34)

LIGHT_GREEN = (144, 238, 144)

DARK_GRAY = (50, 50, 50)
 
# Fonts

font = pygame.font.Font(pygame.font.match_font('arial', bold=True), 28)

small_font = pygame.font.Font(pygame.font.match_font('arial'), 20)
 
# Food menu items

menu_items = [

    {"name": "🍲 ผัดกะเพรา", "price": 35},

    {"name": "🍲 ผัดซีอิ๊ว", "price": 35},

    {"name": "🍲 ข้าวผัด", "price": 35},

    {"name": "🍲 ผัดไทย", "price": 35},

    {"name": "🍗 ไก่ทอด", "price": 30},

    {"name": "🍲 ผัดพริกแกง", "price": 35},

    {"name": "🍣 ต้มยำ", "price": 60},

    {"name": "🍽 ข้าวเปล่า", "price": 30},

]
 
# Button dimensions

BUTTON_WIDTH = WIDTH - 40

BUTTON_HEIGHT = 60

PADDING = 20
 
# Selected items

selected_items = []
 
def draw_header():

    pygame.draw.rect(screen, DARK_GRAY, (0, 0, WIDTH, 80))

    header_text = font.render("Let's order great meals!", True, WHITE)

    screen.blit(header_text, (20, 20))
 
def draw_menu():

    screen.fill(WHITE, (0, 80, WIDTH, HEIGHT - 80))

    y_offset = 100
 
    # Draw menu items

    for item in menu_items:

        button_rect = pygame.Rect((WIDTH - BUTTON_WIDTH) // 2, y_offset, BUTTON_WIDTH, BUTTON_HEIGHT)

        pygame.draw.rect(screen, LIGHT_GREEN if item in selected_items else GRAY, button_rect, border_radius=10)

        pygame.draw.rect(screen, GREEN, button_rect, 2, border_radius=10)
 
        # Text

        text = small_font.render(f"{item['name']} - ฿{item['price']}", True, BLACK if item not in selected_items else DARK_GRAY)

        screen.blit(text, (button_rect.x + 20, button_rect.y + 15))
 
        y_offset += BUTTON_HEIGHT + PADDING
 
    # Draw total price and checkout button

    total_price = sum(item['price'] for item in selected_items)

    total_rect = pygame.Rect((WIDTH - BUTTON_WIDTH) // 2, y_offset, BUTTON_WIDTH, BUTTON_HEIGHT)

    pygame.draw.rect(screen, GREEN, total_rect, border_radius=10)

    total_text = font.render(f"Checkout - ฿{total_price}", True, WHITE)

    screen.blit(total_text, (total_rect.x + 20, total_rect.y + 15))
 
def handle_click(pos):

    y_offset = 100
 
    for item in menu_items:

        button_rect = pygame.Rect((WIDTH - BUTTON_WIDTH) // 2, y_offset, BUTTON_WIDTH, BUTTON_HEIGHT)

        if button_rect.collidepoint(pos):

            if item in selected_items:

                selected_items.remove(item)  # Deselect item

            else:

                selected_items.append(item)  # Select item

        y_offset += BUTTON_HEIGHT + PADDING
 
    # Handle checkout button click

    total_rect = pygame.Rect((WIDTH - BUTTON_WIDTH) // 2, y_offset, BUTTON_WIDTH, BUTTON_HEIGHT)

    if total_rect.collidepoint(pos):

        print("Order Confirmed!", selected_items)

        selected_items.clear()
 
# Main loop

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

            handle_click(event.pos)
 
    draw_header()

    draw_menu()

    pygame.display.flip()
 
pygame.quit()

sys.exit()
 