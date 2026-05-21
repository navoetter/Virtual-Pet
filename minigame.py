import pygame
import random
import sys


class MiniGame:
    def play(self, screen):

        clock = pygame.time.Clock()

        WIDTH, HEIGHT = screen.get_size()

        # Player
        player = pygame.Rect(WIDTH // 2 - 60, HEIGHT - 80, 120, 20)
        speed = 8

        # Food
        food = pygame.Rect(random.randint(0, WIDTH - 30), 0, 30, 30)
        food_speed = 6

        score = 0

        font = pygame.font.SysFont(None, 40)

        running = True

        while running:

            screen.fill((255, 255, 255))

            # Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Controls
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                player.x -= speed
            if keys[pygame.K_RIGHT]:
                player.x += speed

            # Boundaries
            if player.x < 0:
                player.x = 0
            if player.x > WIDTH - player.width:
                player.x = WIDTH - player.width

            # Food movement
            food.y += food_speed

            if food.y > HEIGHT:
                food.y = 0
                food.x = random.randint(0, WIDTH - 30)

            # Collision
            if player.colliderect(food):
                score += 1
                food.y = 0
                food.x = random.randint(0, WIDTH - 30)

            # Draw player
            pygame.draw.rect(screen, (0, 0, 0), player)

            # Draw food
            pygame.draw.rect(screen, (200, 0, 0), food)

            # Score
            text = font.render(f"Score: {score}", True, (0, 0, 0))
            screen.blit(text, (20, 20))

            # Hint
            hint = font.render("Press ESC to exit", True, (120, 120, 120))
            screen.blit(hint, (20, 60))

            # Exit
            if keys[pygame.K_ESCAPE]:
                return score

            pygame.display.flip()
            clock.tick(60)