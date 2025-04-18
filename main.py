import pygame
import sys
from entities.ghost import Ghost
from entities.player import Player
from system.camera import Camera
from constants import *
from system.map import Map
from textures.base_floor import BaseFloor
import random

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('RPG Game')

    tick = 0
    clock = pygame.time.Clock()
    running = True

    number_of_ghosts = 4
    ghosts = []
    for i in range(number_of_ghosts):
        x = random.randint(0, MAX_MAP_WIDTH - 64)
        y = random.randint(0, MAX_MAP_HEIGHT - 64)
        ghosts.append(Ghost(x, y, PIXEL_SIZE, tick, GRID_SIZE))
    
    player = Player(32, 32, PIXEL_SIZE, tick, GRID_SIZE)

    camera = Camera(SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE)

    base_floor = BaseFloor()
    base_map = Map(MAX_MAP_WIDTH, MAX_MAP_HEIGHT, PIXEL_SIZE, base_floor)

    while running:

        clock.tick(FPS)
        if tick >= FPS:
            tick = 0
        else:
            tick += 1
        
        
        player.tick = tick
        
        screen.fill(COLORS['black'])

        base_map.draw(screen, camera)
        
        keys = pygame.key.get_pressed()
        player.move(keys)

        for ghost in ghosts:
            ghost.tick = tick  
            ghost.move()
            ghost_pos = camera.world_coords_to_screen_coords(ghost)
        camera.follow_target(player)

        player_pos = camera.world_coords_to_screen_coords(player)

        for ghost in ghosts:
            draw_entity(screen, ghost, ghost_pos, COLORS)
        
        draw_entity(screen, player, player_pos, COLORS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()  


def draw_entity(screen, entity, position, colors):
    model = entity.models[0] if entity.tick < 12 else entity.models[1]
    draw_x, draw_y = position

    for y, row in enumerate(model):
        for x, pixel in enumerate(row):
            if pixel == 'W':
                color = colors['white']
            elif pixel == 'B':
                color = colors['black']
            elif pixel == 'R':
                color = colors['red']
            elif pixel == 'G':
                color = colors['grey']
            elif pixel == 'D':
                color = colors['darkgrey']
            else:
                continue

            pygame.draw.rect(screen, color, 
                ((draw_x + x) * entity.pixel_size, 
                 (draw_y + y) * entity.pixel_size, 
                 entity.pixel_size, entity.pixel_size))

if __name__ == '__main__':
    main()
