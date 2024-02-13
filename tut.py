import pygame 
x = pygame.init() #intialises all the modules in pygame

#creating a display
gameWindow = pygame.display.set_mode((1200,500)) #we loop this for the window to stay open
pygame.display.set_caption("my first game") #title of the game

#game specific variables
exit_game = False
game_over = False

#creating game loop (so the window doesn't close)
while not exit_game:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("you have pressed right arrow key")

pygame.quit()
quit()
