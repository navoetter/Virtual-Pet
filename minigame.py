import pygame
import random
import sys


class MiniGame:
    def play(self, screen):

        clock = pygame.time.Clock()
        WIDTH, HEIGHT = screen.get_size()

        font = pygame.font.SysFont(None, 40)

        mode = random.choice(["catch", "dodge"])

        # Catch
       
        if mode == "catch":

            player = pygame.Rect(WIDTH // 2 - 60, HEIGHT - 80, 120, 20)
            speed = 8

            food = pygame.Rect(random.randint(0, WIDTH - 30), 0, 30, 30)
            food_speed = 6

            score = 0
            running = True

            while running:

                screen.fill((255, 255, 255))
                screen.blit(
                    font.render("Catch red blocks!", True, (150, 150, 150)),
                    (20, 60)
                )

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                keys = pygame.key.get_pressed()

                if keys[pygame.K_LEFT]:
                    player.x -= speed
                if keys[pygame.K_RIGHT]:
                    player.x += speed

                player.x = max(0, min(WIDTH - player.width, player.x))

                food.y += food_speed

                if food.y > HEIGHT:
                    food.y = 0
                    food.x = random.randint(0, WIDTH - 30)

                if player.colliderect(food):
                    score += 1
                    food.y = 0
                    food.x = random.randint(0, WIDTH - 30)

                pygame.draw.rect(screen, (0, 0, 0), player)
                pygame.draw.rect(screen, (200, 0, 0), food)

                screen.blit(font.render(f"Score: {score}", True, (0, 0, 0)), (20, 20))

                if keys[pygame.K_ESCAPE]:
                    return score

                pygame.display.flip()
                clock.tick(60)

        #Dodge
        else:

            player = pygame.Rect(WIDTH // 2 - 60, HEIGHT - 80, 120, 20)
            speed = 8

            blocks = []
            block_size = 30
            block_speed = 6

            spawn_timer = 0
            score = 0
            running = True

            while running:

                dt = clock.tick(60)
                spawn_timer += dt

                screen.fill((255, 255, 255))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                if spawn_timer > 500:
                    spawn_timer = 0
                    x = random.randint(0, WIDTH - block_size)
                    blocks.append(pygame.Rect(x, 0, block_size, block_size))

                keys = pygame.key.get_pressed()

                if keys[pygame.K_LEFT]:
                    player.x -= speed
                if keys[pygame.K_RIGHT]:
                    player.x += speed

                player.x = max(0, min(WIDTH - player.width, player.x))

                pygame.draw.rect(screen, (0, 0, 0), player)

                for block in blocks[:]:
                    block.y += block_speed

                    if block.y > HEIGHT:
                        blocks.remove(block)
                        score += 1

                    if player.colliderect(block):
                        return score

                    pygame.draw.rect(screen, (200, 0, 0), block)

                screen.blit(font.render(f"Score: {score}", True, (0, 0, 0)), (20, 20))

                screen.blit(
                    font.render("Avoid red blocks!", True, (150, 150, 150)),
                    (20, 60)
                )

                if keys[pygame.K_ESCAPE]:
                    return score

                pygame.display.flip()