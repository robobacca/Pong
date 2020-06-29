'''
Created on 28 May 2020

@author: Samuel
'''
import pygame
import random
import sys

pygame.init()   #initialises pygame

global clock,screen,width,height,score_player_1,score_player_2,dx,dy,ball_flag,paddlesize

width = 800
height = 600

#sets colour of the program
black = (0,0,0)
white = (255,255,255)

#sets a variable for time-related functions
clock = pygame.time.Clock()

#sets display surface for the game
screen = pygame.display.set_mode((width,height)) #sets resolution of the screen

#sets font of the game
font1 = pygame.font.Font('nasalization-rg.ttf',50)
font2 = pygame.font.Font('nasalization-rg.ttf',30)

#sets the variables for the screens of each scenario
run = True
intro = True
how_to_play = False
settings = False
main = False
pause = False
end_game = False

#sets paddle sizes
paddlesize = 120

#sets all player's score to 0
score_player_1 = 0
score_player_2 = 0

#sets the velocity of the ball in terms of difference in x and y
dx = [5,-5]
dy = [[1,2,3],[-1,-2,-3]]

#sets the texts needed for the game
intro_text_main = font1.render('Pong',False,white)
intro_text_mainRect = intro_text_main.get_rect()
intro_text_mainRect.center = (width//2,height//2 - 90)

intro_text_start = font2.render('Start Game',False,white)
intro_text_startRect = intro_text_start.get_rect()
intro_text_startRect.center = (width//2,height//2)

intro_text_htp = font2.render('How to Play',False,white)
intro_text_htpRect = intro_text_htp.get_rect()
intro_text_htpRect.center = (width//2,height//2 + 50)

intro_text_exit = font2.render('Exit Game',False,white)
intro_text_exitRect = intro_text_exit.get_rect()
intro_text_exitRect.center = (width//2,height//2 + 100)

exit_text = font2.render('Press Escape to return to main menu',False,white)
exit_textRect = exit_text.get_rect()
exit_textRect.center = (100,50)

pause_text_main = font1.render('Game Paused',False,white)
pause_text_mainRect = pause_text_main.get_rect()
pause_text_mainRect.center = (width//2,height//2 - 90)

pause_exit_text = font2.render('Press Escape to return to Game',False,white)
pause_exit_textRect = pause_exit_text.get_rect()
pause_exit_textRect.center = (width//2,50)

pause_text_1 = font2.render('Main Menu',False,white)
pause_text_1Rect = pause_text_1.get_rect()
pause_text_1Rect.center = (width//2,height//2)

pause_text_2 = font2.render('Exit Game',False,white)
pause_text_2Rect = pause_text_2.get_rect()
pause_text_2Rect.center = (width//2,height//2 + 50)

htp_text_main = font1.render('HOW TO PLAY',False,white)
htp_text_mainRect = htp_text_main.get_rect()
htp_text_mainRect.center = (width//2,100)

htp_text_1 = font2.render('Pres W and S to control the left paddle',False,white)
htp_text_1Rect = htp_text_1.get_rect()
htp_text_1Rect.center = (width//2,200)

htp_text_2 = font2.render('Pres UP ATTOW and DOWN ARROW',False,white)
htp_text_2Rect = htp_text_2.get_rect()
htp_text_2Rect.center = (width//2,250)

htp_text_3 = font2.render('to control the right paddle',False,white)
htp_text_3Rect = htp_text_3.get_rect()
htp_text_3Rect.center = (width//2,300)

htp_text_4 = font2.render('Press escape to pause the game mid-way',False,white)
htp_text_4Rect = htp_text_4.get_rect()
htp_text_4Rect.center = (width//2,350)

htp_text_5 = font2.render('First to 10 points',False,white)
htp_text_5Rect = htp_text_5.get_rect()
htp_text_5Rect.center = (width//2,height//2 + 150)

htp_text_6 = font2.render('Wins the game!',False,white)
htp_text_6Rect = htp_text_6.get_rect()
htp_text_6Rect.center = (width//2,height//2 + 200)

htp_exit_text = font2.render('Press Escape to return to Main Menu',False,white)
htp_exit_textRect = htp_exit_text.get_rect()
htp_exit_textRect.center = (width//2,50)

end_text_main = font1.render('Game Over',False,white)
end_text_mainRect = end_text_main.get_rect()
end_text_mainRect.center = (width//2,100)

end_text_1 = font1.render('Player 1 Wins!',False,white)
end_text_1Rect = end_text_1.get_rect()
end_text_1Rect.center = (width//2,height//2)

end_text_2 = font1.render('Player 2 Wins!',False,white)
end_text_2Rect = end_text_2.get_rect()
end_text_2Rect.center = (width//2,height//2)

end_text_3 = font2.render('Press enter to return to the Main Menu',False,white)
end_text_3Rect = end_text_3.get_rect()
end_text_3Rect.center = (width//2,450)

class Selector(pygame.sprite.Sprite):   #Creatas class of sprite object for the rectangular selector
    def __init__(self,x,y,state):
        super().__init__()
        self.x = x
        self.y = y
        self.state = state
        selectorsurface = pygame.Surface([251,51], pygame.SRCALPHA, 32)
        selectorsurface = selectorsurface.convert_alpha()
        pygame.draw.rect(selectorsurface,white,(0,0,250,50),2)
        self.image = selectorsurface
        self.rect = self.image.get_rect(center = (x,y))
        
class Paddle(pygame.sprite.Sprite):   #creates a class of sprite objects for paddles
    def __init__(self,x,y):
        super().__init__()
        self.x = x
        self.y = y
        surface1 = pygame.Surface((15, paddlesize))
        surface1.fill(white)
        self.image = surface1
        self.rect = self.image.get_rect(center = (x,y))
        self.vel = [0,0]    #sets velocity for x and y respectively
        
    def update(self):
        #self.rect.x += self.vel[0]
        self.rect.y += self.vel[1]
        if self.rect.top < 150:
            self.rect.top = 150
        if self.rect.bottom > 600:
            self.rect.bottom = 600
            
class Ball(pygame.sprite.Sprite):   #Creatas class of sprite object for the ball
    def __init__(self,x,y,statex,statey,color):
        super().__init__()
        self.x = x
        self.y = y
        self.color = color
        self.statex = statex
        self.statey = statey
        surface2 = pygame.Surface([20,20], pygame.SRCALPHA, 32)
        surface2 = surface2.convert_alpha()
        pygame.draw.circle(surface2, (self.color), (10,10), 10)
        self.image = surface2
        self.rect = self.image.get_rect(center = (x,y))

#creates selector rectangle        
intro_selector = Selector(width//2,height//2,1)
selector_group_1 = pygame.sprite.Group()
selector_group_1.add(intro_selector)

paused_selector = Selector(width//2,height//2,1)
selector_group_2 = pygame.sprite.Group()
selector_group_2.add(paused_selector)

#Create the 2 paddles
paddle1 = Paddle(75,150 + (paddlesize//2))
paddle2 = Paddle(725,600 - (paddlesize//2))
paddle_group = pygame.sprite.Group()
paddle_group.add(paddle1, paddle2)
    
ball = Ball(width//2,(height+150)//2,1,1,white)
ball_group = pygame.sprite.Group()
ball_group.add(ball)

#loads and plays background music
pygame.mixer.music.load("music.wav")
pygame.mixer.music.play(-1)

while run:       
    while intro:
        screen.fill(black)
        
        #draws the selector to the screen
        selector_group_1.draw(screen)
        
        #draws texts to the intro screen
        screen.blit(intro_text_main,intro_text_mainRect)
        screen.blit(intro_text_start,intro_text_startRect)
        screen.blit(intro_text_htp,intro_text_htpRect)
        screen.blit(intro_text_exit,intro_text_exitRect)
        
        #keyboard inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #allows users to end the program when clicking the red X at the top of the screen
                run = False
                pygame.quit()
                sys.exit()
            
            #najes the selector move(part 1)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    if intro_selector.state == 1:
                        intro_selector.state = 2
                    elif intro_selector.state == 2:
                        intro_selector.state = 3
                    elif intro_selector.state == 3:
                        intro_selector.state = 1
                
                if event.key == pygame.K_w:
                    if intro_selector.state == 1:
                        intro_selector.state = 3
                    elif intro_selector.state == 2:
                        intro_selector.state = 1
                    elif intro_selector.state == 3:
                        intro_selector.state = 2
                    
                #for users to select input to the program    
                if event.key == pygame.K_RETURN:
                    if intro_selector.state == 1:
                        #resets game
                        ball.rect.x = width//2
                        ball.rect.y = (height + 150)//2
                        ball.statex = 1
                        ball.statey = 1
                        paddle1.rect.y = 150
                        paddle2.rect.y = 600 - (paddlesize//2)
                        #starts main code
                        intro = False
                        main = True
                    elif intro_selector.state == 2:
                        how_to_play = True
                        intro = False
                    elif intro_selector.state == 3:
                        #exits game
                        run = False
                        intro = False
                        sys.exit()
                        pygame.quit()
        
        #najes the selector move(part 2)
        if intro_selector.state == 1:
            intro_selector.rect.y = height//2 -25
        elif intro_selector.state == 2:
            intro_selector.rect.y = height//2+25
        elif intro_selector.state == 3:
            intro_selector.rect.y = height//2+75
            
        
        pygame.display.update()
        clock.tick(60)
    
    #How to play screen
    while how_to_play:
        screen.fill(black)
        
        #creates text
        screen.blit(htp_exit_text,htp_exit_textRect)
        screen.blit(htp_text_1,htp_text_1Rect)
        screen.blit(htp_text_2,htp_text_2Rect)
        screen.blit(htp_text_3,htp_text_3Rect)
        screen.blit(htp_text_4,htp_text_4Rect)
        screen.blit(htp_text_5,htp_text_5Rect)
        screen.blit(htp_text_6,htp_text_6Rect)
        screen.blit(htp_text_main,htp_text_mainRect)
        
        #event input programs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #allows users to end the program when clicking the red X at the top of the screen
                main = False
                run = False
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    how_to_play = False
                    intro = True
            
        pygame.display.update()
        
        clock.tick(60)
    
    #pause screen
    while pause:
        screen.fill(black)
        
        #creates the selector
        selector_group_2.draw(screen)
        
        #creates texts
        screen.blit(pause_text_main,pause_text_mainRect)
        screen.blit(pause_exit_text,pause_exit_textRect)
        screen.blit(pause_text_1,pause_text_1Rect)
        screen.blit(pause_text_2,pause_text_2Rect)
        
        #event input programs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #allows users to end the program when clicking the red X at the top of the screen
                main = False
                run = False
                pygame.quit()
                sys.exit()
                
            #pauses the screen
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause = False
                    main = True
                    
                if event.key == pygame.K_s:
                    if paused_selector.state == 1:
                        paused_selector.state = 2
                    elif paused_selector.state == 2:
                        paused_selector.state = 1
                        
                if event.key == pygame.K_w:
                    if paused_selector.state == 1:
                        paused_selector.state = 2
                    elif paused_selector.state == 2:
                        paused_selector.state = 1
                
                if event.key == pygame.K_RETURN:
                    if paused_selector.state == 1:
                        intro = True
                        pause = False
                    if paused_selector.state == 2:
                        run = False
                        sys.exit()
                        pygame.quit()
                    
        if paused_selector.state == 1:
            paused_selector.rect.y = height//2 -25
        elif paused_selector.state == 2:
            paused_selector.rect.y = height//2+25
        
        pygame.display.update()
        
        clock.tick(60)
    
    #main program
    while main:
        screen.fill(black)  #sets backgorund colour
        paddle_group.draw(screen)   #draws paddles to the screen
        paddle_group.update()
        ball_group.draw(screen) #draws ball to the screen
        
        #sets text to the screen for scores
        player1_text = font1.render('Player 1 {:>8d}'.format(score_player_1),False,white)
        player1_textRect = player1_text.get_rect()
        player1_textRect.center = (25,75)
    
        player2_text = font1.render('Player 2 {:>8d}'.format(score_player_2),False,white)
        player2_textRect = player2_text.get_rect()
        player2_textRect.center = (425,75)
        
        #draws lines on the screen
        pygame.draw.line(screen,white,(0,150),(800,150),3)
        pygame.draw.line(screen,white,(width//2,0),(width//2,600),3)
        
        #draws texts to the screen
        screen.blit(player1_text,player1_textRect.center)
        screen.blit(player2_text,player2_textRect.center)
        
        #event input programs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #allows users to end the program when clicking the red X at the top of the screen
                main = False
                run = False
                pygame.quit()
                sys.exit()
                
            #pauses the screen
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause = True
                    main = False
                
            #inputs to move paddles up and down
            key = pygame.key.get_pressed()
            if key[pygame.K_w]:
                paddle1.vel[1] = -5
            elif key[pygame.K_s]:
                paddle1.vel[1] = 5
            else:
                paddle1.vel[1] = 0
                
            if key[pygame.K_UP]:
                paddle2.vel[1] = -5
            elif key[pygame.K_DOWN]:
                paddle2.vel[1] = 5
            else:
                paddle2.vel[1] = 0
                
        #reflection of ball
        if ball.statex == 1:
            ball.rect.x += dx[1]
            if ball.rect.left <= paddle1.rect.right:
                if ball.rect.right >= paddle1.rect.right - 5:
                    if ball.rect.y + 10 <= paddle1.rect.bottom:
                        if ball.rect.y + 10>= paddle1.rect.top:
                            ball.statex = 0
        
        if ball.statex == 0:
            ball.rect.x += dx[0]
            if ball.rect.right >= paddle2.rect.left:
                if ball.rect.left <= paddle2.rect.left + 5:
                    if ball.rect.y + 10<= paddle2.rect.bottom:
                        if ball.rect.y + 10 >= paddle2.rect.top:
                            ball.statex = 1
                            
        if ball.statey == 1:
            ball.rect.y += random.choice(dy[1])
            if ball.rect.top <= 150:
                ball.statey = 0
        
        if ball.statey == 0:
            ball.rect.y += random.choice(dy[0])
            if ball.rect.bottom >= 600:
                ball.statey = 1
                
        #scoring system
        if ball.rect.right <= paddle1.rect.left:
            #increase score of player
            score_player_2 += 1
            #sets ball to the middle
            ball.rect.x = width//2
            ball.rect.y = (height + 150)//2
            #makes the ball travel to winning paddle
            ball.statex = 1
            ball.statey = 1
            #resets the paddles
            paddle1.rect.y = 150
            paddle2.rect.y = 600 - (paddlesize//2)
            #pauses the code
            pygame.time.wait(2000)
    
        if ball.rect.left >= paddle2.rect.right:
            #increase score of player
            score_player_1 += 1
            #sets ball to the middle
            ball.rect.x = width//2
            ball.rect.y = (height + 150)//2
            #makes the ball travel to winning paddle
            ball.statex = 0
            ball.statey = 0
            #resets the paddles
            paddle1.rect.y = 150
            paddle2.rect.y = 600 - (paddlesize//2)
            #pauses the code
            pygame.time.wait(2000)
        
        if score_player_1 == 10 or score_player_2 == 10:
            end_game = True
            main = False
        
        
        
        pygame.display.update()
        
        clock.tick(60)  #sets the refresh rate to 6- frames per second
        
    while end_game:
        
        screen.fill(black)  #sets backgorund colour
        
        #display texts
        screen.blit(end_text_main,end_text_mainRect)
        screen.blit(end_text_3,end_text_3Rect)
        
        if score_player_1 == 10:
            screen.blit(end_text_1,end_text_1Rect)
        elif score_player_2 == 10:
            screen.blit(end_text_2,end_text_2Rect)
        
        #event input programs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #allows users to end the program when clicking the red X at the top of the screen
                main = False
                run = False
                pygame.quit()
                sys.exit()
                
            #return to Main Menu
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    end_game = False
                    intro = True
        
        pygame.display.update()
        
        clock.tick(60)  #sets the refresh rate to 6- frames per second