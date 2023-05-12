import pygame, random
from button import *
from assets.fonts.fonts import *
from settings import *
from classes import extras

# Defina as dimensões da board
num_cells_horizontal = 15
num_cells_vertical = 8
# cell_size = 64

# Calcule o tamanho das células com base na resolução da tela
# cell_size = min(SCREEN_WIDTH * 0.70 // num_cells_horizontal, SCREEN_HEIGHT * 0.70 // num_cells_vertical)

cell_width = SCREEN_WIDTH * 0.70 // num_cells_horizontal
cell_height = SCREEN_HEIGHT * 0.70 // num_cells_vertical

# Crie uma matriz para representar a grade da board
grid = []
for row in range(num_cells_vertical):
    # Cada linha representa uma célula
    cell_row = []
    for col in range(num_cells_horizontal):
        # Crie uma célula vazia com as informações necessárias
        cell = {
            'type': 'empty',
            'state': 'normal',
            'content': None
        }
        cell_row.append(cell)
    grid.append(cell_row)

# Exemplo de como acessar uma célula específica na grid
row_index = 2
col_index = 3
cell = grid[row_index][col_index]

# Exemplo de como definir o tipo e o estado de uma célula específica
cell['type'] = 'obstacle'
cell['state'] = 'damaged'

print(grid)
grid[3][4]['type'] = 'obstacle'


# Exemplo de como definir o conteúdo de uma célula específica
content = {
    'name': 'Treasure Chest',
    'loot': ['gold', 'sword']
}
cell['content'] = content


def clean_screen():
    SCREEN.blit(BG, (0, 0))
    SCREEN.blit(BATTLE_BOX_LARGE, (60, 40))
    # draw_dialogue_box(screen=SCREEN, x=110, y=50, width=800,
    #                   text='Welcome to Synthesis. \n \n '
    #                        'Here you can piece together the memories of Cavas to unlock loot and find the Memory Nexus.')


def create_grid():
    grid = []
    for row in range(num_cells_vertical):
        row_cells = []
        for col in range(num_cells_horizontal):
            # Calcule a posição da célula na tela
            cell_x = col * cell_width + 200
            cell_y = row * cell_height + 50
            # Salve as coordenadas da célula na lista
            row_cells.append((cell_x, cell_y))
        grid.append(row_cells)
    return grid


board = []
def roll_board():
    roll = random.randint(3, 4)
    temp_board = create_grid()
    for i in range(0, roll):
        row = random.randint(0, 7)
        column = random.randint(0, 14)
        board.append(temp_board[row][column])


def draw_grid(grid):
    while True:
        SYNTHESIS_MOUSE_POSITION = pygame.mouse.get_pos()
        clean_screen()
        BACK = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(1110, 610),
                      text_input="BACK", font=get_bold_font(30), base_color="White", hovering_color=BLUE)
        SHUFFLE = Button(image=pygame.image.load("assets/images/Smallest Rect.png"), pos=(750, 610),
                      text_input="SHUFFLE", font=get_bold_font(30), base_color="White", hovering_color=BLUE)

        for row in range(num_cells_vertical):
            for col in range(num_cells_horizontal):
                cell_x, cell_y = grid[row][col]
                pygame.draw.rect(SCREEN, (0, 0, 0), (cell_x, cell_y, cell_width, cell_height), 1)
                # Determine a cor do retângulo com base nas coordenadas
                # if (row + col) % 2 == 0:
                #     color = (255, 255, 255)  # Cor para células pares
                # else:
                #     color = (0, 0, 0)  # Cor para células ímpares

                # Renderize a célula como um retângulo
                # pygame.draw.rect(SCREEN, color, (cell_x, cell_y, cell_size, cell_size))


            # SCREEN.blit(FOUR_SIDE_TILE, tile)
        # SCREEN.blit(FOUR_SIDE_TILE, grid[2][2])
        # SCREEN.blit(FOUR_SIDE_TILE, grid[4][4])
        #
        # print(grid[2][2])
        # print(grid[4][4])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK.checkForInput(SYNTHESIS_MOUSE_POSITION):
                    extras.extras()
                if SHUFFLE.checkForInput(SYNTHESIS_MOUSE_POSITION):
                    board.clear()
                    roll_board()
                    # grid = roll_grid()
                    # draw_grid(grid)

        for i in board:
            SCREEN.blit(FOUR_SIDE_TILE, i)
        for button in [BACK, SHUFFLE]:
            button.changeColor(SYNTHESIS_MOUSE_POSITION)
            button.update(SCREEN)
        pygame.display.update()
