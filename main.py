import pygame
import sys
import settings
import player


'''
EXAMPLE:

player = pygame.Rect(10, 10, 50, 50)

rectSurface = pygame.Surface((50,50))
pygame.draw.rect(rectSurface, pygame.Color('red'), player)

x = 0
y = 0
for i in range(0,30):
	screen.blit(rectSurface, (x, y))
	pygame.display.update()
	pygame.time.delay(100)
	x += 10
	y += 10
'''

def initEnvironment():
	circle = pygame.draw.circle(settings.screen, pygame.Color('white'), 
		(settings.screen_width/2, settings.screen_height/2), 50)


if __name__ == "__main__":

	initEnvironment()

	player1 = player.Player('daniel')
	player2 = player.Player('marten')

	# gameLoop()

	pygame.display.update()
	pygame.time.delay(1000)

	pygame.display.quit()
	print player1.getName(), player1.ik
















