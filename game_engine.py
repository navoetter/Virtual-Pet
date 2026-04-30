import pygame
from game_logic import Pet
from minigame import MiniGame

class GameEngine:
    def __init__(self, pet_name: str):
        self.pet = Pet(pet_name)  
        self.minigame = MiniGame()

        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Pet Name Display")

        self.clock = pygame.time.Clock()
        self.running = True

        self.font = pygame.font.SysFont(None, 48)
        self.button_font = pygame.font.SysFont(None, 32)

        self.button_rect = pygame.Rect(20, 80, 200, 50)

    def play_minigame(self):
        won = self.minigame.play()
        self.pet.play(won)

    def render(self):
        self.screen.fill((0, 0, 0))

        text = self.font.render(self.pet.name, True, (255, 255, 255))
        self.screen.blit(text, (20, 20))

        pygame.draw.rect(self.screen, (0, 120, 200), self.button_rect)
        btn_text = self.button_font.render("Play Minigame", True, (255, 255, 255))
        self.screen.blit(btn_text, (30, 92))

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