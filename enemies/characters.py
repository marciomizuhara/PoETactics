from main import *
from settings import *
import pygame

# def __init__(self, name, life, attack, defense, level, xp, crit_chance, status, quote1, quote2, quote3):

# --------------------------------------------------------------------------------------------------------------
# wiegraf1 = Character('Wiegraf', 1500, 120, 30, 5, 150, 50)
# --------------------------------------------------------------------------------------------------------------


characters = {
    'Wiegraf 1': {'name': 'Wiegraf',
                  'life': 1000,
                  'attack': 180,
                  'defense': 40,
                  'level': 5,
                  'xp': 150,
                  'crit_chance': 40,
                  'status': True,
                  'quote1': "You'll never know the feeling of the 'Meager'.",
                  'quote2': "You may think you know it, but you've never lived it!",
                  'quote3': "Behold my full power!",
                  'quote4': "AAAAARRGH... THIS CANNOT BE TRUE... ",
                  'image': 'assets/images/characters/wiegraf1.png'

                  },

    'Dycedarg 1': {'name': 'Dycedarg',
                   'life': 1800,
                   'attack': 300,
                   'defense': 65,
                   'level': 10,
                   'xp': 400,
                   'crit_chance': 40,
                   'status': True,
                   'quote1': "Is it not I? I, who have dirtied my hands to keep yours clean?",
                   'quote2': "All that you are you owe to me! You ought be on your knees thanking me,",
                   'quote3': "yet here you stand in judgment!",
                   'quote4': 'AAAAAAAAAARRRRRGHHHH!',
                   'image': 'assets/images/characters/dycedarg1.png'
                   },

    'Wiegraf 2': {'name': 'Wiegraf, Corpse Brigade Head',
                  'life': 2600,
                  'attack': 400,
                  'defense': 100,
                  'level': 15,
                  'xp': 1000,
                  'crit_chance': 40,
                  'status': True,
                  'quote1': f"And then we meet again...",
                  'quote2': "I guess you wasn't expecting this unforeseen turn of events!",
                  'quote3': "You'll regreat crossing my path a second time!",
                  'quote4': "AAAARRRRRRRRRGHH!",
                  'image': 'assets/images/characters/wiegraf2.png'
                  },

    'Dycedarg 2': {'name': 'Dycedarg, the Betrayer God',
                   'life': 4500,
                   'attack': 550,
                   'defense': 120,
                   'level': 20,
                   'xp': 0,
                   'crit_chance': 40,
                   'status': True,
                   'quote1': "Come! I will show you that common blood",
                   'quote2': "makes naught but a common man!",
                   'quote3': "Face the revenge of the Fallen God!",
                   'quote4': 'AAAAAAAAAAARGH, MY BELOVED REALM OF IVALICE...',
                   'image': 'assets/images/characters/dycedarg2.png'}
}
