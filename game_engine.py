import pygame
from game_logic import Pet
from minigame import MiniGame


class GameEngine:
    def __init__(self, pet_name: str):
        self.pet = Pet(pet_name)
        self.minigame = MiniGame()

        pygame.init()
        self.screen = pygame.display.set_mode((1200, 750))
        pygame.display.set_caption("Pet Name Display")

        self.clock = pygame.time.Clock()
        self.running = True

        self.font = pygame.font.SysFont(None, 48)
        self.button_font = pygame.font.SysFont(None, 32)

        self.button_rect = pygame.Rect(0, 0, 220, 60)

        self.ltg_image = pygame.image.load("Slime.png")
        self.ltg_image = pygame.transform.scale(self.ltg_image, (300, 300))

    def play_minigame(self):
        won = self.minigame.play()
        self.pet.play(won)

    def render(self):
        self.screen.fill((255, 255, 255))

        name_text = self.font.render(self.pet.name, True, (0, 0, 0))
        self.screen.blit(name_text, (20, 20))

        image_rect = self.ltg_image.get_rect()
        image_rect.center = (1200 // 2, 750 // 2 - 80)
        self.screen.blit(self.ltg_image, image_rect)

        # Button
        self.button_rect.center = (1200 // 2, image_rect.bottom + 60)
        pygame.draw.rect(self.screen, (200, 200, 200), self.button_rect)
        
        

        btn_text = self.button_font.render("Play Minigame", True, (0, 0, 0))
        text_rect = btn_text.get_rect(center=self.button_rect.center)
        self.screen.blit(btn_text, text_rect)

        pygame.display.flip()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.button_rect.collidepoint(event.pos):
                            self.play_minigame()

            self.render()
            self.clock.tick(60)

        pygame.quit()