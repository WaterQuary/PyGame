import pygame as pg
from main import Game
pg.init()

class GameMenu():
    def __init__(self):
        self.chooses = ["Играть)", "Не играть("]
        self.current_choose = 0
        self.keys = [pg.K_UP, pg.K_DOWN, pg.K_RETURN]

    def logic_logic(self, key):
        if key == self.keys[0]:
            self.current_choose = 0
        elif key == self.keys[1]:
            self.current_choose = 1

        elif key == self.keys[2]:
            if self.current_choose == 0:
                result = "игра"
            elif self.current_choose == 1:
                result = "выход"
            print(result)
            return result
        return None

class Screen():
    def __init__(self, game_menu):
        self.width = 800
        self.height  = 600
        self.game_menu = game_menu
        self.play_screen = pg.display.set_mode((self.width, self.height))
        self.play_clock = pg.time.Clock()
        pg.display.set_caption("Главное меню")
        self.background_color = (30,30,40)
        self.font = pg.font.SysFont(None, 36)

    def print_menu(self):
        greeting = self.font.render(f"Главное меню", True, (255, 255, 255))
        greeting_rect = greeting.get_rect( center = (self.width // 2, 220))
        self.play_screen.blit(greeting, greeting_rect)
        for i in range(len(self.game_menu.chooses)):
            text = self.game_menu.chooses[i]
            if i == self.game_menu.current_choose:
                text ="< " + text
                color = (255, 255, 0)
            else:
                color = (255, 255, 255)
            menu_item = self.font.render(text, True, color)
            pos_y = 300 + i * 40
            self.play_screen.blit(menu_item, (300, pos_y))

class Show():
    def __init__(self):
        self.gameMenu = GameMenu()
        self.screen = Screen(self.gameMenu)
        self.isGame = False
        self.run = True

    def show_in_game(self):
        while self.run:
            self.screen.play_clock.tick(60)
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    self.run = False
                if e.type == pg.KEYDOWN:
                    key = e.key
                    test = self.gameMenu.logic_logic(key)
                    if test == "игра":
                        print("игра жеско")
                        self.isGame = True
                    elif test == "выход":
                        self.run = False
            self.screen.play_screen.fill(self.screen.background_color)
            if self.isGame:
                Game().start_game()
                return
            else:
                self.screen.print_menu()
            pg.display.flip()

start = Show()
start.show_in_game()
pg.quit()