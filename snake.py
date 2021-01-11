import pygame
import random
import os
pygame.init()
pygame.mixer.init()

# Colors
white = (255,255,255)   
red =   (255,0,0)
black= (0,0,0)
steelblue=(70,130,180)
violet=(238,130,238)
orange=(255,165,0)
gray = (128,128,128)
crimson=(220,20,60)
teal=(0,128,128)
lime = (0,255,0)
# Creating window
screen_width = 600
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

#background image:
bgimg1 = pygame.image.load("snake1.jpg")
bgimg1 = pygame.transform.scale(bgimg1,(screen_width,screen_height)).convert_alpha()
bgimg2 = pygame.image.load("ab.jpg")
bgimg2 = pygame.transform.scale(bgimg2,(screen_width,screen_height)).convert_alpha() 
bgimg3= pygame.image.load("c.jpg")
bgimg3 = pygame.transform.scale(bgimg3,(screen_width,screen_height)).convert_alpha()
# Game Title
pygame.display.set_caption("Snakes With ABHAY")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 40)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])


def plot_snake(gameWindow, color, snake_list, snake_size):
    print(snake_list)
    for x,y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    pygame.mixer.music.load('NCSC.mp3')
    pygame.mixer.music.play()
    while not exit_game:
        gameWindow.blit(bgimg1,(0,0))
        text_screen("      Welcome To The Game",orange,10,20)
        text_screen("<< PRESS SPACE TO PLAY >>",black,10,70)
       


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('NCSD.mp3')
                    pygame.mixer.music.play()

                    gameloop()                
        pygame.display.update()
        clock.tick(90)        

def gameloop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 80
    velocity_x = 0
    velocity_y = 0
    snake_list = []
    snake_length = 1
    
    if(not os.path.exists("HIGHSCORE.txt")):
        with open("HIGHSCORE.txt","w") as f: 
            f.write("0")                     
    with open("HIGHSCORE.txt", "r") as f:
        HIGHSCORE = f.read()                  
    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    init_velocity = 5
    snake_size = 10
    fps = 90
    while not exit_game:
        if game_over:
            with open("HIGHSCORE.txt", "w") as f:
                f.write(str(HIGHSCORE))

            
            gameWindow.blit(bgimg3,(0,0))
            text_screen("                  Game Over!",red,5, 150)
            text_screen("          Press ENTER to continue",black,5, 200)

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
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_q:        
                        score +=5

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<8 and abs(snake_y - food_y)<8:
                score +=10
                food_x = random.randint(5, screen_width -20)
                food_y = random.randint(80, screen_height-20)
                snake_length +=2
                if score>int(HIGHSCORE):
                    HIGHSCORE = score
            
            
            gameWindow.blit(bgimg2,(0,0))
            text_screen("Score: " + str(score) + "  HIGHSCORE: "+str(HIGHSCORE),lime, 5, 5)
            text_screen("press arrow kews to play",orange,5,35)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list)>snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True
                pygame.mixer.music.load('explosion.mp3')
                pygame.mixer.music.play()


            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load('explosion.mp3')
                pygame.mixer.music.play()

            plot_snake(gameWindow, black, snake_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()