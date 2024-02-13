import pygame 
import random
import os

pygame.mixer.init()
pygame.init()

white = (255, 255, 255)
red  = (255, 0, 0)
black = (0, 0, 0)
green = (30, 132, 73)
purple = (126,87,194)
screen_width = 950
screen_height = 600

gameWindow = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("ssss🐍💀")
pygame.display.update()

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow,color,snake_list,snake_size):
        for x,y in snake_list:
            pygame.draw.rect(gameWindow,color,[x,y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(black)
        bgimg = pygame.image.load('/Users/sarang/Desktop/desktop/coding/python/python.py/pygames/welcome.png')
        bgimg = pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()
        gameWindow.blit(bgimg,(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()

        pygame.display.update()
        clock.tick(60)

def gameloop():
    exit_game = False
    game_over = False
    snake_x = 80
    snake_y = 150
    snake_size = 10 
    fps = 60
    velocityx = 0
    velocityy = 0
    foodx = random.randint(130, screen_width/2)
    foody = random.randint(130, screen_height/2)
    food_size = 8
    score = 0
    init_velocity = 3
    snake_list = []
    snake_length = 1
    
    if (not os.path.exists("/Users/sarang/Desktop/desktop/coding/python/python.py/pygames/highscore.txt")):
        with open("/Users/sarang/Desktop/desktop/coding/python/python.py/pygames/highscore.txt","w") as f:
            f.write("0")

    with open ("/Users/sarang/Desktop/desktop/coding/python/python.py/pygames/highscore.txt","r") as f:
        highscore = f.read()

    while not exit_game:
        if game_over:
            with open ("/Users/sarang/Desktop/desktop/coding/python/python.py/pygames/highscore.txt","w") as f:
                f.write(str(highscore))

            gameWindow.fill(black)
            bgimg = pygame.image.load('/Users/sarang/Desktop/desktop/coding/python/python.py/pygames/gameover.png')
            bgimg = pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()
            gameWindow.blit(bgimg,(0,0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocityx = init_velocity
                        velocityy = 0
                    
                    if event.key == pygame.K_LEFT:
                        velocityx = -init_velocity
                        velocityy = 0
                    
                    if event.key == pygame.K_UP:
                        velocityy = -init_velocity
                        velocityx = 0
                    
                    if event.key == pygame.K_DOWN:
                        velocityy = init_velocity
                        velocityx = 0
                    
                    if event.key == pygame.K_q:
                        score += 5

            snake_x = snake_x +velocityx
            snake_y = snake_y +velocityy        
            if abs(snake_x - foodx) <6 and abs (snake_y - foody)<6:
                score += 10
                foodx = random.randint(130, screen_width/2)
                foody = random.randint(130, screen_height/2)
                snake_length += 5
                pygame.mixer.music.load('/Users/sarang/Desktop/desktop/coding/python/python.py/pygames/beep.mp3')
                pygame.mixer.music.play()
                if score > int(highscore):
                    highscore = score

            gameWindow.fill(black)
            bgimg = pygame.image.load('/Users/sarang/Desktop/desktop/coding/python/python.py/pygames/snake_bg.png')
            bgimg = pygame.transform.scale(bgimg,(screen_width,screen_height)).convert_alpha()
            gameWindow.blit(bgimg,(0,0))

            text_screen("Score:",white,20,15)
            text_screen(str(score),red,140,18)
            text_screen("Highscore:",white,260,15)
            text_screen(str(highscore),red,460,18)

            pygame.draw.rect(gameWindow,red,[foodx, foody, food_size, food_size])
            
            head= []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]
            
            if head in snake_list[:-1]:
                game_over = True
                pygame.mixer.music.load('/Users/sarang/Desktop/desktop/coding/python/python.py/pygames/gameover.mp3')
                pygame.mixer.music.play()


            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load('/Users/sarang/Desktop/desktop/coding/python/python.py/pygames/gameover.mp3')
                pygame.mixer.music.play()

            plot_snake(gameWindow,green,snake_list, snake_size)
        pygame.display.update()
        clock.tick(fps)
        

    pygame.quit()
    quit()

welcome()