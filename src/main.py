from pygame import Surface, Color, K_SPACE
import pygame

from rendering import Circle

fps        = 10000
resolution = width, height = 1000, 1000
clock      = pygame.time.Clock()
surface    = pygame.display.set_mode(resolution)

circle = Circle((width / 2, height / 2), 100)
circleThick = Circle((width / 2, height / 2), 200, 5)
circleThick2 = Circle((width / 2, height / 2), 150, 10)

color = Color(255, 255, 255)

while True:
    [exit() for event in pygame.event.get() if event.type == pygame.QUIT]
    clock.tick(fps)
    
    if pygame.key.get_pressed()[K_SPACE]: 
        pygame.display.set_caption(f"Circle Drawing: PAUSED")
        continue

    surface.fill(Color(0, 0, 0))

    pygame.display.set_caption(f"Circle Drawing. { clock.get_fps() // 1 } FPS")
    
    circle.render(surface, color)
    circleThick.render(surface, color)
    circleThick2.render(surface, color)

    pygame.display.flip()