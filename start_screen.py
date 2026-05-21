import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Virtual Pet - Start")

font = pygame.font.SysFont("arial", 40)
small_font = pygame.font.SysFont("arial", 28)

clock = pygame.time.Clock()


def start_screen():
    input_text = ""

    while True:
        # 🖥️ WHITE BACKGROUND
        screen.fill((255, 255, 255))

        # Titel
        title = font.render("Name your Pet", True, (0, 0, 0))
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 120))

        # Input box
        box_rect = pygame.Rect(WIDTH // 2 - 200, 220, 400, 60)
        pygame.draw.rect(screen, (230, 230, 230), box_rect, border_radius=10)
        pygame.draw.rect(screen, (0, 0, 0), box_rect, 2, border_radius=10)

        text_surface = small_font.render(input_text, True, (0, 0, 0))
        screen.blit(text_surface, (box_rect.x + 10, box_rect.y + 15))

        # Hint
        hint = small_font.render("Press ENTER to start", True, (120, 120, 120))
        screen.blit(hint, (WIDTH // 2 - hint.get_width() // 2, 320))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if input_text.strip() != "":
                        return input_text

                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]

                else:
                    if len(input_text) < 12:
                        input_text += event.unicode

        pygame.display.flip()
        clock.tick(60)