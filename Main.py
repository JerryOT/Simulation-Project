import pygame, sys
import matplotlib.pyplot as plt
import Enums
import Classes
import LevelSet


def main():
   # initializing pygame
    #pygame.mixer.init()
    pygame.init()

    clock = pygame.time.Clock()

    screen_width = 1280
    screen_height = 640
    tick_rate = 60
    slingshot_delay = 10.5
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Angry Bird')

    paused = False
    current_level = LevelSet.Get_Level(1)
    
    while True:
        clock.tick(tick_rate)

        event = pygame.event.poll()

        if (not current_level.slingshot.assigned_bird) and (current_level.cur_time - current_level.slingshot.last_assigned_time) > 30 * slingshot_delay:
            current_level.slingshot.asssign(current_level.Dequeue_Bird(), current_level.cur_time)


        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            paused = not paused
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            pygame.quit()
            sys.exit(0)

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            projectedX, projectedY = event.pos[0], screen_height - event.pos[1]
            obj = current_level.Get_Object_On_Position(projectedX, projectedY)
            if obj:
                if current_level.slingshot.assigned_bird and current_level.slingshot.assigned_bird == obj:
                    current_level.slingshot.set_dragging(True)

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            projectedX, projectedY = event.pos[0], screen_height - event.pos[1]
            if current_level.slingshot.dragging:
                current_level.slingshot.release(projectedX, projectedY)

        if paused:
            continue

        if hasattr(event, "pos"):
            projectedX, projectedY = event.pos[0], screen_height - event.pos[1]
            current_level.slingshot.update(projectedX, projectedY)
        current_level.Step()

        screen.fill((0,0,0))
        current_level.Draw_All(screen, screen_width, screen_height)
        current_level.slingshot.draw(screen, screen_width, screen_height)
        pygame.display.flip()
        pygame.display.update()

if __name__ == '__main__':
    main()