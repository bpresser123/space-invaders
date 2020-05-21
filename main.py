import pygame 

pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Caption and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('./assets/alien.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('./assets/ship3.png')
playerX = 370
playerY = 480
playerX_change = 0

def player(x,y):
  screen.blit(playerImg, (x, y))


# Game loop
running = True
while running:

  screen.fill((0, 0, 0))  

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
            playerX_change -= 1
      if event.key == pygame.K_RIGHT:
            playerX_change += 1
      if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
          playerX_change = 0

  playerX += playerX_change
  player(playerX, playerY)
  pygame.display.update()