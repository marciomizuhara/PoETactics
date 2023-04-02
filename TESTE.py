import pygame
import pygame.gfxdraw
from pygame.locals import *
from pygame.color import THECOLORS
from settings import *

pygame.init()

# Configuração da tela
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Brilho do ícone')
clock = pygame.time.Clock()

# Definindo as cores
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# Configuração do ícone
icon_rect = pygame.Rect(100, 100, 50, 50)
icon_color = WHITE

# Configuração do Tween
start_color = WHITE
end_color = CYAN
tween_duration = 500  # 1 segundo
tween_start_time = None


# Função para o Tween
def interpolate_color(start_color, end_color, progress):
    r = int(start_color[0] + (end_color[0] - start_color[0]) * progress)
    g = int(start_color[1] + (end_color[1] - start_color[1]) * progress)
    b = int(start_color[2] + (end_color[2] - start_color[2]) * progress)
    return (r, g, b)


# Loop principal
running = True
while running:
    # Tratamento de eventos
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            running = False

        # Evento que ativa o Tween
        if event.type == KEYDOWN and event.key == K_SPACE:
            icon_color = YELLOW
            tween_start_time = pygame.time.get_ticks()

    # Atualização da cor do ícone com o Tween
    if tween_start_time is not None:
        time_since_tween_start = pygame.time.get_ticks() - tween_start_time
        if time_since_tween_start < tween_duration:
            progress = time_since_tween_start / tween_duration
            icon_color = interpolate_color(start_color, end_color, progress)
        else:
            icon_color = WHITE
            tween_start_time = None

    # Desenho na tela
    screen.fill(THECOLORS['black'])
    pygame.gfxdraw.box(screen, icon_rect, icon_color)
    pygame.display.flip()

    # Espera o tempo necessário para atingir o FPS desejado
    clock.tick(60)

pygame.quit()
