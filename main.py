import pygame, sys, random

def ball_animation():
  global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time
  ball.x += ball_speed_x
  ball.y += ball_speed_y

  if ball.top <= 0 or ball.bottom >= screen_height:
    ball_speed_y *= -1
    pygame.mixer.Sound.play(pong_sound)
  if ball.left <=0:
    score_time = pygame.time.get_ticks()
    player_score += 1
    pygame.mixer.Sound.play(score_sound)
  if ball.right >= screen_width:
    score_time = pygame.time.get_ticks()
    opponent_score+=1
    pygame.mixer.Sound.play(score_sound)
  if ball.colliderect(player) or ball.colliderect(opponent):
    ball_speed_x *= -1
    pygame.mixer.Sound.play(pong_sound)


def player_animation():
  global player
  player.y += player_speed
  if player.top <= 0:
    player.top = 0
  if player.bottom >= screen_height:
    player.bottom = screen_height

def opponent_animation():
  global opponent
  if opponent.bottom - 20 <= ball.top: 
    opponent.y += opponent_speed
  if opponent.top +20 >= ball.bottom:
    opponent.y -= opponent_speed

  if opponent.top <= 0:
    opponent.top = 0
  if opponent.bottom >= screen_height:
    opponent.bottom = screen_height

def ball_restart():
  global ball_speed_x, ball_speed_y, ball, score_time
  ball.center = (screen_width/2, screen_height/2)
  current_time = pygame.time.get_ticks()

  if current_time - score_time < 700:
    number_three = basic_font.render("3",False, orange)
    screen.blit(number_three, (screen_width/2 - 10, screen_height/2 - 200))
  if 700 < current_time - score_time < 1400:
    number_two = basic_font.render("2",False, orange)
    screen.blit(number_two, (screen_width/2 - 10, screen_height/2 - 200))
  if 1400 < current_time - score_time < 2100:
    number_one = basic_font.render("1",False, orange)
    screen.blit(number_one, (screen_width/2 - 10, screen_height/2 - 200))



  if current_time - score_time <= 2100:
    ball_speed_y, ball_speed_x = 0,0
  else:
    ball_speed_x = 7 * random.choice((1,-1))
    ball_speed_y = 7 * random.choice((1,-1))
    score_time = None
    



pygame.init()
clock = pygame.time.Clock()

screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("PONG")

ball = pygame.Rect(screen_width/2-15, screen_height/2-15, 30, 30)
player = pygame.Rect(screen_width-20, screen_height/2-75, 10, 150)
opponent = pygame.Rect(10, screen_height/2-75, 10, 150)

bg = pygame.Color((2, 48, 71))
orange = pygame.Color((251, 133, 0))
yellow = pygame.Color((255, 183, 3))

ball_speed_x = 7*random.choice((-1, 1))
ball_speed_y = 7*random.choice((-1, 1))
player_speed = 0
opponent_speed = 7
score_time = True

player_score = 0
opponent_score = 0
basic_font = pygame.font.Font('freesansbold.ttf', 32)

pong_sound = pygame.mixer.Sound("pong.ogg")
score_sound = pygame.mixer.Sound("score.ogg")




while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_DOWN:
        player_speed += 7
      if event.key == pygame.K_UP:
        player_speed -= 7

    if event.type == pygame.KEYUP:
      if event.key == pygame.K_DOWN:
        player_speed -= 7
      if event.key == pygame.K_UP:
        player_speed += 7
    


  ball_animation()
  player_animation()
  opponent_animation()


  screen.fill(bg)
  pygame.draw.aaline(screen, orange, (screen_width/2, 0), (screen_width/2, screen_height))
  pygame.draw.rect(screen, orange, player)
  pygame.draw.rect(screen, orange, opponent)
  pygame.draw.ellipse(screen, yellow, ball)

  if score_time:
    ball_restart()

  player_text = basic_font.render(f'{player_score}', False, orange)
  screen.blit(player_text,(screen_width/2+100, screen_height/2-16))

  opponent_text = basic_font.render(f'{opponent_score}',False, orange)
  screen.blit(opponent_text,(screen_width/2-100, screen_height/2-16))



  pygame.display.flip()
  clock.tick(60)




