import pygame
import random
import sys

pygame.init()

screen_width = 600
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Click the Colors")

icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

# Create a font for the score display
font = pygame.font.Font(None, 36)

def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def draw_random_circle():
    max_radius = 60  # Maximum radius
    radius = random.randint(30, max_radius)
    x = random.randint(radius, screen_width - radius)
    y = random.randint(radius, screen_height - radius)
    color = random_color()
    return (x, y, radius, color)

circles = []
score = 0  # Initialize the score
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            for circle in circles:
                x, y, radius, color = circle

                if pygame.Rect(x - radius, y - radius, 2 * radius, 2 * radius).collidepoint(event.pos):
                    circles.remove(circle)
                    score += 1  # Increase the score when a circle is clicked

    if len(circles) < 5:
        circles.append(draw_random_circle())

    screen.fill((255, 255, 255))

    for circle in circles:
        x, y, radius, color = circle
        pygame.draw.circle(screen, color, (x, y), radius)

    # Display the score in the upper left corner
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
sys.exit()
