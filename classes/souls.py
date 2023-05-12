import pygame, sys, random, math
from settings import *
from assets.fonts.fonts import *
from assets.music.music import *
from button import *
from settings import *
from classes import consumable_item_
from classes import drop
from classes import extras
from classes import inventory
from classes import player_
from classes import save_load
from items.uniques import *
from classes import unique


current_soul = []


class SoulSkill:
    def __init__(self, image, name, description, level, unlock_cost, locked=True):
        self.image = image
        self.name = name
        self.description = description
        self.level = level
        self.unlock_cost = unlock_cost
        self.locked = locked

    def unlock(self):
        self.locked = False

    def lock(self):
        self.locked = True


soul_reaper_1 = SoulSkill(SOUL_REAPER_1, "Soul Reaper 1", "+100% to soul gain", 1, 100)
one_with_the_nature = SoulSkill(ONE_WITH_THE_NATURE, "One with the Nature", "+10% to total life", 2, 250)
assassination = SoulSkill(ASSASSINATION, "Assassination", "+10% to attack", 3, 270)
soul_of_steel = SoulSkill(SOUL_OF_STEEL, "Soul of Steel", "+10% to defense", 3, 270)
merciless_blow = SoulSkill(MERCILESS_BLOW, "Merciless Blow", "+20% to critical damage", 3, 500)
deadly_precision = SoulSkill(DEADLY_PRECISION, "Deadly Precision", "+10 to critical chance", 3, 500)

soul_skills_list = [soul_reaper_1, one_with_the_nature, assassination, soul_of_steel, merciless_blow]

# Verificar se uma soul skill está desbloqueada
# if not soul_skill1.locked:
#     # Realizar ação relacionada à soul skill
#     print("Soul Skill Fireball unlocked!")

buff_granted = {
    'Assassination': 0,
}


def activate_soul(soul_skill, attribute, attribute_value, percentage):
    buff_granted[soul_skill.name] = attribute_value * percentage
    print('activation, atual', attribute_value)
    print('activation, buff granted', buff_granted[soul_skill.name])
    if attribute == 'attack':
        player_.player.attack += buff_granted[soul_skill.name]
    print('activation, depois ', player_.player.attack)


def disable_soul(soul_skill, attribute, attribute_value):
    print('disable, atual', attribute_value)
    if attribute == 'attack':
        player_.player.attack -= buff_granted[soul_skill.name]
    print('disable,depois ', player_.player.attack)


def show_confirmation_message(soul_image, soul_name, locked_status):
    if locked_status:
        locked = 'Disabled!'
        color = RED
    else:
        locked = 'Activated!'
        color = GREEN
    locked_text = get_bold_font(30).render(locked, True, color)
    soul_image_resized = pygame.transform.scale(soul_image, (150, 150))
    soul_text = get_bold_font(45).render(soul_name, True, WHITE)
    text_rect = soul_text.get_rect()
    text_rect.center = (1020, 250)
    image_rect = soul_image_resized.get_rect()
    image_rect.center = (1020, 135)
    locked_text_rect = locked_text.get_rect()
    locked_text_rect.center = (1020, 300)
    SCREEN.blit(soul_image_resized, image_rect)
    SCREEN.blit(soul_text, text_rect)
    SCREEN.blit(locked_text, locked_text_rect)
    # pygame.display.update()




def draw_souls_icon():
    SCREEN.blit(SOULS_ICON, (1020, 633))


def draw_souls_quantity():
    souls_text = get_regular_font(25).render(f" {player_.player.souls}", True, WHITE)
    souls_rect = souls_text.get_rect(midleft=(1065, 653))
    SCREEN.blit(souls_text, souls_rect)


def gain_souls(number):
    player_.player.souls += number


def update_souls(soul_skill, operation):
    print(f"entrou {soul_skill.name}, custo: {soul_skill.unlock_cost}, operação: {operation} ")
    if operation == 'add':
        player_.player.souls += soul_skill.unlock_cost
    else:
        player_.player.souls -= soul_skill.unlock_cost


def clean_screen():
    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(BATTLE_BOX_LARGE, (60, 40))
    draw_dialogue_box(screen=SCREEN, x=110, y=70, width=700,
                      text='Welcome to the Soul Pantheon. \n \n '
                           'Here you can exchange your souls points to unlock powerful perks and skills.')
    souls_text = get_bold_font(35).render(f" {player_.player.souls}", True, WHITE)
    deviation = pygame.Surface((700,60))
    deviation.fill(RED)
    deviation_rect = deviation.get_rect()
    deviation_rect.left = 110
    deviation_rect.top = 200
    souls_text_rect = souls_text.get_rect(center=(750, 220))
    souls_text_rect.right = deviation_rect.right - 70

    SCREEN.blit(SOULS_ICON, (souls_text_rect.left - 50 ,200))
    SCREEN.blit(souls_text, souls_text_rect)
    # SCREEN.blit(deviation, deviation_rect)


def souls_menu():
    global counter, LAST_TIME_MS, confirmation_counter
    # clean_screen()
    toggle_confirmation = False
    screen = 1
    soul_buttons = []
    while True:
        HELP_MOUSE_POSITION = pygame.mouse.get_pos()
        clean_screen()
        RETURN = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(1110, 610),
                        text_input="BACK", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        BACK = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(190, 610),
                      text_input="<<", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        NEXT = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(730, 610),
                      text_input=">>", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        if screen == 1:
            SOUL_SKILL_1 = SoulBox(image=pygame.image.load("assets/images/SOUL_SKILLS_BOX.png"), pos=(460, 300),
                                   skill=soul_reaper_1.name, description=soul_reaper_1.description, soul_cost=str(soul_reaper_1.unlock_cost),
                                   soul_icon=pygame.transform.scale(SOUL_REAPER_1, (45, 45)),
                                   skill_font=get_bold_font(20),
                                   description_font=get_regular_font(20), soul_cost_font=get_bold_font(25),
                                   sphere=soul_reaper_1.locked,
                                   base_color='White', hovering_color=BLUE)

            SOUL_SKILL_2 = SoulBox(image=pygame.image.load("assets/images/SOUL_SKILLS_BOX.png"), pos=(460, 360),
                                   soul_icon=pygame.transform.scale(ONE_WITH_THE_NATURE, (45,45)),
                                   skill=one_with_the_nature.name, description=one_with_the_nature.description,
                                   soul_cost=str(one_with_the_nature.unlock_cost),
                                   skill_font=get_bold_font(20),
                                   description_font=get_regular_font(20), soul_cost_font=get_bold_font(25),
                                   sphere=one_with_the_nature.locked,
                                   base_color='White', hovering_color=BLUE)

            SOUL_SKILL_3 = SoulBox(image=pygame.image.load("assets/images/SOUL_SKILLS_BOX.png"), pos=(460, 420),
                                   soul_icon=pygame.transform.scale(ASSASSINATION, (45,45)),
                                   skill=assassination.name,
                                   description=assassination.description, soul_cost=str(assassination.unlock_cost),
                                   skill_font=get_bold_font(20),
                                   description_font=get_regular_font(20), soul_cost_font=get_bold_font(25),
                                   sphere=assassination.locked,
                                   base_color='White', hovering_color=BLUE)

            SOUL_SKILL_4 = SoulBox(image=pygame.image.load("assets/images/SOUL_SKILLS_BOX.png"), pos=(460, 480),
                                   soul_icon=pygame.transform.scale(SOUL_OF_STEEL, (45,45)),
                                   skill=soul_of_steel.name,
                                   description=soul_of_steel.description, soul_cost=str(soul_of_steel.unlock_cost),
                                   skill_font=get_bold_font(20),
                                   description_font=get_regular_font(20), soul_cost_font=get_bold_font(25),
                                   sphere=soul_of_steel.locked,
                                   base_color='White', hovering_color=BLUE)


            soul_buttons.clear()
            soul_buttons.extend([SOUL_SKILL_1, SOUL_SKILL_2, SOUL_SKILL_3, SOUL_SKILL_4])

        if screen == 2:
            SOUL_SKILL_5 = SoulBox(image=pygame.image.load("assets/images/SOUL_SKILLS_BOX.png"), pos=(460, 300),
                                   soul_icon=pygame.transform.scale(MERCILESS_BLOW, (45, 45)),
                                   skill=merciless_blow.name,
                                   description=merciless_blow.description, soul_cost=str(merciless_blow.unlock_cost),
                                   skill_font=get_bold_font(20),
                                   description_font=get_regular_font(20), soul_cost_font=get_bold_font(25),
                                   sphere=merciless_blow.locked,
                                   base_color='White', hovering_color=BLUE)
            SOUL_SKILL_6 = SoulBox(image=pygame.image.load("assets/images/SOUL_SKILLS_BOX.png"), pos=(460, 360),
                                   skill=deadly_precision.name, description=deadly_precision.description, soul_cost=str(deadly_precision.unlock_cost),
                                   soul_icon=pygame.transform.scale(DEADLY_PRECISION, (45, 45)),
                                   skill_font=get_bold_font(20),
                                   description_font=get_regular_font(20), soul_cost_font=get_bold_font(25),
                                   sphere=deadly_precision.locked,
                                   base_color='White', hovering_color=BLUE)
            soul_buttons.clear()
            soul_buttons.extend([SOUL_SKILL_5, SOUL_SKILL_6])

        diff_time_ms = int(round(time.time() * 4000)) - LAST_TIME_MS

        if diff_time_ms >= 4000:
            counter += 1
            confirmation_counter += 1
            LAST_TIME_MS = int(round(time.time() * 4000))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RETURN.checkForInput(HELP_MOUSE_POSITION):
                    counter = 0
                    extras.extras()
                if BACK.checkForInput(HELP_MOUSE_POSITION):
                    clean_screen()
                    if screen == 2:
                        screen = 1
                if NEXT.checkForInput(HELP_MOUSE_POSITION):
                    clean_screen()
                    if screen == 1:
                        screen = 2
                # if SOUL_SKILL_1.checkForInput(HELP_MOUSE_POSITION):
                #     confirmation_counter =0
                #     toggle_confirmation = True

                for button in soul_buttons:
                    if button.checkForInput(HELP_MOUSE_POSITION):
                        soul_skill_name = button.skill
                        if soul_skill_name == soul_reaper_1.name and soul_reaper_1.locked:
                            if soul_reaper_1.unlock_cost <= player_.player.souls:
                                update_souls(soul_reaper_1, 'remove')
                                soul_reaper_1.locked = False
                                current_soul.append(soul_reaper_1)
                                confirmation_counter = 0
                                toggle_confirmation = True
                        elif soul_skill_name == soul_reaper_1.name and not soul_reaper_1.locked:
                            update_souls(soul_reaper_1, 'add')
                            soul_reaper_1.locked = True
                            current_soul.append(soul_reaper_1)
                            confirmation_counter = 0
                            toggle_confirmation = True
                        elif soul_skill_name == one_with_the_nature.name and one_with_the_nature.locked:
                            if one_with_the_nature.unlock_cost <= player_.player.souls:
                                update_souls(one_with_the_nature, 'remove')
                                one_with_the_nature.locked = False
                                current_soul.append(one_with_the_nature)
                                confirmation_counter = 0
                                toggle_confirmation = True
                        elif soul_skill_name == one_with_the_nature.name and not one_with_the_nature.locked:
                            update_souls(one_with_the_nature, 'add')
                            one_with_the_nature.locked = True
                            current_soul.append(one_with_the_nature)
                            confirmation_counter = 0
                            toggle_confirmation = True
                        elif soul_skill_name == assassination.name and assassination.locked:
                            if assassination.unlock_cost <= player_.player.souls:
                                update_souls(assassination, 'remove')
                                activate_soul(assassination, 'attack', player_.player.attack, 0.1)
                                assassination.locked = False
                                current_soul.append(assassination)
                                confirmation_counter = 0
                                toggle_confirmation = True
                        elif soul_skill_name == assassination.name and not assassination.locked:
                            update_souls(assassination, 'add')
                            disable_soul(assassination, 'attack', player_.player.attack)
                            assassination.locked = True
                            current_soul.append(assassination)
                            confirmation_counter = 0
                            toggle_confirmation = True
                        elif soul_skill_name == soul_of_steel.name and soul_of_steel.locked:
                            if soul_of_steel.unlock_cost <= player_.player.souls:
                                update_souls(soul_of_steel, 'remove')
                                soul_of_steel.locked = False
                                current_soul.append(soul_of_steel)
                                confirmation_counter = 0
                                toggle_confirmation = True
                        elif soul_skill_name == soul_of_steel.name and not soul_of_steel.locked:
                            update_souls(soul_of_steel, 'add')
                            soul_of_steel.locked = True
                            current_soul.append(soul_of_steel)
                            confirmation_counter = 0
                            toggle_confirmation = True
                        elif soul_skill_name == merciless_blow.name and merciless_blow.locked:
                            if merciless_blow.unlock_cost <= player_.player.souls:
                                update_souls(merciless_blow, 'remove')
                                merciless_blow.locked = False
                                current_soul.append(merciless_blow)
                                confirmation_counter = 0
                                toggle_confirmation = True
                        elif soul_skill_name == merciless_blow.name and not merciless_blow.locked:
                            update_souls(merciless_blow, 'add')
                            merciless_blow.locked = True
                            current_soul.append(merciless_blow)
                            confirmation_counter = 0
                            toggle_confirmation = True
                        elif soul_skill_name == deadly_precision.name and deadly_precision.locked:
                            if deadly_precision.unlock_cost <= player_.player.souls:
                                update_souls(deadly_precision, 'remove')
                                deadly_precision.locked = False
                                current_soul.append(deadly_precision)
                                confirmation_counter = 0
                                toggle_confirmation = True
                        elif soul_skill_name == deadly_precision.name and not deadly_precision.locked:
                            update_souls(deadly_precision, 'add')
                            deadly_precision.locked = True
                            current_soul.append(deadly_precision)
                            confirmation_counter = 0
                            toggle_confirmation = True

        if toggle_confirmation and confirmation_counter >= 0:
            show_confirmation_message(current_soul[-1].image,
                                      current_soul[-1].name,
                                      current_soul[-1].locked)
        if confirmation_counter == 3 and toggle_confirmation:
            confirmation_counter = 0
            current_soul.clear()
            toggle_confirmation = False
            # clean_screen()

        for button in [RETURN, BACK, NEXT]:
            button.changeColor(HELP_MOUSE_POSITION)
            button.update(SCREEN)
        for button in soul_buttons:
                button.changeColor(HELP_MOUSE_POSITION)
                button.update(SCREEN)
        pygame.display.update()


def roulette_outcome(index):
    global counter, LAST_TIME_MS, click_blocking

    reward = ''
    setter = True
    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(BATTLE_BOX_LARGE, (60, 40))
    # SCREEN.blit(pygame.transform.rotate(ROULETTE_WHEEL2, angle), (position))
    print(type(index))
    print(index)
    if index == 19:
        consumable_item_.mirror_of_kalandra.quantity += 1
        reward = 'Mirror of Kalandra'
    if index == 18:
        consumable_item_.exalted_orb.quantity += 1
        reward = 'Exalted Orb'
    if index == 17:
        consumable_item_.elixir.quantity += 1
        reward = 'Elixir'
    if index == 16:
        consumable_item_.divine_orb.quantity += 1
        reward = 'Divine Orb'
    if index == 15:
        consumable_item_.elixir.quantity += 1
        reward = 'Elixir'
    if index == 14:
        consumable_item_.deft_fossil.quantity += 1
        reward = 'Deft Fossil'
    if index == 13:
        consumable_item_.elixir.quantity += 1
        reward = 'Elixir'
    if index == 12:
        consumable_item_.pristine_fossil.quantity += 1
        reward = 'Pristine Fossil'
    if index == 11:
        consumable_item_.elixir.quantity += 1
        reward = 'Elixir'
    if index == 10:
        consumable_item_.chaos_orb.quantity += 1
        reward = 'Chaos Orb'
    if index == 9:
        consumable_item_.elixir.quantity += 1
        reward = 'Elixir'
    if index == 8:
        consumable_item_.serrated_fossil.quantity += 1
        reward = 'Serrated Fossil'
    if index == 7:
        consumable_item_.elixir.quantity += 1
        reward = 'Elixir'
    if index == 6:
        consumable_item_.divine_orb.quantity += 1
        reward = 'Divine Orb'
    if index == 5:
        consumable_item_.elixir.quantity += 1
        reward = 'Elixir'
    if index == 4:
        consumable_item_.dense_fossil.quantity += 1
        reward = 'Dense Fossil'
    if index == 3:
        consumable_item_.elixir.quantity += 1
        reward = 'Elixir'
    if index == 2:
        consumable_item_.chaos_orb.quantity += 1
        reward = 'Chaos Orb'
    if index == 1:
        new_drop = random.choice(uniques)
        inventory_uniques = [value for elem in inventory.inventory for value in elem.__dict__.values()]
        print(new_drop)
        print(inventory_uniques)
        input('aqui')
        if new_drop['name'] in inventory_uniques:
            if new_drop['name'] in unique.uniques_list:
                consumable_item_.elixir.quantity += 1
                reward = 'Elixir'
            else:
                consumable_item_.elixir.quantity += 1
                reward = 'Elixir'
        else:
            unique.uniques_list.append(new_drop['name'])
            reward = new_drop['name']
            new_item = unique.Unique(new_drop['type'],
                              new_drop['name'],
                              new_drop['level'],
                              new_drop['life'],
                              new_drop['attack'],
                              new_drop['defense'],
                              new_drop['crit_chance'],
                              new_drop['crit_damage'],
                              new_drop['magic_find'],
                              new_drop['rarity'],
                              new_drop['image'],
                              )
            inventory.inventory.append(new_item)
            db.execute("INSERT INTO uniques_list (username, name) VALUES (:username, :name)",
                       username=player_.player.name, name=new_drop['name'])
            inventory.inventory_update(player_.player.name, new_item)
            new_drop.temp_unique_new_drop.append(new_item)

    save_load.save_state()

    outcome = get_bold_font(40).render(f"You received 1x {reward}!", True, YELLOW)
    outcome_rect = outcome.get_rect(center=(SCREEN_WIDTH / 2, 260))

    while True:
        ROULETTE_OUTCOME_MOUSE_POSITION = pygame.mouse.get_pos()
        # BUTTONS = main_menu_structure(PLAYER_STATUS_MOUSE_POSITION)

        CONTINUE = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(SCREEN_WIDTH / 2, 360),
                          text_input="CONTINUE", font=get_bold_font(30), base_color="White", hovering_color=BLUE)

        # NO_BUTTON = Button(image=pygame.image.load("images/Smallest Rect.png"), pos=(380, 600),
        #                      text_input="NO", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        # YES_BUTTON = Button(image=pygame.image.load("images/Smallest Rect.png"), pos=(540, 600),
        #                     text_input="YES", font=get_bold_font(30), base_color="White", hovering_color=BLUE)

        diff_time_ms = int(round(time.time() * 4000)) - LAST_TIME_MS

        if diff_time_ms >= 4000:
            counter = counter + 1
            LAST_TIME_MS = int(round(time.time() * 4000))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CONTINUE.checkForInput(ROULETTE_OUTCOME_MOUSE_POSITION):
                    counter = 0
                    click_blocking = True
                    roulette()

        if counter >= 0:
            if setter:
                consumable_drop_sound()
                SCREEN.blit(outcome, outcome_rect)
                setter = False
        if counter >= 2:
            for button in [CONTINUE]:
                button.changeColor(ROULETTE_OUTCOME_MOUSE_POSITION)
                button.update(SCREEN)
        pygame.display.update()


