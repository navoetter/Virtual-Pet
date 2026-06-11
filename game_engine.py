import pygame
import os
import json
from game_logic import Pet
from minigame import MiniGame

SAVE_FILE = "pet_data.json"

class GameEngine:
    def __init__(self, pet_name: str):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 750))
        pygame.display.set_caption("Virtual Pet")

        self.pet = self.load_pet(pet_name)
        self.minigame = MiniGame()

        self.clock = pygame.time.Clock()
        self.running = True

        self.font = pygame.font.SysFont(None, 48)
        self.big_font = pygame.font.SysFont(None, 72) # Für das Level-Up
        self.small_font = pygame.font.SysFont(None, 32)

        self.width, self.height = self.screen.get_size()
        self.border = 20

        self.tick_timer = 0
        self.tick_delay = 1000

        self.level_timer = 0
        self.level_interval = 60000
        
        # Neuer Zustand für den Sonderbildschirm
        self.level_up_screen = False 

        BASE_DIR = os.path.dirname(__file__)
        TEXTURE_PATH = os.path.join(BASE_DIR, "textures")

        self.button_feed = pygame.image.load(os.path.join(TEXTURE_PATH, "button_feed.png")).convert_alpha()
        self.button_play = pygame.image.load(os.path.join(TEXTURE_PATH, "button_play.png")).convert_alpha()
        self.button_sleep = pygame.image.load(os.path.join(TEXTURE_PATH, "button_sleep.png")).convert_alpha()

        self.button_feed = pygame.transform.scale(self.button_feed, (165, 149))
        self.button_play = pygame.transform.scale(self.button_play, (198, 99))
        self.button_sleep = pygame.transform.scale(self.button_sleep, (165, 115))

        self.feed_rect = self.button_feed.get_rect()
        self.play_rect = self.button_play.get_rect()
        self.sleep_rect = self.button_sleep.get_rect()

        self.revive_rect = pygame.Rect(self.width // 2 - 220, 200, 200, 60)
        self.new_pet_rect = pygame.Rect(self.width // 2 + 20, 200, 200, 60)

        self.pet_image = pygame.image.load(os.path.join(TEXTURE_PATH, "Slime.png")).convert_alpha()
        self.pet_image = pygame.transform.scale(self.pet_image, (300, 300))

    def load_pet(self, default_name):
        if os.path.exists(SAVE_FILE):
            try:
                with open(SAVE_FILE, "r") as f:
                    data = json.load(f)
                loaded_pet = Pet.from_dict(data)
                if loaded_pet.alive:
                    return loaded_pet
            except Exception:
                pass
        return Pet(default_name)

    def save_pet(self):
        with open(SAVE_FILE, "w") as f:
            json.dump(self.pet.to_dict(), f)

    def play_minigame(self):
        score = self.minigame.play(self.screen)
        self.pet.play(score)

    def handle_buttons(self, pos):
        # 1. Wenn der Level-Up-Bildschirm da ist, schließt jeder Klick ihn
        if self.level_up_screen:
            self.level_up_screen = False
            return

        # 2. Wenn das Pet tot ist
        if not self.pet.alive:
            if self.revive_rect.collidepoint(pos):
                self.pet.alive = True
                self.pet.level = 1       # LEVEL WIRD ZURÜCKGESETZT
                self.pet.hunger = 90
                self.pet.energy = 100
                self.pet.happiness = 100
                self.level_timer = 0     # Timer für das nächste Level auch zurücksetzen
            elif self.new_pet_rect.collidepoint(pos):
                if os.path.exists(SAVE_FILE):
                    os.remove(SAVE_FILE)
                self.running = False
                os.system('python main.py') if os.name == 'nt' else os.system('python3 main.py')
                exit()
            return

        if self.pet.sleeping:
            return

        if self.feed_rect.collidepoint(pos):
            self.pet.feed()
        elif self.play_rect.collidepoint(pos):
            self.play_minigame()
        elif self.sleep_rect.collidepoint(pos):
            self.pet.sleep()

    def draw_status_bar(self, x, y, value, max_value, color, label):
        value = max(0, min(value, max_value))
        label_text = self.small_font.render(f"{label}: {int(value)}", True, (0, 0, 0))
        self.screen.blit(label_text, (x, y - 30))

        bar_width = 250
        pygame.draw.rect(self.screen, (200, 200, 200), (x, y, bar_width, 25))
        fill_width = int((value / max_value) * bar_width)
        pygame.draw.rect(self.screen, color, (x, y, fill_width, 25))
        pygame.draw.rect(self.screen, (0, 0, 0), (x, y, bar_width, 25), 2)

    def render(self):
        self.screen.fill((20, 60, 20))
        pygame.draw.rect(self.screen, (255, 255, 255), (self.border, self.border, self.width - self.border * 2, self.height - self.border * 2))

        name_text = self.font.render(self.pet.name, True, (0, 0, 0))
        self.screen.blit(name_text, (30, 20))

        self.draw_status_bar(50, 120, self.pet.hunger, 100, (255, 100, 100), "Fullness")
        self.draw_status_bar(50, 190, self.pet.energy, 100, (100, 100, 255), "Energy")
        self.draw_status_bar(50, 260, self.pet.happiness, 100, (100, 255, 100), "Happiness")

        pet_rect = self.pet_image.get_rect(center=(self.width // 2, self.height // 2 - 50))
        self.screen.blit(self.pet_image, pet_rect)

        start_x = self.width // 2 - 300
        button_y = 520

        self.feed_rect.topleft = (start_x, button_y - 17)
        self.play_rect.topleft = (start_x + 210, button_y)
        self.sleep_rect.topleft = (start_x + 420, button_y + 12)

        self.screen.blit(self.button_feed, self.feed_rect)
        self.screen.blit(self.button_play, self.play_rect)
        self.screen.blit(self.button_sleep, self.sleep_rect)

        level_text = self.small_font.render(f"Level {self.pet.level}", True, (0, 0, 0))
        self.screen.blit(level_text, (self.border + 10, self.height - self.border - level_text.get_height() - 5))

        # Schlaf-Overlay (wird nur angezeigt, wenn nicht tot und kein Level-Up)
        if self.pet.sleeping and self.pet.alive and not self.level_up_screen:
            overlay = pygame.Surface((self.width, self.height))
            overlay.set_alpha(140)
            overlay.fill((0, 0, 0))
            self.screen.blit(overlay, (0, 0))
            zzz = self.font.render("Zzz...", True, (255, 255, 255))
            self.screen.blit(zzz, (self.width // 2 - 50, 100))

        # SONDERBILDSCHIRM: LEVEL UP (Überdeckt alles außer das Tot-Menü)
        if self.level_up_screen and self.pet.alive:
            lvl_overlay = pygame.Surface((self.width, self.height))
            lvl_overlay.set_alpha(220)
            lvl_overlay.fill((20, 50, 100)) # Schickes Blau für den Erfolg
            self.screen.blit(lvl_overlay, (0, 0))

            congrats_txt = self.big_font.render("LEVEL UP!", True, (255, 215, 0)) # Goldene Schrift
            info_txt = self.font.render(f"{self.pet.name} is now Level {self.pet.level}!", True, (255, 255, 255))
            dismiss_txt = self.small_font.render("(Click anywhere to continue)", True, (200, 200, 200))

            self.screen.blit(congrats_txt, congrats_txt.get_rect(center=(self.width // 2, self.height // 2 - 80)))
            self.screen.blit(info_txt, info_txt.get_rect(center=(self.width // 2, self.height // 2)))
            self.screen.blit(dismiss_txt, dismiss_txt.get_rect(center=(self.width // 2, self.height // 2 + 100)))

        # TOT-MENÜ OVERLAY (Hat höchste Priorität)
        if not self.pet.alive:
            overlay = pygame.Surface((self.width, self.height))
            overlay.set_alpha(200)
            overlay.fill((50, 10, 10))
            self.screen.blit(overlay, (0, 0))

            dead_text = self.font.render("Your pet died!", True, (255, 50, 50))
            self.screen.blit(dead_text, dead_text.get_rect(center=(self.width // 2, 120)))

            pygame.draw.rect(self.screen, (50, 200, 50), self.revive_rect, border_radius=5)
            pygame.draw.rect(self.screen, (200, 50, 50), self.new_pet_rect, border_radius=5)

            revive_lbl = self.small_font.render("Revive", True, (255, 255, 255))
            new_pet_lbl = self.small_font.render("New Pet", True, (255, 255, 255))

            self.screen.blit(revive_lbl, revive_lbl.get_rect(center=self.revive_rect.center))
            self.screen.blit(new_pet_lbl, new_pet_lbl.get_rect(center=self.new_pet_rect.center))

        pygame.display.flip()

    def run(self):
        while self.running:
            dt = self.clock.tick(60)
            
            # Wenn der Level-Up-Bildschirm aktiv ist, pausieren wir die Timer
            if self.pet.alive and not self.level_up_screen:
                self.tick_timer += dt
                self.level_timer += dt

                # Level Up Logik
                if self.level_timer >= self.level_interval:
                    self.pet.level += 1
                    self.level_timer = 0
                    self.level_up_screen = True # Aktiviert den Sonderbildschirm!
                    self.save_pet()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.handle_buttons(event.pos)

            if self.tick_timer >= self.tick_delay and self.pet.alive and not self.level_up_screen:
                self.pet.tick()
                self.tick_timer = 0
                self.save_pet()

            self.render()

        self.save_pet()
        pygame.quit()