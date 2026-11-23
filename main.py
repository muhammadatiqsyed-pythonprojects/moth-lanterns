import asyncio

import pygame

import settings


async def main():
    # -------------------------------------SETUP-------------------------------
    pygame.init()
    screen = pygame.display.set_mode(
        (settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT),
        pygame.SCALED | pygame.RESIZABLE,
    )
    pygame.display.set_caption("MOTH AND LANTERNS")
    clock = pygame.time.Clock()

    # variables
    # loop variable
    running = True

    # game states menu, ready, playing, paused, gameover
    game_state = "menu"

    # game loop
    while running:
        dt = clock.tick(settings.FPS)
        # -------------------------------INPUT---------------------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # ------------------------------UPDATE---------------------------------
        # ------------------------------DRAW-----------------------------------
        screen.fill(settings.SCREEN_COLOR)

        pygame.display.flip()
        await asyncio.sleep(0)
    # ------------------------------EXIT-----------------------------------
    pygame.quit()


if __name__ == "__main__":
    asyncio.run(main())
