#Это скрипт для начала игры
from Scripts_utilites_for_game.LoadingFuncBRO import run_loading_bar

import subprocess
import sys
import time
class StartGame():
    def __init__(self):
        self.isInstalled = False
        self.isInstalled_mass = []
        with open('requirements.txt', 'r', encoding='utf-8') as file:
            content = file.read()

        self.mass_content = content.split()
        print("===ИДЕТ ПРОВЕРКА НА СКАЧИВАНИЕ БИБЛИОТЕК===\n")
        time.sleep(1)

    def check_for_libs(self, libs):
        try:
            __import__ (libs)
            isInstalled = True
            self.isInstalled_mass.append(str(isInstalled))
            time.sleep(1)
            return "Библиотека установлена: " + libs
        except ModuleNotFoundError:
            isInstalled = False
            self.isInstalled_mass.append(str(isInstalled))
            time.sleep(1)
            return"Библиотека не найдена: " + libs

    def check_access(self):
        if "False" in self.isInstalled_mass:
            return "непрошли"
        else:
            print("\n===УСПЕШНО===\nНачинаем загрузку в игру...\n")
            return "прошли"

    def print_result(self):
        for i in self.mass_content:
            print(self.check_for_libs(i))
        print("\n╔" + ("═"*23) + "╗")
        print(f"║Библиотек скачано: {self.isInstalled_mass.count(str("True"))}   ║")
        print(f"║Библиотек не скачано: {self.isInstalled_mass.count(str("False"))}║")
        print("╚" + ("═"*23) + "╝")
        time.sleep(1)

    def Launch_Game(self):
        self.print_result()
        finally_access = self.check_access()
        
        if finally_access == "прошли":
            run_loading_bar()
            from Scripts_utilites_for_game.init_game import start_games
            start_games()
            
        if finally_access == "непрошли":
            print("ВЫ чмо, поэтому скачиваем\n")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame"])
            from Scripts_utilites_for_game.init_game import start_games
            start_games()
start = StartGame()
start.Launch_Game()
