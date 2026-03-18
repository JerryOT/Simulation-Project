import pygame, sys
import matplotlib.pyplot as plt
import Component__UI


def main():

   # initializing pygame
    #pygame.mixer.init()
    pygame.init()
    clock = pygame.time.Clock()

    screen_width = 640
    screen_height = 640
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Rigid')

    paused = False

    while True:
        clock.tick(60)
        screen.fill(Component__UI.Get_Colors()['BLACK'])

        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            paused = not paused
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            pygame.quit()
            sys.exit(0)
        else:
            pass
        if paused:
            continue


        #TEST CASE
        Box_A = Component__UI.Box(Component__UI.Get_Colors()['RED'], 40, 40)
        Box_A.Set_Position(0,0)
        Box_A.Set_Rotation(20)
        Box_A.Draw(screen, screen_width, screen_height)

        Circle_A = Component__UI.Circle(Component__UI.Get_Colors()['RED'], 20)
        Circle_A.Set_Position(80,0)
        Circle_A.Draw(screen, screen_width, screen_height)
        

        pygame.display.flip()
        pygame.display.update()


if __name__ == '__main__':
    main()