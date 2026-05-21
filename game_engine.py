import pygame
import os
from game_logic import Pet
from minigame import MiniGame


class GameEngine:
    def __init__(self, pet_name: str):

        self.pet = Pet(pet_name)
        self.minigame = MiniGame()

        pygame.init()

        self.screen = pygame.display.set_mode((1200, 750))
        pygame.display.set_caption("Virtual Pet")

        self.clock = pygame.time.Clock()
        self.running = True

        self.font = pygame.font.SysFont(None, 48)
        self.small_font = pygame.font.SysFont(None, 32)

        self.width, self.height = self.screen.get_size()

        self.border = 20

        self.tick_timer = 0
        self.tick_delay = 1000

        BASE_DIR = os.path.dirname(__file__)
        TEXTURE_PATH = os.path.join(BASE_DIR, "textures")

        self.button_feed = pygame.image.load(
            os.path.join(TEXTURE_PATH, "button_feed.png")
        ).convert_alpha()

        self.button_play = pygame.image.load(
            os.path.join(TEXTURE_PATH, "button_play.png")
        ).convert_alpha()

        self.button_sleep = pygame.image.load(
            os.path.join(TEXTURE_PATH, "button_sleep.png")
        ).convert_alpha()

        self.button_feed = pygame.transform.scale(self.button_feed, (165, 149))
        self.button_play = pygame.transform.scale(self.button_play, (198, 99))
        self.button_sleep = pygame.transform.scale(self.button_sleep, (165, 115))

        self.feed_rect = self.button_feed.get_rect()
        self.play_rect = self.button_play.get_rect()
        self.sleep_rect = self.button_sleep.get_rect()

        self.pet_image = pygame.image.load(
            os.path.join(TEXTURE_PATH, "Slime.png")
        ).convert_alpha()

        self.pet_image = pygame.transform.scale(self.pet_image, (300, 300))

    # -------------------------
    def play_minigame(self):
        score = self.minigame.play(self.screen)
        self.pet.play(score)

    # -------------------------
    def handle_buttons(self, pos):

        if self.pet.sleeping:
            return

        if self.feed_rect.collidepoint(pos):
            self.pet.feed()

        elif self.play_rect.collidepoint(pos):
            self.play_minigame()

        elif self.sleep_rect.collidepoint(pos):
            self.pet.sleep()

    # -------------------------
    def draw_status_bar(self, x, y, value, max_value, color, label):

        label_text = self.small_font.render(
            f"{label}: {int(value)}",
            True,
            (0, 0, 0)
        )
        self.screen.blit(label_text, (x, y - 30))

        pygame.draw.rect(self.screen, (200, 200, 200), (x, y, 250, 25))

        fill_width = int((value / max_value) * 250)
        pygame.draw.rect(self.screen, color, (x, y, fill_width, 25))

        pygame.draw.rect(self.screen, (0, 0, 0), (x, y, 250, 25), 2)

    # -------------------------
    def render(self):

        self.screen.fill((20, 60, 20))

        pygame.draw.rect(
            self.screen,
            (255, 255, 255),
            (
                self.border,
                self.border,
                self.width - self.border * 2,
                self.height - self.border * 2
            )
        )

        name_text = self.font.render(self.pet.name, True, (0, 0, 0))
        self.screen.blit(name_text, (30, 20))

        self.draw_status_bar(50, 120, self.pet.hunger, 100, (255, 100, 100), "Sattheit")
        self.draw_status_bar(50, 190, self.pet.energy, 100, (100, 100, 255), "Energy")
        self.draw_status_bar(50, 260, self.pet.happiness, 100, (100, 255, 100), "Happiness")

        pet_rect = self.pet_image.get_rect(
            center=(self.width // 2, self.height // 2 - 50)
        )
        self.screen.blit(self.pet_image, pet_rect)

        # BUTTON POSITION (DEIN STYLE)
        spacing = 30
        start_x = self.width // 2 - 300
        button_y = 520

        self.feed_rect.topleft = (start_x, button_y - 17)
        self.play_rect.topleft = (start_x + 210, button_y)
        self.sleep_rect.topleft = (start_x + 420, button_y + 12)

        self.screen.blit(self.button_feed, self.feed_rect)
        self.screen.blit(self.button_play, self.play_rect)
        self.screen.blit(self.button_sleep, self.sleep_rect)

        # DEAD
        if not self.pet.alive:
            dead_text = self.font.render("Your pet died!", True, (255, 0, 0))
            dead_rect = dead_text.get_rect(center=(self.width // 2, 50))
            self.screen.blit(dead_text, dead_rect)

        # 💤 SLEEP UI
        if self.pet.sleeping:

            overlay = pygame.Surface((self.width, self.height))
            overlay.set_alpha(140)
            overlay.fill((0, 0, 0))
            self.screen.blit(overlay, (0, 0))

            zzz = self.font.render("Zzz...", True, (255, 255, 255))
            self.screen.blit(
                zzz,
                (self.width // 2 - zzz.get_width() // 2, 100)
            )

            info = self.small_font.render(
                "Sleeping until energy is full",
                True,
                (200, 200, 200)
            )
            self.screen.blit(
                info,
                (self.width // 2 - info.get_width() // 2, 160)
            )

        pygame.display.flip()

    # -------------------------
    def run(self):

        while self.running:

            dt = self.clock.tick(60)
            self.tick_timer += dt

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.handle_buttons(event.pos)

            if self.tick_timer >= self.tick_delay:
                self.pet.tick()
                self.tick_timer = 0

            self.render()

        pygame.quit()