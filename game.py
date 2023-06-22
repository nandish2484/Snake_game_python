import pygame
import random
import os

pygame.init()

# colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0,100,0)
brown = (150,75,0)

# creating window
screen_width = 900
screen_height = 600
gamewindow = pygame.display.set_mode((screen_width, screen_height))

#Background Imagedsssddddwds
bgimg = pygame.image.load("snake.png")
endimg = pygame.image.load("end.png")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()
endimg = pygame.transform.scale(endimg, (screen_width, screen_height)).convert_alpha()

#game title
pygame.display.set_caption("Snakes by Nandish")
pygame.display.update()

def text_screen(text, color, x, y):
    font = pygame.font.SysFont(None, 55)
    screen_text = font.render(text, True, color)
    gamewindow.blit(screen_text, [x, y])

def plot_snake(gameWindow, color, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False

    while not exit_game:
        gamewindow.fill(white)
        text_screen("Welcome to Snakes", black, 260, 250)
        text_screen("Press Space Bar To Play", black, 232, 290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()

        pygame.display.update()



# game loop
def gameloop():

    # Game variables

    exit_game = False
    game_over = False

    snake_x = 45
    snake_y = 55

    snake_list = []
    snake_lenght = 1

    snake_size = 30
    score = 0

    init_velocity = 5

    velocity_x = 0
    velocity_y = 0

    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)

    fps = 60
    clock = pygame.time.Clock()

    #check if file is created or not
    if (not os.path.exists("hiscore.txt")):
        with open("hiscore.txt", "w") as f:
            f.write("0")

    with open("hiscore.txt", "r") as f:
        hiscore = f.read()



    while not exit_game:

        if game_over:

            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))

            gamewindow.fill(white)
            gamewindow.blit(endimg, (0, 0))
            text_screen("Game over enter to Continue",brown,150,100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

        else :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True




                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d :
                        velocity_x = init_velocity
                        velocity_y = 0


                    if event.key == pygame.K_a :
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_w:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_s :
                        velocity_y = init_velocity
                        velocity_x = 0

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





            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) < 30 and abs(snake_y - food_y) < 30:
                score += 10
                print("hiscore : ",hiscore)
                print("score : ", score )
                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
                snake_lenght += 5

                if score > int(hiscore):
                    hiscore = score
            gamewindow.fill(white)
            gamewindow.blit(bgimg, (0, 0))
            text_screen("Score: " + str(score), blue, 5, 5)
            text_screen("Hiscore : "+ str(hiscore),blue,650,5)
            pygame.draw.rect(gamewindow, brown, [food_x, food_y, snake_size, snake_size])


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_lenght:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                print("Game over")

            plot_snake(gamewindow, black, snake_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()
gameloop()
