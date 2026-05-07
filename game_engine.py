import pygame
import os
from game_logic import Pet
from minigame import MiniGame


class GameEngine:
    def __init__(self, pet_name: str):
        self.pet = Pet(pet_name)
        self.minigame = MiniGame()

        pygame.init()
        self.screen = pygame.display.set_mode((1920, 1080))
        pygame.display.set_caption("Pet Game")

        self.clock = pygame.time.Clock()
        self.running = True

        self.font = pygame.font.SysFont(None, 48)

        self.width, self.height = self.screen.get_size()

        # -------------------------
        # PATH SETUP
        # -------------------------
        BASE_DIR = os.path.dirname(__file__)
        TEXTURE_PATH = os.path.join(BASE_DIR, "textures")

        # -------------------------
        # ICONS (LEFT SIDE) - NO SCALING
        # -------------------------
        self.icon_hunger = pygame.image.load(os.path.join(TEXTURE_PATH, "icon_hunger.png"))
        self.icon_life = pygame.image.load(os.path.join(TEXTURE_PATH, "icon_life.png"))
        self.icon_sleep = pygame.image.load(os.path.join(TEXTURE_PATH, "icon_sleep.png"))

        # -------------------------
        # BUTTONS (RIGHT SIDE) - NO SCALING
        # -------------------------
        self.button_feed = pygame.image.load(os.path.join(TEXTURE_PATH, "button_feed.png"))
        self.button_play = pygame.image.load(os.path.join(TEXTURE_PATH, "button_play.png"))
        self.button_sleep = pygame.image.load(os.path.join(TEXTURE_PATH, "button_sleep.png"))

        # Button rects (for clicking)
        self.feed_rect = self.button_feed.get_rect()
        self.play_rect = self.button_play.get_rect()
        self.sleep_rect = self.button_sleep.get_rect()

        # -------------------------
        # PET IMAGE
        # -------------------------
        self.pet_image = pygame.image.load(os.path.join("Slime.png"))

    # -------------------------
    # GAME ACTIONS
    # -------------------------
    def play_minigame(self):
        won = self.minigame.play()
        self.pet.play(won)

    def handle_buttons(self, pos):
        if self.feed_rect.collidepoint(pos):
            self.pet.feed()

        elif self.play_rect.collidepoint(pos):
            self.play_minigame()

        elif self.sleep_rect.collidepoint(pos):
            self.pet.sleep()

    # -------------------------
    # DRAWING
    # -------------------------
    def render(self):
        self.screen.fill((255, 255, 255))

        # Pet name
        name_text = self.font.render(self.pet.name, True, (0, 0, 0))
        self.screen.blit(name_text, (20, 20))

        # Pet center image
        pet_rect = self.pet_image.get_rect(
            center=(self.width // 2, self.height // 2 - 50)
        )
        self.screen.blit(self.pet_image, pet_rect)

        # -------------------------
        # LEFT ICONS (FIXED ALIGNMENT)
        # -------------------------
        left_x = 60
        spacing = 150
        start_y = 250

        self.screen.blit(self.icon_hunger, (left_x, start_y))
        self.screen.blit(self.icon_life, (left_x, start_y + spacing))
        self.screen.blit(self.icon_sleep, (left_x, start_y + spacing * 2))

        # -------------------------
        # RIGHT BUTTONS (FIXED ALIGNMENT)
        # -------------------------
        right_x = self.width - 300
        center_y = self.height // 2

        self.feed_rect.topleft = (right_x, center_y - 120)
        self.play_rect.topleft = (right_x, center_y)
        self.sleep_rect.topleft = (right_x, center_y + 120)

        self.screen.blit(self.button_feed, self.feed_rect)
        self.screen.blit(self.button_play, self.play_rect)
        self.screen.blit(self.button_sleep, self.sleep_rect)

        pygame.display.flip()

    # -------------------------
    # MAIN LOOP
    # -------------------------
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.handle_buttons(event.pos)

            self.render()
            self.clock.tick(60)

        pygame.quit()