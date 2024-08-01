import pygame
import random
import tkinter as tk
from tkinter import simpledialog
from bubble_sort import bubble_sort
from insertion_sort import insertion_sort

# Initialize Pygame
pygame.init()

# Screen settings
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sorting Algorithm Visualizer")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (200, 200, 200)
LIGHT_BLUE = (173, 216, 230)

# Default number of elements and default elements
num_elements = 100
elements = [random.randint(1, height) for _ in range(num_elements)]
element_width = width // num_elements
custom_array = False

# Speed control options
speeds = [0.1, 0.05, 0.01]
speed_labels = ["Speed 1 (0.1s)", "Speed 2 (0.05s)", "Speed 3 (0.01s)"]
speed = speeds[0]
selected_speed_index = 0

def draw_elements(elements, color_positions={}, show_values=False):
    screen.fill(WHITE)
    font = pygame.font.SysFont('Arial', 12)
    for i, val in enumerate(elements):
        color = color_positions.get(i, BLACK)
        pygame.draw.rect(screen, color, (i * element_width, height - val, element_width, val))
        if show_values:
            value_surface = font.render(str(val), True, BLACK)
            screen.blit(value_surface, (i * element_width, height - val - 20))
    pygame.display.update()

def get_user_input():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    user_input = simpledialog.askstring("Input", "Enter the array values separated by commas or periods:")
    root.destroy()
    if user_input:
        try:
            # Replace periods with commas for uniformity
            user_input = user_input.replace('.', ',')
            return [int(x) for x in user_input.split(',')]
        except ValueError:
            print("Invalid input. Please enter integers separated by commas or periods.")
            return None
    return None

def draw_buttons():
    default_color = LIGHT_BLUE if not custom_array else GREY
    custom_color = LIGHT_BLUE if custom_array else GREY
    pygame.draw.rect(screen, default_color, (width//2 - 250, 50, 200, 50))
    pygame.draw.rect(screen, custom_color, (width//2 + 50, 50, 200, 50))
    font = pygame.font.SysFont('Arial', 25)
    screen.blit(font.render('Default Array', True, BLACK), (width//2 - 225, 65))
    screen.blit(font.render('Custom Array', True, BLACK), (width//2 + 75, 65))
    pygame.display.update()

def draw_speed_buttons():
    y_offset = 180
    button_height = 50
    for i, label in enumerate(speed_labels):
        color = LIGHT_BLUE if i == selected_speed_index else GREY
        pygame.draw.rect(screen, color, (width//2 - 75, y_offset + i * (button_height + 20), 150, button_height))
        font = pygame.font.SysFont('Arial', 20)
        screen.blit(font.render(label, True, BLACK), (width//2 - 60, y_offset + i * (button_height + 20) + 15))
    pygame.display.update()

def main():
    global elements, num_elements, element_width, custom_array, speed, selected_speed_index
    sorting = False
    sorting_algorithm = None
    array_chosen = False

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b and not sorting and array_chosen:
                    sorting = True
                    sorting_algorithm = bubble_sort(elements, draw_elements, speed, custom_array)
                if event.key == pygame.K_i and not sorting and array_chosen:
                    sorting = True
                    sorting_algorithm = insertion_sort(elements, draw_elements, speed, custom_array)
                if event.key == pygame.K_r and array_chosen:
                    sorting = False
                    elements = [random.randint(1, height) for _ in range(num_elements)]
                    draw_elements(elements)
                if event.key == pygame.K_BACKSPACE:
                    sorting = False
                    array_chosen = False
                    screen.fill(BLACK)
                    pygame.display.update()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if width//2 - 250 <= mouse_x <= width//2 - 50 and 50 <= mouse_y <= 100:
                    elements = [random.randint(1, height) for _ in range(num_elements)]
                    custom_array = False
                    array_chosen = True
                    draw_elements(elements)
                elif width//2 + 50 <= mouse_x <= width//2 + 250 and 50 <= mouse_y <= 100:
                    user_elements = get_user_input()
                    if user_elements:
                        elements = user_elements
                        num_elements = len(elements)
                        element_width = width // num_elements
                        custom_array = True
                        array_chosen = True
                        draw_elements(elements, show_values=custom_array)
                elif width//2 - 75 <= mouse_x <= width//2 + 75:
                    for i, sp in enumerate(speeds):
                        if 180 + i * 70 <= mouse_y <= 230 + i * 70:
                            speed = sp
                            selected_speed_index = i
                            draw_speed_buttons()
                            draw_buttons()

        if sorting:
            try:
                next(sorting_algorithm)
            except StopIteration:
                sorting = False

        if not array_chosen:
            draw_buttons()
            draw_speed_buttons()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
