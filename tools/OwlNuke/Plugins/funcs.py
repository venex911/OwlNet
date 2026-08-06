from colorama import init
from pystyle import Colorate, Colors, Center, Col, Add, Anime

from Plugins.logger import Logger
from Plugins.colors import Palette



palette = Palette()



class Funcs:
    
    @staticmethod
    def get_input(text: str, checker = True):
        
        
        
        text = f"{palette.red}{text}{palette.better_grassy_green}"

        v = input(text)
        if not checker(v):
            while not checker(v):
                Logger.Error.error("Try Again")
                v = input(text)
        
        return v
    
    @staticmethod
    def print_logo():
        logo = """
________         .__    _______         __        ____   ________ 
\_____  \__  _  _|  |   \      \  __ __|  | __ ___\   \ /   /_   |
 /   |   \ \/ \/ /  |   /   |   \|  |  \  |/ // __ \   Y   / |   |
/    |    \     /|  |__/    |    \  |  /    <\  ___/\     /  |   |
\_______  /\/\_/ |____/\____|__  /____/|__|_ \\___  >\___/   |___|
        \/                     \/           \/    \/              
"""


        print(Colorate.Vertical(Colors.DynamicMIX((Col.red, Col.dark_red)), logo))