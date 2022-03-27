"""
Creator: Zain Banday
Date Created : 2022-01-18
Description: 2 player game controlled by WASD and ARROWS. Two Ships race to the top
to get points. If the ship collides with an asteroid, the ship is reset back to
the start. 60 Second timer per game.
"""



import pygame
import random
import math

pygame.init()


#set window size
winW = 800
winH = 800
dis = pygame.display.set_mode((winW, winH))

# Name of Game
pygame.display.set_caption("Space Race")

# Speed of game
clock = pygame.time.Clock()
FPS = 30


#game variables
running = True
preGame = True
gameOver = False
score_1 = 0
score_2 = 0

#ship variables
ship1X = 200
ship1Y = winH-80
ship1W = 53
ship1H = 53

ship2X = 600
ship2Y = winH-80
ship2W = 53
ship2H = 53

ship_speed = 5

#asteroid variables
asteroid_x_l = []
asteroid_y_l = []
asteroid_x_r = []
asteroid_y_r = []
wait_time_l = []
wait_time_r = []
asteroid_image_l = []
asteroid_image_r = []
asteroid_speed = 10
max_asteroids = 16
asteroid_w = 25

    
    

for count in range(max_asteroids//2):
    asteroid_image_l.append(pygame.image.load(r'D:Space Race Assets/asteroid_picture.png'))
    asteroid_image_r.append(pygame.image.load(r'D:Space Race Assets/asteroid_picture.png'))
for count in range(max_asteroids//2):
    asteroid_x_l.append(random.randint(-100, -35))
    asteroid_y_l.append(random.randint(0, winH-130))
    asteroid_x_r.append(random.randint(winW, winW+80))
    asteroid_y_r.append(random.randint(0, winH-130))
    wait_time_l.append(random.randrange(0, 50))
    wait_time_r.append(random.randrange(0,50))
    
    
# Initialize position of timer
timerX = 393.75
timerY = 0
timerW = 12.5
timerH = winH

# Initialize positon of border in the middle
mid_borderX = 393.75
mid_borderY = 0
mid_borderW = 12.5
mid_borderH = winH

# Timer variables
startTime = 6000


#Movement of Ship Variables
ship1UP = False
ship1DOWN = False
ship1LEFT = False
ship1RIGHT = False
ship2UP = False
ship2DOWN = False
ship2LEFT = False
ship2RIGHT = False

#colors
white = (255,255,255)
grey = (131, 139, 139)
red = (238, 0, 0)
blue = (142,229,238)

#load images
background_image = pygame.image.load(r'D:Space Race Assets/space_background.png').convert_alpha()
ship_image = pygame.image.load(r'D:Space Race Assets/pixel_ship.png').convert_alpha()
pregame_screen = pygame.image.load(r'D:Space Race Assets/pregame_screen.png').convert_alpha()
newgame_button = pygame.image.load(r'D:Space Race Assets/newgame_button.png').convert_alpha()
newgame_button_hover = pygame.image.load(r'D:Space Race Assets/newgame_button_hover.png').convert_alpha()

exit_button = pygame.image.load(r'D:Space Race Assets/exit_button.png').convert_alpha()
exit_button_hover = pygame.image.load(r'D:Space Race Assets/exit_button_hover.png').convert_alpha()

hard_button =  pygame.image.load(r'D:Space Race Assets/hardmode_button.png').convert_alpha()
hard_button_hover =  pygame.image.load(r'D:Space Race Assets/hardmode_button_hover.png').convert_alpha()
#load sounds
death_sound = pygame.mixer.Sound(
   r'D:Space Race Assets/death_sound.mp3')
score_sound = pygame.mixer.Sound(
   r'D:Space Race Assets/score_sound.mp3')
background_music = pygame.mixer.music.load(
   r'D:Space Race Assets/background_music.mp3')
pygame.mixer.music.play(-1, 0.0)


#load fonts
bigFont = pygame.font.Font(
   r'D:Space Race Assets/gameover_font.ttf', 60)
smallFont = pygame.font.Font(
    r'D:Space Race Assets/gameover_font.ttf', 20)



#functions
def add_ship(x,y):
    dis.blit(ship_image, [x,y])
    
def add_asteroid(image,x,y,i):
    dis.blit(pygame.transform.scale(image[i] , (asteroid_w, asteroid_w)), [x,y])

def isCollision(obstacleX, obstacleY, shipX, shipY, i):
    distance = math.sqrt(
        (math.pow(obstacleX[i]-shipX, 2)) + (math.pow(obstacleY[i]-shipY, 2)))
    if distance < 30:
        return True
    else:
        return False
    
def message(msg, color, x, y):
    mesg = bigFont.render(msg, True, color)
    dis.blit(mesg, [x, y])
    
def score_check(score1, score2):
    if score1>score2:
        return ('1win')
    elif score2>score1:
        return('2win')
    elif score1 == score2:
        return ('tie')




while running:   #<--------------- Main Game 

    while preGame: #<------------ Pregame Screen (menu)
        dis.blit(pregame_screen, [0,0])
        
        mouse = pygame.mouse.get_pos()

        (x, y) = mouse
        
        
        spacerace_text = bigFont.render("Space Race", True, red)

        dis.blit(spacerace_text, [200, 200])
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                running = False
                preGame = False
                
                
            #recieving input from pressing buttons
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #pressing exit button
                if 347 < x < 453 and 600 < y < 645:

                    running = False
                    preGame = False
                    
                #pressing Hard mode button
                if 330 < x < 470 and 500 < y < 565:
                    preGame = False
                    score_1 = 0
                    score_2 = 0
    
                    
                    ship1X = 200
                    ship1Y = winH-80
                    
    
                    ship2X = 600
                    ship2Y = winH-80
                    
                    #increasing difficulty because it is now hardmode
                    max_asteroid = 20
                    asteroid_speed = 15
                    asteroid_w = 30
                    
    
                    
                    asteroid_x_l = []
                    asteroid_y_l = []
                    asteroid_x_r = []
                    asteroid_y_r = []
                    wait_time_l = []
                    wait_time_r = []
                    asteroid_image_l = []
                    asteroid_image_r = []
                    
                    
                    for count in range(max_asteroids//2):
                        asteroid_image_l.append(pygame.image.load(r'D:Space Race Assets/asteroid_picture.png'))
                        asteroid_image_r.append(pygame.image.load(r'D:Space Race Assets/asteroid_picture.png'))
                    for count in range(max_asteroids//2):
                        asteroid_x_l.append(random.randint(-100, -35))
                        asteroid_y_l.append(random.randint(0, winH-130))
                        asteroid_x_r.append(random.randint(winW, winW+80))
                        asteroid_y_r.append(random.randint(0, winH-130))
                        wait_time_l.append(random.randrange(0, 50))
                        wait_time_r.append(random.randrange(0,50))
                        
                        
                    
                    
                    
                    timerH = winH
                    mid_borderH = winH
                    startTime = 6000
                   
            
            #pressing new game button    
                if 310 < x < 490 and 400 < y < 443:
                    #reset all variables for newgame
                    
                    preGame = False
                    score_1 = 0
                    score_2 = 0
    
                    
                    ship1X = 200
                    ship1Y = winH-80
                    
    
                    ship2X = 600
                    ship2Y = winH-80
                    
                    #resetting dificulty to easy
                    max_asteroid = 16
                    asteroid_speed = 10
                    asteroid_w  = 25
    
                    
                    asteroid_x_l = []
                    asteroid_y_l = []
                    asteroid_x_r = []
                    asteroid_y_r = []
                    wait_time_l = []
                    wait_time_r = []
                    asteroid_image_l = []
                    asteroid_image_r = []
                    
                    
    
                    for count in range(max_asteroids//2):
                        asteroid_image_l.append(pygame.image.load(r'D:Space Race Assets/asteroid_picture.png'))
                        asteroid_image_r.append(pygame.image.load(r'D:Space Race Assets/asteroid_picture.png'))
                    for count in range(max_asteroids//2):
                        asteroid_x_l.append(random.randint(-100, -35))
                        asteroid_y_l.append(random.randint(0, winH-130))
                        asteroid_x_r.append(random.randint(winW, winW+80))
                        asteroid_y_r.append(random.randint(0, winH-130))
                        wait_time_l.append(random.randrange(0, 50))
                        wait_time_r.append(random.randrange(0,50))
                        
                        
                    
                    
                    
                    timerH = winH
                    mid_borderH = winH
                    startTime = 6000
                
                    
                
        #drawing buttons
        #drawing newgame button
        if 310 < x < 490 and 400 < y < 443:
            dis.blit(newgame_button_hover, [310, 400])
        else:

            dis.blit(newgame_button, [310, 400])

#drawing exit button      
        if 347 < x < 453 and 600 < y < 645:
            dis.blit(exit_button_hover, [347, 600])

        else:

            dis.blit(exit_button, [347, 600])
            
        #drawing hard button
        if 330 < x < 470 and 500 < y < 565:
            dis.blit(pygame.transform.scale(hard_button_hover, (140,65)), [330, 500])
        else:
            dis.blit(pygame.transform.scale(hard_button, (140,65)), [330, 500])
            
            
        
        
        
        
        clock.tick(FPS)
        pygame.display.update()
        
    while gameOver: #<---------- Game Over screen (menu)
        dis.blit(pregame_screen, [0,0])
        
        mouse = pygame.mouse.get_pos()

        (x, y) = mouse
        
        gameover_message = bigFont.render("GAME OVER", True, red)
        spacerace_text = bigFont.render("Space Race", True, red)

        dis.blit(gameover_message, [200,100])
        dis.blit(spacerace_text, [200, 200])
        
        win_status = score_check(score_1, score_2)
        if win_status == ('1win'):
            winner_result = smallFont.render("The Winner is Player 1! The score was " + str(score_1) + " - " + str(score_2), True, blue)
        elif win_status == ('2win'):
            winner_result = smallFont.render("The Winner is Player 2! The score was " + str(score_2) + " - " + str(score_1), True, blue)
        elif win_status == ('tie'):
            winner_result = winner_result = smallFont.render("It was a Tie. The score was " + str(score_2) + " - " + str(score_1), True, blue)
        
        dis.blit(winner_result, [215, 300])
        
        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                running = False
                gameOver = False
                
                
            #recieving input from pressing buttons
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #pressing exit button
                if 347 < x < 453 and 600 < y < 645:

                    running = False
                    gameOver = False
                    
                 #pressing Hard mode button
                if 330 < x < 470 and 500 < y < 565:
                    gameOver = False
                    score_1 = 0
                    score_2 = 0
    
                    
                    ship1X = 200
                    ship1Y = winH-80
                    
    
                    ship2X = 600
                    ship2Y = winH-80
                    
                    #increasing difficulty because it is now hardmode
                    max_asteroid = 20
                    asteroid_speed = 15
                    asteroid_w = 30
                    
    
                    
                    asteroid_x_l = []
                    asteroid_y_l = []
                    asteroid_x_r = []
                    asteroid_y_r = []
                    wait_time_l = []
                    wait_time_r = []
                    asteroid_image_l = []
                    asteroid_image_r = []
                    
                    
                    for count in range(max_asteroids//2):
                        asteroid_image_l.append(pygame.image.load(r'D:Space Race Assets/asteroid_picture.png'))
                        asteroid_image_r.append(pygame.image.load(r'D:Space Race Assets/asteroid_picture.png'))
                    for count in range(max_asteroids//2):
                        asteroid_x_l.append(random.randint(-100, -35))
                        asteroid_y_l.append(random.randint(0, winH-130))
                        asteroid_x_r.append(random.randint(winW, winW+80))
                        asteroid_y_r.append(random.randint(0, winH-130))
                        wait_time_l.append(random.randrange(0, 50))
                        wait_time_r.append(random.randrange(0,50))
                        
                        
                    
                    
                    
                    timerH = winH
                    mid_borderH = winH
                    startTime = 6000
            
            #pressing new game button    
                if 310 < x < 490 and 400 < y < 443:
                    #reset all variables for newgame
                    
                    gameOver = False
                    score_1 = 0
                    score_2 = 0
    
                    
                    ship1X = 200
                    ship1Y = winH-80
                    
    
                    ship2X = 600
                    ship2Y = winH-80
                    
    
                    #resetting difficulty to easy
                    max_asteroid = 16
                    asteroid_speed = 10
                    asteroid_w = 25
                    
                    asteroid_x_l = []
                    asteroid_y_l = []
                    asteroid_x_r = []
                    asteroid_y_r = []
                    wait_time_l = []
                    wait_time_r = []
                    asteroid_image_l = []
                    asteroid_image_r = []
                    
                    
    
                    for count in range(max_asteroids//2):
                        asteroid_image_l.append(pygame.image.load(r'D:Space Race Assets/asteroid_picture.png'))
                        asteroid_image_r.append(pygame.image.load(r'D:Space Race Assets/asteroid_picture.png'))
                    for count in range(max_asteroids//2):
                        asteroid_x_l.append(random.randint(-100, -35))
                        asteroid_y_l.append(random.randint(0, winH-130))
                        asteroid_x_r.append(random.randint(winW, winW+80))
                        asteroid_y_r.append(random.randint(0, winH-130))
                        wait_time_l.append(random.randrange(0, 50))
                        wait_time_r.append(random.randrange(0,50))
                        
                        
                    
                    
                    
                    timerH = winH
                    mid_borderH = winH
                    startTime = 6000
                
                    
                
        #drawing buttons
        if 310 < x < 490 and 400 < y < 443:
            dis.blit(newgame_button_hover, [310, 400])
        else:

            dis.blit(newgame_button, [310, 400])

        if 347 < x < 453 and 600 < y < 645:
            dis.blit(exit_button_hover, [347, 600])

        else:

            dis.blit(exit_button, [347, 600])
            
        #drawing hard button
        if 330 < x < 470 and 500 < y < 565:
            dis.blit(pygame.transform.scale(hard_button_hover, (140,65)), [330, 500])
        else:
            dis.blit(pygame.transform.scale(hard_button, (140,65)), [330, 500])
            
            
            
        
        
        
        
        clock.tick(FPS)
        pygame.display.update()
        
    
    dis.blit(background_image, [0,0])
    
    
    # Close game if user clicks close button
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False
            


    # Movement of Ships
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                ship1UP = True
            if event.key == pygame.K_s:
                ship1DOWN = True
            if event.key == pygame.K_a:
                ship1LEFT = True
            if event.key == pygame.K_d:
                ship1RIGHT = True
                
            

            if event.key == pygame.K_UP:
                ship2UP = True
            if event.key == pygame.K_DOWN:
                ship2DOWN = True
            if event.key == pygame.K_LEFT:
                ship2LEFT = True
            if event.key == pygame.K_RIGHT:
                ship2RIGHT = True
                
            if event.key == pygame.K_ESCAPE:
                gameOver = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                ship1UP = False
            if event.key == pygame.K_s:
                ship1DOWN = False
            if event.key == pygame.K_a:
                ship1LEFT = False
            if event.key == pygame.K_d:
                ship1RIGHT = False
            if event.key == pygame.K_UP:
                ship2UP = False
            if event.key == pygame.K_DOWN:
                ship2DOWN = False
            if event.key == pygame.K_LEFT:
                ship2LEFT = False
            if event.key == pygame.K_RIGHT:
                ship2RIGHT = False
                
    if (ship1UP):
        ship1Y -= ship_speed
    if (ship1DOWN):
        ship1Y += ship_speed
    if (ship1LEFT):
        ship1X -= ship_speed
    if (ship1RIGHT):
        ship1X += ship_speed
    if (ship2UP):
        ship2Y -= ship_speed
    if (ship2DOWN):
        ship2Y += ship_speed
    if (ship2LEFT):
        ship2X -= ship_speed
    if (ship2RIGHT):
        ship2X += ship_speed
        
        
        
    #draw both ships
    add_ship(ship1X, ship1Y)
    add_ship(ship2X, ship2Y)
    
    #draw asteroids
    for count in range(max_asteroids//2):
        add_asteroid(asteroid_image_l, asteroid_x_l[count], asteroid_y_l[count], count)
        add_asteroid(asteroid_image_r, asteroid_x_r[count], asteroid_y_r[count], count)
        
    
        
    #move asteroids
    for count in range(max_asteroids//2):
        if wait_time_l[count] > 0:
            wait_time_l[count] -= 1
        elif wait_time_l[count] <= 0:
            asteroid_x_l[count] += asteroid_speed
        
        if wait_time_r[count] > 0:
            wait_time_r[count] -= 1
        elif wait_time_r[count] <= 0:
            asteroid_x_r[count] -= asteroid_speed
            
    #check if asteroids have passed the window
    for count in range (max_asteroids//2):
        if asteroid_x_l[count] + 30 >= winW:
            asteroid_x_l[count] = random.randint(-100, -35)
            asteroid_y_l[count] = random.randint(0, winH-130)
            wait_time_l[count] = random.randrange(0,50)
        
        if asteroid_x_r[count] <= -5:
            asteroid_x_r[count] = random.randint(winW, winW+80)
            asteroid_y_r[count] = random.randint(0, winH-130)
            wait_time_r[count] = random.randrange(0,50)
            
    # Collision for both ships with all asteroids
    for count in range(max_asteroids//2):
        collision_l_1 = isCollision(
            asteroid_x_l, asteroid_y_l, ship1X, ship1Y, count)
        if collision_l_1:
            ship1Y = winH - 60
            pygame.mixer.Sound.play(death_sound)
        collision_r_1 = isCollision(
            asteroid_x_r, asteroid_y_r, ship1X, ship1Y, count)
        if collision_r_1:
            ship1Y = winH - 60
            pygame.mixer.Sound.play(death_sound)
        collision_l_2 = isCollision(
            asteroid_x_l, asteroid_y_l, ship2X, ship2Y, count)
        if collision_l_2:
            ship2Y = winH - 60
            pygame.mixer.Sound.play(death_sound)
        collision_r_2 = isCollision(
            asteroid_x_r, asteroid_y_r, ship2X, ship2Y, count)
        if collision_r_2:
            ship2Y = winH - 60
            pygame.mixer.Sound.play(death_sound)
            
            
        # Draw Mid Border
    pygame.draw.rect(
        dis, red, [mid_borderX, mid_borderY, mid_borderW, mid_borderH])

        # Draw Timer
    pygame.draw.rect(dis, grey, [timerX, timerY, timerW, timerH])
    

    # Keep Ship 1 in window
    if ship1Y >= winH - ship1H:
        ship1Y = winH-ship1H
    if ship1X <= 0:
        ship1X = 0
    if ship1X >= timerX-ship1W:
        ship1X = timerX-ship1W

    # Keep Ship 2 in window
    if ship2Y >= winH - ship2H:
        ship2Y = winH - ship2H
    if ship2X >= winW - ship2W:
        ship2X = winW - ship2W
    if ship2X <= timerX + timerW:
        ship2X = timerX + timerW
        
    #check if ship has hit top of the window
    if ship1Y <= 0:
        ship1Y = winH-60
        score_1 += 1
        pygame.mixer.Sound.play(score_sound)

    if ship2Y <= 0:
        ship2Y = winH-60
        score_2 += 1
        pygame.mixer.Sound.play(score_sound)
    
    
    
        # decrease timer every frame
    startTime -= 3.333
    if startTime <= -0:
        gameOver = True
    timerH -= (winH/60)/ FPS
        
    # Display Score for player 1
    message(str(score_1), white, 340, winH - 60)
    # Display Score for player 2
    message(str(score_2), white, 430, winH - 60)
    
    #Display Timer
    timerText = bigFont.render(str(int((startTime/100)//1)), True, white)
    dis.blit(timerText, (50, 50))

    
    clock.tick(FPS)
    pygame.display.update()
    
pygame.quit()