import pygame, time
from cs50 import SQL
from playsound import playsound

# Setting database
db = SQL("sqlite:///database.db")

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
WINDOW_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
FPS = 60

# PYGAME CONSTANTS
SCREEN = pygame.display.set_mode(WINDOW_SIZE)


LAST_TIME_MS = int(round(time.time() * 4000))
counter = 0
confirmation_counter = 0

# DROP RATE
GEAR_DROP_RATE = 35
CONSUMABLE_DROP_RATE = 100
TICKET_DROP_RATE = 20
CARD_DROP_RATE = 100
DELVE_DROP_RATE = 100
UNIQUE_DROP_RATE = 100
DROP_HEIGHT = 210

# GAME ICONS
RIGHT_ARROW = pygame.transform.scale(pygame.image.load('assets/images/arrow_2.png'), (120, 90))
SOULS_ICON = pygame.transform.scale(pygame.image.load('assets/images/souls_icon.png'), (40, 40))
SOULS_ICON_COLORED = pygame.transform.scale(pygame.image.load('assets/images/souls_icon_colored.png'), (60, 60))

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
GREEN = pygame.Color('#6bfa1f')


# Images
BG = pygame.image.load('assets/images/main_menu.png')
BATTLE_BOX = pygame.image.load('assets/images/battle_box.png')
BATTLE_BOX_LARGE = pygame.image.load('assets/images/battle_box_large.png')
CARD_EQUIPPED = pygame.image.load('assets/images/ONE_LINE_CARD_BOX.png')
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
CARD = pygame.transform.scale(pygame.image.load('assets/images/card_icon.png'), (60, 60))

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

# SOUL SKILLS
SOUL_REAPER_1 = pygame.transform.scale(pygame.image.load('assets/images/soul_reaper_1.png'), (45, 45))
ONE_WITH_THE_NATURE = pygame.transform.scale(pygame.image.load('assets/images/one_with_the_nature.png'), (45, 45))
ASSASSINATION = pygame.transform.scale(pygame.image.load('assets/images/assassination.png'), (45, 45))

# Cards
SQUIRE = pygame.transform.scale(pygame.image.load('assets/images/characters/cards/squire.png'), (100, 133))
SQUIRE_CARD = pygame.image.load('assets/images/characters/cards/squire_card.png')
SQUIRE_CARD_FRAME = pygame.transform.scale(pygame.image.load('assets/images/characters/cards/squire_frame.png'), (100, 133))
CHEMIST = pygame.transform.scale(pygame.image.load('assets/images/characters/cards/chemist.png'), (100, 133))
CHEMIST_CARD = pygame.image.load('assets/images/characters/cards/chemist_card.png')
CHEMIST_CARD_FRAME = pygame.transform.scale(pygame.image.load('assets/images/characters/cards/chemist_frame.png'), (100, 133))
KNIGHT = pygame.transform.scale(pygame.image.load('assets/images/characters/cards/knight.png'), (100, 133))
KNIGHT_CARD = pygame.image.load('assets/images/characters/cards/knight_card.png')
KNIGHT_CARD_FRAME = pygame.transform.scale(pygame.image.load('assets/images/characters/cards/knight_frame.png'), (100, 133))
ARCHER = pygame.transform.scale(pygame.image.load('assets/images/characters/cards/archer.png'), (100, 133))
ARCHER_CARD = pygame.image.load('assets/images/characters/cards/archer_card.png')
ARCHER_CARD_FRAME = pygame.transform.scale(pygame.image.load('assets/images/characters/cards/archer_frame.png'), (100, 133))
PRIEST = pygame.transform.scale(pygame.image.load('assets/images/characters/cards/priest.png'), (100, 133))
PRIEST_CARD = pygame.image.load('assets/images/characters/cards/priest_card.png')
PRIEST_CARD_FRAME = pygame.transform.scale(pygame.image.load('assets/images/characters/cards/priest_frame.png'), (100, 133))
WIZARD = pygame.transform.scale(pygame.image.load('assets/images/characters/cards/wizard.png'), (100, 133))
WIZARD_CARD = pygame.image.load('assets/images/characters/cards/wizard_card.png')
WIZARD_CARD_FRAME = pygame.transform.scale(pygame.image.load('assets/images/characters/cards/wizard_frame.png'), (100, 133))
MONK = pygame.transform.scale(pygame.image.load('assets/images/characters/cards/monk.png'), (100, 133))
MONK_CARD = pygame.image.load('assets/images/characters/cards/monk_card.png')
MONK_CARD_FRAME = pygame.transform.scale(pygame.image.load('assets/images/characters/cards/monk_frame.png'), (100, 133))
THIEF = pygame.transform.scale(pygame.image.load('assets/images/characters/cards/thief.png'), (100, 133))
THIEF_CARD = pygame.image.load('assets/images/characters/cards/thief_card.png')
THIEF_CARD_FRAME = pygame.transform.scale(pygame.image.load('assets/images/characters/cards/thief_frame.png'), (100, 133))
ORACLE = pygame.transform.scale(pygame.image.load('assets/images/characters/cards/oracle.png'), (100, 133))
ORACLE_CARD = pygame.image.load('assets/images/characters/cards/oracle_card.png')
ORACLE_CARD_FRAME = pygame.transform.scale(pygame.image.load('assets/images/characters/cards/oracle_frame.png'), (100, 133))
TIME_MAGE = pygame.transform.scale(pygame.image.load('assets/images/characters/cards/time_mage.png'), (100, 133))
TIME_MAGE_CARD = pygame.image.load('assets/images/characters/cards/time_mage_card.png')
TIME_MAGE_CARD_FRAME = pygame.transform.scale(pygame.image.load('assets/images/characters/cards/time_mage_frame.png'), (100, 133))
GEOMANCER = pygame.transform.scale(pygame.image.load('assets/images/characters/cards/geomancer.png'), (100, 133))
GEOMANCER_CARD = pygame.image.load('assets/images/characters/cards/geomancer_card.png')
GEOMANCER_CARD_FRAME = pygame.transform.scale(pygame.image.load('assets/images/characters/cards/geomancer_frame.png'), (100, 133))
LANCER = pygame.transform.scale(pygame.image.load('assets/images/characters/cards/lancer.png'), (100, 133))
LANCER_CARD = pygame.image.load('assets/images/characters/cards/lancer_card.png')
LANCER_CARD_FRAME = pygame.transform.scale(pygame.image.load('assets/images/characters/cards/lancer_frame.png'), (100, 133))
MEDIATOR = pygame.transform.scale(pygame.image.load('assets/images/characters/cards/mediator.png'), (100, 133))
MEDIATOR_CARD = pygame.image.load('assets/images/characters/cards/mediator_card.png')
MEDIATOR_CARD_FRAME = pygame.transform.scale(pygame.image.load('assets/images/characters/cards/mediator_frame.png'), (100, 133))
SUMMONER = pygame.transform.scale(pygame.image.load('assets/images/characters/cards/summoner.png'), (100, 133))
SUMMONER_CARD = pygame.image.load('assets/images/characters/cards/summoner_card.png')
SUMMONER_CARD_FRAME = pygame.transform.scale(pygame.image.load('assets/images/characters/cards/summoner_frame.png'), (100, 133))
SAMURAI = pygame.transform.scale(pygame.image.load('assets/images/characters/cards/samurai.png'), (100, 133))
SAMURAI_CARD = pygame.image.load('assets/images/characters/cards/samurai_card.png')
SAMURAI_CARD_FRAME = pygame.transform.scale(pygame.image.load('assets/images/characters/cards/samurai_frame.png'), (100, 133))
NINJA = pygame.transform.scale(pygame.image.load('assets/images/characters/cards/ninja.png'), (100, 133))
NINJA_CARD = pygame.image.load('assets/images/characters/cards/ninja_card.png')
NINJA_CARD_FRAME = pygame.transform.scale(pygame.image.load('assets/images/characters/cards/ninja_frame.png'), (100, 133))
CALCULATOR = pygame.transform.scale(pygame.image.load('assets/images/characters/cards/calculator.png'), (100, 133))
CALCULATOR_CARD = pygame.image.load('assets/images/characters/cards/calculator_card.png')
CALCULATOR_CARD_FRAME = pygame.transform.scale(pygame.image.load('assets/images/characters/cards/calculator_frame.png'), (100, 133))
BARD_DANCER = pygame.transform.scale(pygame.image.load('assets/images/characters/cards/bard_dancer.png'), (100, 133))
BARD_DANCER_CARD = pygame.image.load('assets/images/characters/cards/bard_dancer_card.png')
BARD_DANCER_CARD_FRAME = pygame.transform.scale(pygame.image.load('assets/images/characters/cards/bard_dancer_frame.png'), (100, 133))


CARD_LIST = [SQUIRE_CARD, CHEMIST_CARD]
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
CARD_CHANGE = 'assets/music/card_change.mp3'
ESSENCE_ENCOUNTER = 'assets/music/essence_encounter.mp3'


