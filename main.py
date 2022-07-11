import pygame
import sys
from desk import Desk
from cube import Figure, NextCubes


def main(background_color: str, second_color: str, cube_colors: list):
    pygame.init()
    clock = pygame.time.Clock()

    game_screen = pygame.display.set_mode((600, 1000))
    stats_rect = pygame.rect.Rect((0, 0), (600, 200))
    score = 0

    desk = Desk()
    figure = Figure(NextCubes(cube_colors))
    cubes = NextCubes(cube_colors)
    cubes_down_event = pygame.USEREVENT + 1
    pygame.time.set_timer(cubes_down_event, 550)

    def change_timer(score_value: int):
        pygame.time.set_timer(cubes_down_event, max(550 - score_value * 50, 100))

    font = pygame.font.SysFont('opensans', 40, True)
    next_cubes_surf = pygame.rect.Rect((150, 15), (175, 175))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == cubes_down_event:
                figure.update(desk, cubes, cube_colors)
                change_timer(score)
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_a:
                        figure.move_left(desk)
                    case pygame.K_d:
                        figure.move_right(desk)
                    case pygame.K_s:
                        figure.move_down(desk)
                    case pygame.K_q:
                        figure.rot_left(desk)
                    case pygame.K_e:
                        figure.rot_right(desk)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            figure.move_down(desk)

        game_screen.fill(background_color)

        score_surf = font.render(f"SCORE: {score}", True, background_color)
        next_surf = font.render(f"NEXT:", True, background_color)

        pygame.draw.rect(game_screen, second_color, stats_rect)
        pygame.draw.rect(game_screen, background_color, next_cubes_surf)

        pygame.draw.rect(game_screen, second_color, next_cubes_surf, 2)
        pygame.draw.rect(game_screen, second_color, next_cubes_surf, 4, 5)

        game_screen.blit(score_surf, score_surf.get_rect(topright=(550, 50)))
        game_screen.blit(next_surf, next_surf.get_rect(topright=(130, 50)))

        figure.draw(game_screen)
        desk.draw(game_screen)
        cubes.draw(game_screen)

        score = desk.check(score)
        desk.update()

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    background_color_1 = 'white'
    background_color_2 = '#666666'
    colors_of_cubes = ['#fff7b3', '#ff7777',
                       '#ffc1b3', '#ffb3f0',
                       '#b8b3ff', '#b3ffc9']
    main(background_color_1,
         background_color_2,
         colors_of_cubes)
#
