import pygame
import random
import os

pygame.mixer.init()

pygame.init()

#colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)

#display variables
DIS_HEIGHT=500
DIS_WIDTH=800
game_window=pygame.display.set_mode((DIS_WIDTH,DIS_HEIGHT))
pygame.display.set_caption("SNAKES")

font = pygame.font.SysFont(None, 40)
def Screen_text(text, color, x, y):
    screen_text = font.render(text, True, color)
    game_window.blit(screen_text, [x, y])

#to apply background
'''
img=pygame.image.load(" <path to img>")
img=pygame.transform.scale(img, (DIS_WIDTH,DIS_HEIGHT)).convert_alpha()
#then add game_window.blit(img,(0,0))

'''



clock=pygame.time.Clock()
def welcome():
    game_exit=False
    colourrr=(100,100,100)
    while not game_exit:
        game_window.fill(colourrr)
        Screen_text("Welcome To  SNAKES", black, 260, 210)
        Screen_text("Hit 'SpaceBar' To 'Play'", black, 260, 465)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    game_exit = True
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load("electronic.mp3")
                    pygame.mixer.music.play()
                    gameLoop()

        pygame.display.update()
        clock.tick(60)

#game loop
def gameLoop():
    # game variables
    game_over = False
    game_exit = False
    fps = 30
    scrore = 0

    # snake
    snakegetX = DIS_WIDTH / 2
    snakegetY = DIS_HEIGHT / 2
    snake_color=(white)
    headsize = 20
    velocity=7
    velocityx = 0
    velocityy = 0
    snakelist = []
    snakelength = 1

    def plotsnake(game_window, black, snakelist, headsize):
        for x, y in snakelist:
            pygame.draw.rect(game_window, black, [x, y, headsize, headsize])

    # food
    foodx = random.randint(DIS_WIDTH / 5, 4 * DIS_WIDTH / 5)
    foody = random.randint(DIS_HEIGHT / 5, 4 * DIS_HEIGHT / 5)
    foodsize = 20
    food_color = (255, 0, 0)
    if (not os.path.exists("highscore_snakegame.txt")):
        with open("highscore_snakegame.txt", "w") as f:
            f.write("0")
    with open("highscore_snakegame.txt", "r") as f:
        highscore = f.read()

    while not game_exit:
        if game_over==True:
            with open("highscore_snakegame.txt", "w") as f:
                f.write(str(highscore))
            game_window.fill(black)
            Screen_text("Game Over!!",red, 330,DIS_HEIGHT/2)
            Screen_text("Press Enter to continue", red, 260, 465)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        game_exit = True
                    elif event.key == pygame.K_RETURN:
                        pygame.mixer.music.load("electronic.mp3")
                        pygame.mixer.music.play()
                        gameLoop()
        else:
                game_window.fill(black)
                for event in pygame.event.get():
                        # print(event)

                        if event.type==pygame.QUIT:
                            game_exit=True

                        if event.type==pygame.KEYDOWN:
                            if event.key== pygame.K_UP:
                                velocityy=velocity
                                velocityx=0
                            elif  event.key== pygame.K_RIGHT:
                                velocityy=0
                                velocityx=velocity
                            elif event.key == pygame.K_LEFT:
                                velocityy = 0
                                velocityx = -velocity
                            elif event.key == pygame.K_DOWN:
                                velocityy = -velocity
                                velocityx = 0
                            elif event.key == pygame.K_x:
                                game_exit=True



                if abs(snakegetY-foody)<(foodsize*2+headsize)/3 and abs(snakegetX-foodx)<(foodsize+headsize)/2:
                    scrore+=10
                    snakelength+=5
                    if scrore>int(highscore):
                        highscore=scrore
                    foodx = random.randint(DIS_WIDTH / 5, 4 * DIS_WIDTH / 5)
                    foody = random.randint(DIS_HEIGHT / 5, 4 * DIS_HEIGHT / 5)
                    #to add diff color food
                    '''a = random.randint(50, 255)
                    b = random.randint(50, 255)
                    c = random.randint(50, 255)
                    pygame.draw.rect(game_window, (a, b, c), [foodx, foody, foodsize, foodsize])
                    food_color=(a,b,c)'''

                    # print("score",scrore)


                snakegetX+=velocityx
                snakegetY-=velocityy

                if snakegetY>DIS_HEIGHT or snakegetY<0 or snakegetX>DIS_WIDTH or snakegetX<0:
                    game_over=True


                head=[]
                head.append(snakegetX)
                head.append(snakegetY)
                snakelist.append(head)
                if len(snakelist)>snakelength:
                    del snakelist[0]
                if head in snakelist[:-1]:
                    game_over=True
                Screen_text("Score: " + str(scrore)+"  High Score: "+ str(highscore), (0,155,255), DIS_WIDTH-400, DIS_HEIGHT-50)
                # pygame.draw.rect(game_window, black, [snakegetX,snakegetY,headsize,headsize])
                plotsnake(game_window, snake_color, snakelist, headsize)
                pygame.draw.circle(game_window,food_color,[foodx,foody],foodsize/2)
                #pygame.draw.rect(game_window, food_color, [foodx, foody, foodsize,foodsize])

        pygame.display.update()
        clock.tick(fps)

pygame.mixer.music.load("both-of-us.mp3")
pygame.mixer.music.play()
                        
welcome()
# gameLoop()

pygame.quit()
quit()