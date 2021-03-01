import pygame, sys, random

# Pygame Setup
pygame.mixer.pre_init(44100, -16, 2, 512) 
pygame.init()
clock = pygame.time.Clock()

#extendo mode boolean INP, 1 for true, 0 for false, add code to flip this later
extendo = 1

# Game Window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')

# Colors
light_grey = (200,200,200)
bg_color = pygame.Color('grey12')

# Game Rectangles
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10,140)
opponent = pygame.Rect(10, screen_height / 2 - 70, 10,140)

#extended rectangles

playerExtendTop = pygame.Rect(((screen_width / 4) * 3) - 45, 20, 90, 10)
playerExtendBottom = pygame.Rect(((screen_width / 4) * 3) - 45, screen_height - 20, 90, 10)
opponentExtendTop = pygame.Rect((screen_width / 4) - 45, 20, 90, 10)
opponentExtendBottom = pygame.Rect((screen_width / 4) - 45, screen_height - 20, 90, 10)

# Game Variables
ball_speed_x = 7 * random.choice((1,-1)) 
ball_speed_y = 7 * random.choice((1,-1)) 
player_speed = 0
opponent_speed = 7

# Score Text
player_score = 0
opponent_score = 0
basic_font = pygame.font.Font('freesansbold.ttf', 32)

# Sound Effects
pong_sound = pygame.mixer.Sound("./media/pong.ogg") 
score_sound = pygame.mixer.Sound("./media/score.ogg") 


def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score
    
    ball.x += ball_speed_x
    ball.y += ball_speed_y



    # Ball Collision (Top or Bottom)
    if ball.y <= 0 or ball.y >= screen_height:

     pygame.mixer.Sound.play(pong_sound)
     ball_speed_y *= -1
    
    # Player Scores
    if ball.left <= 0: 
        pygame.mixer.Sound.play(score_sound)
        player_score += 1 
        ball_restart() 

        

    # Opponent Scores
    if ball.right >= screen_width:
        pygame.mixer.Sound.play(score_sound) 
        opponent_score += 1 
        ball_restart() 

    # Ball Collision (Player or Opponent)
    if ball.colliderect(player) or ball.colliderect(opponent):
        pygame.mixer.Sound.play(pong_sound)
        ball_speed_x *= -1




def ball_animation_extendo():

    global ball_speed_x, ball_speed_y, player_score, opponent_score
    
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.y <= 0 or ball.y >= screen_height:
        ballTopBottomScore()
    
        # Player Scores
    if ball.left <= 0: 
        pygame.mixer.Sound.play(score_sound)
        player_score += 1 
        ball_restart() 

    # Opponent Scores
    if ball.right >= screen_width:
        pygame.mixer.Sound.play(score_sound) 
        opponent_score += 1 
        ball_restart() 

    # Ball Collision (Player or Opponent)
    if ball.colliderect(player) or ball.colliderect(opponent):
        pygame.mixer.Sound.play(pong_sound)
        ball_speed_x *= -1
        

    if ball.colliderect(playerExtendTop) or ball.colliderect(opponentExtendTop) or ball.colliderect(playerExtendBottom) or ball.colliderect(opponentExtendBottom):
        pygame.mixer.Sound.play(pong_sound)
        ball_speed_y *= -1

def player_animation_extendo():    
    player.y += player_speed
    playerExtendTop.x -= player_speed
    playerExtendBottom.x += player_speed



    if player.top <= 0:
        player.top = 0
 

    if player.bottom >= screen_height:
        player.bottom = screen_height

    if playerExtendTop.left <= screen_width / 2:
        playerExtendTop.left = screen_width / 2
    
    if playerExtendBottom.left <= screen_width / 2:
        playerExtendBottom.left = screen_width / 2

    if playerExtendTop.right >= screen_width:
        playerExtendTop.right = screen_width
    
    if playerExtendBottom.right >= screen_width:
        playerExtendBottom.right = screen_width

         







#td: this needs a total rewrite

def opponent_ai_extendo():
    if opponent.top < ball.y:
        opponent.y += opponent_speed
        opponentExtendTop.x += opponent_speed
        opponentExtendBottom.x -= opponent_speed

    if opponent.bottom > ball.y:
        opponent.y -= opponent_speed
        opponentExtendBottom.x += opponent_speed
        opponentExtendTop.x -= opponent_speed


    if opponent.top <= 0:
        opponent.top = 0

    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height
    
    if opponentExtendTop.right > (screen_width / 2):
        opponentExtendTop.right = screen_width / 2
    
    if opponentExtendBottom.right > screen_width / 2:
        opponentExtendBottom.right = screen_width / 2

    if opponentExtendTop.left < 0:
        opponentExtendTop.left = 0
    
    if opponentExtendBottom.left < 0:
        opponentExtendBottom.left = 0




    


def player_animation():
    player.y += player_speed

    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def opponent_ai():
    if opponent.top < ball.y:
        opponent.y += opponent_speed
    if opponent.bottom > ball.y:
        opponent.y -= opponent_speed

    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def ball_restart():
    global ball_speed_x, ball_speed_y

    # move ball to the center
    ball.center = (screen_width/2, screen_height/2)

    # start the ball in a random direction
    ball_speed_y *= random.choice((1,-1)) 
    ball_speed_x *= random.choice((1,-1))  




def ballTopBottomScore():
    global player_score, opponent_score
    if ball.y <= 0 or ball.y >= screen_height and extendo == True:
     if ball.x <= (screen_width / 2):
                pygame.mixer.Sound.play(score_sound)
                player_score += 1 
                ball_restart() 
     else:
         pygame.mixer.Sound.play(score_sound)
         opponent_score += 1
         ball_restart()


        



if __name__ == "__main__":

  while True:
    for event in pygame.event.get():

      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
          player_speed -= 6
        if event.key == pygame.K_DOWN:
          player_speed += 6
      if event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
          player_speed += 6
        if event.key == pygame.K_DOWN:
          player_speed -= 6

    if extendo == True:
          player_animation_extendo()
          ball_animation_extendo()
          opponent_ai_extendo()
    else:
         player_animation()
         opponent_ai()
         ball_animation()
         playerExtendTop = pygame.Rect(0,0,0,0)
         playerExtendBottom = pygame.Rect(0,0,0,0)
         opponentExtendBottom = pygame.Rect(0,0,0,0)
         opponentExtendTop = pygame.Rect(0,0,0,0)


    # Visuals 
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.rect(screen, light_grey, playerExtendTop)
    pygame.draw.rect(screen, light_grey, playerExtendBottom)
    pygame.draw.rect(screen, light_grey, opponentExtendTop)
    pygame.draw.rect(screen, light_grey, opponentExtendBottom)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0),(screen_width / 2, screen_height))

    # Creating the surface for text
    player_text = basic_font.render(f'{player_score}',False,light_grey)
    screen.blit(player_text,(660,470)) 

    opponent_text = basic_font.render(f'{opponent_score}',False,light_grey)
    screen.blit(opponent_text,(600,470)) 

    # Loop Timer
    pygame.display.flip()
    clock.tick(60)