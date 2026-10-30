"""ИГРА БРО"""

import pygame as pg
import random
pg.init()
pg.mixer.init()

class Player():
    def __init__(self, target):
        self.isUp = self.isDown = self.isLeft = False
        self.isRight = True
        self.player_speed = 2.5
        self.radius = 40
        self.player_image = pg.image.load("pictures/MainHero.png").convert_alpha()
        self.rect = self.player_image.get_rect()
        self.score = 0
        self.rect.center = (400, 300)
        self.target = target
        self.click_sound = pg.mixer.Sound("audio/ReachTarget2.mp3")
        self.click_sound.set_volume(0.5)
        self.image = self.player_image.copy()

    def directions(self, dir):
        if dir == pg.K_UP:
            self.isUp = self.isDown = self.isRight = self.isLeft = False
            self.isUp = True
        if dir == pg.K_DOWN:
            self.isUp = self.isDown = self.isRight = self.isLeft = False
            self.isDown = True
        if dir == pg.K_RIGHT:
            self.isUp = self.isDown = self.isRight = self.isLeft = False
            self.isRight = True
        if dir == pg.K_LEFT:
            self.isUp = self.isDown = self.isRight = self.isLeft = False
            self.isLeft = True
    def move(self):
        x, y = self.rect.center
        if self.isUp == True: y -= self.player_speed
        if self.isDown == True: y += self.player_speed
        if self.isRight == True: x += self.player_speed
        if self.isLeft == True: x -= self.player_speed

        if y < -30:
            y = 625
        if y > 630:
            y = -25
        if x < -30:
            x = 825
        if x > 830:
            x = -25

        self.rect.center = (x, y)

        distance_x = self.rect.centerx - self.target.targett_x
        distance_y = self.rect.centery - self.target.targett_y

        distance = (distance_x**2 + distance_y**2)**0.5

        if distance < (self.radius + self.target.radius_target):
            self.reach_target()

    def spawn_player(self, screen):
        screen.blit(self.image, self.rect)
    def change_radius(self):
        old_center = self.rect.center
        new_size = (self.radius * 2, self.radius * 2)
        self.image = pg.transform.scale(self.player_image, new_size)
        
        self.rect = self.image.get_rect()
        self.rect.center = old_center

    def reach_target(self):
        self.target.respawn()
        self.score += 1
        self.click_sound.stop()
        self.click_sound.play()
        print(f"Очки: {self.score}")
        self.radius += 2
        self.change_radius()
        
class Target():
    def __init__(self):
        self.radius_target = 40
        self.targett_x, self.targett_y = self.random()
        self.target_image = pg.image.load("pictures/Target.png").convert_alpha()
        self.rect_target = self.target_image.get_rect()
    def random(self):
        target_y = random.randint(40, 560)
        target_x = random.randint(40, 760)
        return target_x, target_y
    
    def respawn(self):
        self.targett_x, self.targett_y = self.random()

    def spawn(self, screen):
        self.rect_target.center = (self.targett_x, self.targett_y)
        screen.blit(self.target_image, self.rect_target)

class Screen():
    def __init__(self):
        self.width = 800
        self.height  = 600
        self.play_screen = pg.display.set_mode((self.width, self.height))
        self.play_clock = pg.time.Clock()
        pg.display.set_caption("Первая игра")
        self.background_color = (30,30,40)
        self.font = pg.font.SysFont(None, 36)

    def print_score(self, score):
        score_surf = self.font.render(f'Счет: {score}', True, (255, 255, 255))
        self.play_screen.blit(score_surf, (10, 10))

class Game():
    def __init__(self):
        self.game_screen = Screen()
        self.game_target = Target()
        self.game_player = Player(self.game_target)
        self.audio = "audio/BackGround.mp3"
    
        self.run = True

    def start_game(self):
        self.background_music()
        while self.run:
            self.game()

    def background_music(self):
        pg.mixer.music.load(self.audio)
        pg.mixer.music.play(loops=-1)
        pg.mixer.music.set_volume(0.1)
    def game(self):
        self.game_screen.play_clock.tick(90)
        for e in pg.event.get():
            if e.type == pg.QUIT:
                self.run = False
            if e.type == pg.KEYDOWN:
                dir = e.key
                self.game_player.directions(dir)
        self.game_screen.play_screen.fill(self.game_screen.background_color)
        self.game_player.move()
        self.game_player.spawn_player(self.game_screen.play_screen)
        self.game_target.spawn(self.game_screen.play_screen)
        self.game_screen.print_score(self.game_player.score)
        
        pg.display.flip()
pg.quit()