import pygame
import sys
from desk import Desk
from cube import Figure, NextCubes


def main():
    pygame.init()
    clock = pygame.time.Clock()

    game_screen = pygame.display.set_mode((600, 1000))
    stats_rect = pygame.rect.Rect((0, 0), (600, 200))
    score = 0

    desk = Desk()
    all_cubes = Figure(NextCubes())
    cubes = NextCubes()
    cubes_down_event = pygame.USEREVENT + 1
    pygame.time.set_timer(cubes_down_event, 850)

    def change_timer(score_value):
        pygame.time.set_timer(cubes_down_event, max(750 - score_value * 50, 100))

    font = pygame.font.SysFont('opensans', 40, True)
    next_cubes_surf = pygame.rect.Rect((150, 15), (175, 175))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == cubes_down_event:
                all_cubes.update(desk, cubes)
                change_timer(score)
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_a:
                        all_cubes.move_left(desk)
                    case pygame.K_d:
                        all_cubes.move_right(desk)
                    case pygame.K_s:
                        all_cubes.update(desk, cubes)
                    case pygame.K_q | pygame.K_SPACE:
                        all_cubes.rot_left(desk)
                    case pygame.K_e:
                        all_cubes.rot_right(desk)
        game_screen.fill('white')

        score_surf = font.render(f"SCORE: {score}", True, 'White')
        next_surf = font.render(f"NEXT:", True, 'White')

        pygame.draw.rect(game_screen, "#3c3f41", stats_rect)
        pygame.draw.rect(game_screen, 'white', next_cubes_surf)

        pygame.draw.rect(game_screen, '#3c3f41', next_cubes_surf, 2)
        pygame.draw.rect(game_screen, 'black', next_cubes_surf, 4, 5)

        game_screen.blit(score_surf, score_surf.get_rect(topright=(550, 50)))
        game_screen.blit(next_surf, next_surf.get_rect(topright=(130, 50)))

        all_cubes.draw(game_screen)
        desk.draw(game_screen)
        cubes.draw(game_screen)

        score = desk.check(score)
        desk.update()

        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()
