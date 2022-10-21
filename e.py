import pygame
pygame.init()
fps = 60
fps_clock = pygame.time.Clock()
screen = pygame.display.set_mode((500, 500))

while True:
    pygame.draw.rect(3,3,3)
    screen.blit()


    pygame.display.flip()
    fps_clock.tick(fps)