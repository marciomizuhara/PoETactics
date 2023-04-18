import pygame
from pygame.math import Vector2

pygame.init()


def get_bold_font(size):
    return pygame.font.Font('assets/fonts/AvenirNextLTPro-DemiCond.otf', size)


def get_regular_font(size):
    return pygame.font.Font('assets/fonts/AvenirNextLTPro-LightCond.otf', size)


def get_italic_font(size):
    return pygame.font.Font('assets/fonts/AvenirNextLTPro-LightCondItalic.otf', size)


def get_quote_font(size):
    return pygame.font.Font('assets/fonts/AvenirNextLTPro-LightCondItalic.otf', size)


dialogue_font = get_regular_font(20)


def wrap_text(dialogue_font, text, width):
    words = text.split()
    lines = []
    current_line = words[0]

    for word in words[1:]:
        if dialogue_font.size(current_line + ' ' + word)[0] < width - 10:
            current_line += ' ' + word
        elif dialogue_font.size(word)[0] > width - 10:
            for i in range(0, len(word), int(len(word) / 2)):
                if dialogue_font.size(current_line + ' ' + word[:i])[0] >= width - 10:
                    break
            else:
                i = len(word)
            lines.append(current_line + ' ' + word[:i])
            current_line = word[i:]
        else:
            lines.append(current_line)
            current_line = word

    lines.append(current_line)
    for i in lines:
        print(len(i))
    return lines

#
#
def draw_dialogue_box(screen, x, y, width, text):
    lines = wrap_text(dialogue_font, text, width)
    height = dialogue_font.size(' ')[1] * len(lines) + 50
    rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, (255, 255, 255), rect)
    pygame.draw.rect(screen, (90, 90, 90), rect, 0)

    for i, line in enumerate(lines):
        text_surface = dialogue_font.render(line, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_pos = Vector2(rect.topleft) + Vector2(10, i * dialogue_font.size(' ')[1] + 10)
        text_rect.topleft = text_pos
        screen.blit(text_surface, text_rect)

    pygame.display.update()