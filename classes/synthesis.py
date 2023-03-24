import pygame

# Define as cores que serão usadas no jogo
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define as dimensões da tela do jogo
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Inicializa o Pygame
pygame.init()

# Define a fonte que será usada para exibir o texto na tela
font = pygame.font.SysFont('Arial', 30)

# Cria a janela do jogo
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Mecânica de síntese')

# Cria a matriz de síntese
synthesis_grid = [[None, None, None], [None, None, None], [None, None, None]]

# Define os itens base
sword_item = {'name': 'Espada', 'image': pygame.image.load('../assets/images/deft_fossil.png')}
shield_item = {'name': 'Escudo', 'image': pygame.image.load('../assets/images/dense_fossil.png')}
potion_item = {'name': 'Poção', 'image': pygame.image.load('../assets/images/pristine_fossil.png')}

# Define as posições dos itens base na tela
sword_position = (100, 100)
shield_position = (300, 100)
potion_position = (500, 100)

# Define a energia disponível do jogador
energy = 10

# Define a posição da energia na tela
energy_position = (SCREEN_WIDTH - 100, 50)

# Define a posição da mensagem na tela
message_position = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)


# Função que desenha um item na tela
def draw_item(item, position):
    screen.blit(item['image'], position)


# Função que desenha a matriz de síntese na tela
def draw_synthesis_grid():
    for row_index, row in enumerate(synthesis_grid):
        for column_index, column in enumerate(row):
            if column is not None:
                item_position = (50 + column_index * 100, 200 + row_index * 100)
                draw_item(column, item_position)
            pygame.draw.rect(screen, BLACK, (50 + column_index * 100, 200 + row_index * 100, 150, 150), 2)



# Função que verifica se a matriz de síntese contém um padrão específico e retorna o resultado da síntese
def perform_synthesis():
    # Verifica se a matriz de síntese contém uma espada, um escudo e uma poção em uma linha horizontal
    if synthesis_grid[1][0] == sword_item and synthesis_grid[1][1] == shield_item and synthesis_grid[1][2] == potion_item:
        return {'name': 'Nova arma', 'image': pygame.image.load('new_weapon.png')}
    # Verifica se a matriz de síntese contém um escudo, uma poção e uma espada em uma linha horizontal
    elif synthesis_grid[1][0] == shield_item and synthesis_grid[1][1] == potion_item and synthesis_grid[1][2] == sword_item:
        return {'name': 'Novo escudo', 'image': pygame.image.load('new_shield.png')}
    # Retorna None se a matriz de síntese não contém um padrão válido
    else:
        return None


# Loop principal do jogo
running = True
while running:
    # Limpa a tela
    screen.fill(WHITE)

    # Desenha os itens
    draw_synthesis_grid()
    draw_item(sword_item, sword_position)
    # perform_synthesis()


    pygame.display.update()