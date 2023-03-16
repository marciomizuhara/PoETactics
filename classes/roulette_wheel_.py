import pygame, sys, random, math

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


click_blocking = True

ROULETTE_WHEEL_LIST = [0, 26, 3, 35, 12, 28, 7, 29, 18, 22, 9, 31, 14, 20, 1, 33, 16, 24, 5, 10, 23, 8, 30, 11, 36, 13,
                       27, 6, 34, 17, 25, 2, 21, 4, 19, 15, 32]

ROULETTE_WHEEL_LIST2 = [19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]


def roulette():
    global counter, LAST_TIME_MS, click_blocking

    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(BATTLE_BOX_LARGE, (60, 40))
    SCREEN.blit(PLAYER_STATUS_BOX, (80, 60))

    # Definir fonte
    font = pygame.font.SysFont(None, 30)

    # Definir variáveis
    numeros = [str(i) for i in range(0, 37)]
    cores = ["vermelho", "preto"]
    resultado = None
    selecao = None
    aposta = 0

    # Loop principal do jogo
    running = True
    while running:

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # Limpar a tela
        SCREEN.fill(WHITE)

        # Desenhar a roleta
        pygame.draw.circle(SCREEN, BLUE, (int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2)), 150, 0)
        pygame.draw.circle(SCREEN, BLACK, (int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2)), 148, 0)

        # Desenhar os números na roleta
        for i in range(0, 37):
            if i % 2 == 0:
                cor = RED
            else:
                cor = BLACK
            angulo = (2 * i * 3.1416) / 37
            x = int(SCREEN_WIDTH / 2 + 135 * math.sin(angulo))
            y = int(SCREEN_HEIGHT / 2 + 135 * math.cos(angulo))
            numero = font.render(numeros[i], True, cor)
            SCREEN.blit(numero, (x - 10, y - 10))

        # Desenhar os botões de seleção
        for i in range(0, 2):
            if selecao == i:
                cor = BLUE
            else:
                cor = WHITE
            pygame.draw.rect(SCREEN, cor, (i * SCREEN_WIDTH / 2 + 20, 300, SCREEN_WIDTH / 2 - 40, 50), 0)
            cor_texto = BLACK
            texto = font.render(cores[i], True, cor_texto)
            SCREEN.blit(texto, (i * SCREEN_WIDTH / 2 + SCREEN_WIDTH / 4 - 35, 310))

        # Desenhar o botão de aposta
        pygame.draw.rect(SCREEN, WHITE, (20, 360, SCREEN_WIDTH - 40, 30), 0)
        cor_texto = BLACK
        texto = font.render("Apostar: " + str(aposta), True, cor_texto)
        SCREEN.blit(texto, (50, 365))

        # # Sortear um número aleatório
        # if resultado is None:
        #     resultado = random.choice(numeros)
        #     if resultado in ["0", "00"]:
        #         cor_resultado = BLUE
        #     elif int(resultado) % 2 == 0:
        #         cor_resultado = RED
        #     else:
        #         cor_resultado = BLACK
        #     resultado_texto = font.render(resultado, True)