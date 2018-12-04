import math
import pygame as pg
from pygame.math import Vector2


pg.init()
screen = pg.display.set_mode((640, 480))
FONT = pg.font.Font(None, 24)
BLACK = pg.Color('black')
BG_COLOR = pg.Color('darkseagreen4')


class Bullet(pg.sprite.Sprite):

    def __init__(self, pos, angle):
        super(Bullet, self).__init__()
        self.image = pg.Surface((20, 11), pg.SRCALPHA)
        pg.draw.rect(self.image, pg.Color('grey11'), [0, 0, 13, 11])
        pg.draw.polygon(
            self.image, pg.Color('grey11'), [(13, 0), (20, 5), (13, 10)])
        self.image = pg.transform.rotate(self.image, -angle)
        self.rect = self.image.get_rect(center=pos)
        # To apply an offset to the start position,
        # create another vector and rotate it as well.
        offset = Vector2(80, 0).rotate(angle)
        #print(offset)
        # Use the offset to change the starting position.
        self.pos = Vector2(pos) + offset
        self.velocity = Vector2(5, 0)
        self.velocity.rotate_ip(angle)

    def update(self):
        self.pos += self.velocity
        #print(self.pos)
        self.rect.center = self.pos
        print(self.rect.center)
        print(self.pos)


def main():
    clock = pg.time.Clock()
    # The cannon image and rect.
    surf = pg.Surface((40, 22), pg.SRCALPHA)
    print(surf)
    surf.fill(pg.Color('grey27'))
    pg.draw.rect(surf, pg.Color('grey11'), [30, 6, 10, 10])
    orig_surf = surf
    rect = surf.get_rect(center=(320, 240))
    print(rect)
    angle = 0  # Angle of the cannon.
    # Add bullets to this group.
    bullet_group = pg.sprite.Group()

    playing = True
    while playing:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                playing = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left button fires bullet.
                    # Fire a bullet from cannon center with current angle.
                    bullet_group.add(Bullet(rect.center, angle))

        bullet_group.update()
        # Find angle to target (mouse pos).
        x, y = Vector2(pg.mouse.get_pos()) - rect.center
        angle = math.degrees(math.atan2(y, x))
        # Rotate the cannon image.
        surf = pg.transform.rotate(orig_surf, -angle)
        rect = surf.get_rect(center=rect.center)

        # Draw
        screen.fill(BG_COLOR)
        bullet_group.draw(screen)
        
        screen.blit(surf, rect)
        txt = FONT.render('angle {:.1f}'.format(angle), True, BLACK)
        screen.blit(txt, (10, 10))
        pg.draw.line(screen, pg.Color(150, 60, 20), rect.center, pg.mouse.get_pos(), 2)
        pg.display.update()

        clock.tick(30)

if __name__ == '__main__':
    main()
    pg.quit()