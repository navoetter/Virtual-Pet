import pygame
from game_logic import Pet


class GameEngine:
    def __init__(self, pet_name: str):
        self.pet = Pet(pet_name)

        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Pet Name Display")

        self.clock = pygame.time.Clock()
        self.running = True

        self.font = pygame.font.SysFont(None, 48)

    def render(self):
        self.screen.fill((0, 0, 0))

        text = self.font.render(self.pet.name, True, (255, 255, 255))
        self.screen.blit(text, (20, 20))

        pygame.display.flip()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.render()
            self.clock.tick(60)

        pygame.quit()