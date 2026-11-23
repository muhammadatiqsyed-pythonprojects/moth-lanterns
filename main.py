import asyncio

import pygame

# GAME CONSTANTS
WINDOW_WIDTH = 480
WINDOW_HEIGHT = 800
FPS = 60
SCREEN_COLOR = "white"


async def main():
    # -------------------------------------SETUP-------------------------------
    pygame.init()
    screen = pygame.display.set_mode(
        (WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SCALED | pygame.RESIZABLE
    )
    pygame.display.set_caption("MOTH AND LANTERNS")
    clock = pygame.time.Clock()

    # variables
    # loop variable
    running = True

    # game loop
    while running:
        dt = clock.tick(FPS)
        # -------------------------------INPUT---------------------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # ------------------------------UPDATE---------------------------------
        # ------------------------------DRAW-----------------------------------
        screen.fill(SCREEN_COLOR)

        pygame.display.flip()
        await asyncio.sleep(0)
    # ------------------------------EXIT-----------------------------------
    pygame.quit()


if __name__ == "__main__":
    asyncio.run(main())
