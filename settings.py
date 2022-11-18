import pygame
from playsound import playsound

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
WINDOW_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
FPS = 60

#colors
DARK_GREY = pygame.Color("#2B2D2F")
WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)
PINK = pygame.Color('#FF0084')
BLUE = pygame.Color('#0096FF')
RED = pygame.Color('#FF0000')
ORANGE = pygame.Color('#FF6600')
YELLOW = pygame.Color('#FFE800')
CYAN = pygame.Color('#4ADEDE')

# Images
BG = pygame.image.load('assets/images/main_menu.png')
BATTLE_BOX = pygame.image.load('assets/images/battle_box.png')
BATTLE_BOX_LARGE = pygame.image.load('assets/images/battle_box_large.png')
PLAYER_STATUS_BOX = pygame.image.load('assets/images/PLAYER_STATUS_BOX.png')
PLAYER = pygame.image.load('assets/images/characters/ramza.png')
PLAYER_STATUS = pygame.transform.scale(pygame.image.load('assets/images/characters/ramza2.png'), (152, 320))
BLACK_LIFE_BAR = pygame.image.load('assets/images/BLACK_LIFE_BAR.png')
RED_LIFE_BAR = pygame.image.load('assets/images/RED_ONE_LINE_OPTION.png')
CONSUMABLES_GRID = pygame.image.load('assets/images/consumables_grid.png')
CONSUMABLES_ONE_LINE_BOX = pygame.image.load('assets/images/CONSUMABLE_ONE_LINE_BOX.png')
DELVE_MAIN_BG = pygame.image.load('assets/images/delve_main_menu.png')
FROZEN_HOLLOW = pygame.image.load('assets/images/frozen_hollow.png')
FUNGAL_CAVERNS = pygame.image.load('assets/images/fungal_caverns.png')
PETRIFIED_FOREST = pygame.image.load('assets/images/petrified_forest.png')
ABYSSAL_DEPTHS = pygame.image.load('assets/images/abyssal_depths.png')
MAGMA_FISSURE = pygame.image.load('assets/images/magma_fissure.png')
SULPHUR_VENTS = pygame.image.load('assets/images/sulphur_vents.png')
ROULETTE_WHEEL = pygame.image.load('assets/images/roulette_wheel.png')
ROULETTE_WHEEL2 = pygame.image.load('assets/images/roulette_wheel2.png')
ROULETTE_WHEEL2_ARROW = pygame.transform.scale(pygame.image.load('assets/images/arrow.png'), (40, 67))

# Icons
ICON_FRAME = pygame.transform.scale(pygame.image.load('assets/images/cards.png'), (100, 100))
POTION = pygame.transform.scale(pygame.image.load('assets/images/potion.png'), (40, 60))
HI_POTION = pygame.transform.scale(pygame.image.load('assets/images/hi_potion.png'), (40, 60))
X_POTION = pygame.transform.scale(pygame.image.load('assets/images/x_potion.png'), (40, 60))
ELIXIR = pygame.transform.scale(pygame.image.load('assets/images/elixir.png'), (40, 60))
CHAOS_ORB = pygame.transform.scale(pygame.image.load('assets/images/chaos_orb.png'), (55, 55))
DIVINE_ORB = pygame.transform.scale(pygame.image.load('assets/images/divine_orb.png'), (55, 55))
EXALTED_ORB = pygame.transform.scale(pygame.image.load('assets/images/exalted_orb.png'), (55, 55))
MIRROR_OF_KALANDRA = pygame.transform.scale(pygame.image.load('assets/images/mirror_of_kalandra.png'), (60, 60))
DENSE_FOSSIL = pygame.transform.scale(pygame.image.load('assets/images/dense_fossil.png'), (60, 60))
SERRATED_FOSSIL = pygame.transform.scale(pygame.image.load('assets/images/serrated_fossil.png'), (60, 60))
PRISTINE_FOSSIL = pygame.transform.scale(pygame.image.load('assets/images/pristine_fossil.png'), (60, 60))
DEFT_FOSSIL = pygame.transform.scale(pygame.image.load('assets/images/deft_fossil.png'), (60, 60))
FRACTURED_FOSSIL = pygame.transform.scale(pygame.image.load('assets/images/fractured_fossil.png'), (60, 60))
ROULETTE_WHEEL2_TICKET = pygame.transform.scale(pygame.image.load('assets/images/roulette_wheel_ticket.png'), (60, 60))
CARDS = pygame.transform.scale(pygame.image.load('assets/images/cards.png'), (60, 60))

WEAPON = pygame.transform.scale(pygame.image.load('assets/images/weapon.png'), (60, 60))
HELMET = pygame.transform.scale(pygame.image.load('assets/images/helmet.png'), (60, 60))
ARMOR = pygame.transform.scale(pygame.image.load('assets/images/armor.png'), (60, 60))
SHIELD = pygame.transform.scale(pygame.image.load('assets/images/shield.png'), (60, 60))
LEGS = pygame.transform.scale(pygame.image.load('assets/images/legs.png'), (60, 60))
GLOVES = pygame.transform.scale(pygame.image.load('assets/images/gloves.png'), (60, 60))
BOOTS = pygame.transform.scale(pygame.image.load('assets/images/boots.png'), (60, 60))
RING = pygame.transform.scale(pygame.image.load('assets/images/ring.png'), (60, 60))
AMULET = pygame.transform.scale(pygame.image.load('assets/images/amulet.png'), (40, 60))

G_ROULETTE_WHEEL2_TICKET = pygame.transform.scale(pygame.image.load('assets/images/g_roulette_wheel_ticket.png'), (60, 60))
G_POTION = pygame.transform.scale(pygame.image.load('assets/images/g_potion.png'), (40, 60))
G_HI_POTION = pygame.transform.scale(pygame.image.load('assets/images/g_hi_potion.png'), (40, 60))
G_X_POTION = pygame.transform.scale(pygame.image.load('assets/images/g_x_potion.png'), (40, 60))
G_ELIXIR = pygame.transform.scale(pygame.image.load('assets/images/g_elixir.png'), (40, 60))
G_CHAOS_ORB = pygame.transform.scale(pygame.image.load('assets/images/g_chaos_orb.png'), (55, 55))
G_DIVINE_ORB = pygame.transform.scale(pygame.image.load('assets/images/g_divine_orb.png'), (55, 55))
G_EXALTED_ORB = pygame.transform.scale(pygame.image.load('assets/images/g_exalted_orb.png'), (55, 55))
G_MIRROR_OF_KALANDRA = pygame.transform.scale(pygame.image.load('assets/images/g_mirror_of_kalandra.png'), (60, 60))
G_DENSE_FOSSIL = pygame.transform.scale(pygame.image.load('assets/images/g_dense_fossil.png'), (60, 60))
G_SERRATED_FOSSIL = pygame.transform.scale(pygame.image.load('assets/images/g_serrated_fossil.png'), (60, 60))
G_PRISTINE_FOSSIL = pygame.transform.scale(pygame.image.load('assets/images/g_pristine_fossil.png'), (60, 60))
G_DEFT_FOSSIL = pygame.transform.scale(pygame.image.load('assets/images/g_deft_fossil.png'), (60, 60))
G_FRACTURED_FOSSIL = pygame.transform.scale(pygame.image.load('assets/images/g_fractured_fossil.png'), (60, 60))

# Cards
SQUIRE_CARD = pygame.image.load('assets/images/characters/cards/squire.png')
SQUIRE_CARD_FRAME = pygame.transform.scale(pygame.image.load('assets/images/characters/cards/squire_frame.png'), (100, 133))

DASH = 160
BACKGROUND_SONG = 'assets/music/opening_song.mp3'
BOSS_FIGHT_SONG = 'assets/music/boss_fight.wav'
GAME_OVER = 'assets/music/game_over.wav'
PLAYER_LEVEL_UP = 'assets/music/player_level_up3.wav'
MIRROR = 'assets/music/mirror_of_kalandra.mp3'
DROP_1 = 'assets/music/drop1.wav'
DROP_CONSUMABLE = 'assets/music/consumable.mp3'
PLAYER_ATTACK = 'assets/music/slash2.wav'
ENEMY_ATTACK = 'assets/music/slash1.wav'
CRITICAL_ATTACK = 'assets/music/criticalhit.wav'
DELVE = 'assets/music/delve.mp3'



