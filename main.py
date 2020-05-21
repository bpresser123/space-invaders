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

def player():
  screen.blit(playerImg, (playerX, playerY))


# Game loop
running = True
while running:

  screen.fill((0, 0, 0))

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  player()
  pygame.display.update()