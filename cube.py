import pygame
import numpy as np
from random import choice


class Figure(pygame.sprite.Group):
    def __init__(self, cubes):
        super().__init__()
        self.helper_y = None
        self.helper_x = None
        self.empty()
        self.add(*cubes)
        self.pos = 1

    def draw(self, screen):
        for cube in self:
            cube.draw(screen, color='green')

    def move_left(self, desk):
        cubes = [Cube(cube.x, cube.y) for cube in self]
        for moved_cube in cubes:
            moved_cube.x -= 50
            if pygame.sprite.spritecollideany(moved_cube, desk) or moved_cube.x < 0:
                return
        self.empty()
        self.add(*cubes)

    def move_right(self, desk):
        cubes = [Cube(cube.x, cube.y) for cube in self]
        for moved_cube in cubes:
            moved_cube.x += 50
            if pygame.sprite.spritecollideany(moved_cube, desk) or moved_cube.x > 550:
                return
        self.empty()
        self.add(*cubes)

    @property
    def helper(self):
        cubes_x = np.array([cube.x // 50 for cube in self])
        cubes_y = np.array([cube.y // 50 for cube in self])
        self.helper_x = min(cubes_x)
        self.helper_y = min(cubes_y)
        cubes_x -= self.helper_x
        cubes_y -= self.helper_y
        res = np.zeros((len(cubes_x), len(cubes_y)))
        res[cubes_y, cubes_x] = 1
        return res

    def rot_left(self, desk):
        self.pos = (self.pos + 1) % 2
        all_y, all_x = np.nonzero(np.rot90(self.helper, 1))
        new_cubes = []
        for x, y in zip(all_x, all_y):
            cube = Cube((self.helper_x + x) * 50, (self.helper_y + y - 1 - self.pos) * 50)
            if pygame.sprite.spritecollideany(cube,
                                              desk) or cube.y >= 1000 or cube.rect.right > 600 or cube.rect.left < 0:
                return
            new_cubes.append(cube)

        self.empty()
        self.add(*new_cubes)

    def rot_right(self, desk):
        for i in range(3):
            self.rot_left(desk)

    def update(self, desk, cubes):
        for cube in self:
            cube.y += 50
        if any(cube.y == 1000 for cube in self) or pygame.sprite.groupcollide(desk, self, False, False):
            for cube in self:
                cube.y -= 50
                desk.add(cube)
            self.empty()
            self.__init__(cubes)
            cubes.__init__()


class Cube(pygame.sprite.Sprite):
    def __init__(self, x, y, width=50, height=50):
        super().__init__()
        self.x, self.y = x, y
        self.width, self.height = width, height

    def draw(self, screen, color='green'):
        pygame.draw.rect(screen, pygame.Color(color), (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, 'black', self.rect, 5)
        pygame.draw.rect(screen, 'white', self.rect, 1)

    @property
    def rect(self):
        return pygame.rect.Rect(self.x, self.y, self.width, self.height)


class NextCubes(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        coords = {(200, 200)}
        while len(coords) < 4:
            base = choice(list(coords))
            if choice([0, 1]):
                new_coords = (base[0] + 50, base[1])
            else:
                new_coords = (base[0], base[1] + 50)
            coords.add(new_coords)
        cubes = [Cube(x, y) for x, y in coords]
        self.add(*cubes)

    def draw(self, screen):
        for cube in self:
            rect = (cube.x, cube.y - 175, 50, 50)
            rect = list(i * 4 / 5 for i in rect)
            pygame.draw.rect(screen, pygame.Color('yellow'), rect)
            pygame.draw.rect(screen, 'black', rect, 5)
            pygame.draw.rect(screen, 'white', rect, 1)
