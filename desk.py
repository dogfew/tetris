import pygame


class Desk(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

    def draw(self, screen):
        for cube in self:
            cube.draw(screen, color='red')

    def check(self, score):
        for cube_1 in self:
            bottom = cube_1.rect.bottom
            print(bottom)
            if bottom == 250:
                self.empty()
                return 0
            good_cubes = [cube_2 for cube_2 in self if cube_2.rect.bottom == bottom]
            if len(good_cubes) >= 12:
                score += 1
                self.remove(*good_cubes)
                for cube in self:
                    if cube.rect.bottom <= bottom:
                        cube.y += 50
        return score
