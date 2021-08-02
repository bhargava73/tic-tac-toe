# Github link => https://github.com/bhargava73/tic-tac-toe

import pygame
from pygame import *

pygame.init()

screen_height = 300
screen_width = 300
line_width = 5
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tic Tac Toe')

red = (255, 102, 102)
green = (28, 141, 115)
blue = (53, 189, 208)

font = pygame.font.SysFont(None, 30)

clicked = False
player = 1
pos = (0,0)
markers = []
game_over = False
winner = 0

again_rect = Rect(screen_width // 2 - 70, screen_height // 2 + 35, 145, 30)

for x in range (3):
	row = [0] * 3
	markers.append(row)

def draw_board():
	bg = (239, 242, 246)
	grid = (50, 50, 50)
	screen.fill(bg)
	for x in range(1,3):
		pygame.draw.line(screen, grid, (0, 100 * x), (screen_width,100 * x), line_width)
		pygame.draw.line(screen, grid, (100 * x, 0), (100 * x, screen_height), line_width)

def draw_markers():
	x_pos = 0
	for x in markers:
		y_pos = 0
		for y in x:
			if y == 1:
				pygame.draw.line(screen, red, (x_pos * 100 + 15, y_pos * 100 + 15), (x_pos * 100 + 85, y_pos * 100 + 85), line_width)
				pygame.draw.line(screen, red, (x_pos * 100 + 85, y_pos * 100 + 15), (x_pos * 100 + 15, y_pos * 100 + 85), line_width)
			if y == -1:
				pygame.draw.circle(screen, blue, (x_pos * 100 + 50, y_pos * 100 + 50), 38, 4)
			y_pos += 1
		x_pos += 1


def check_game_over():
	global game_over
	global winner

	x_pos = 0
	for x in markers:
		if sum(x) == 3:
			winner = 1
			game_over = True
		if sum(x) == -3:
			winner = -1
			game_over = True
		if markers[0][x_pos] + markers [1][x_pos] + markers [2][x_pos] == 3:
			winner = 1
			game_over = True
		if markers[0][x_pos] + markers [1][x_pos] + markers [2][x_pos] == -3:
			winner = -1
			game_over = True
		x_pos += 1

	if markers[0][0] + markers[1][1] + markers [2][2] == 3 or markers[2][0] + markers[1][1] + markers [0][2] == 3:
		winner = 1
		game_over = True
	if markers[0][0] + markers[1][1] + markers [2][2] == -3 or markers[2][0] + markers[1][1] + markers [0][2] == -3:
		winner = -1
		game_over = True

	if game_over == False:
		tie = True
		for row in markers:
			for i in row:
				if i == 0:
					tie = False
		if tie == True:
			game_over = True
			winner = 0

def draw_game_over(winner):
	if winner == 1:
		end_text = "Player X wins!"
	if winner == 0:
		end_text = "It is a draw!"
	if winner == -1:
		end_text = "Player O wins!"

	end_img = font.render(end_text, True, blue)
	pygame.draw.rect(screen, green, (screen_width // 2 - 75, screen_height // 2 - 60, 154, 30))
	screen.blit(end_img, (screen_width // 2 - 70, screen_height // 2 - 55))

	again_text = 'Play again?'
	again_img = font.render(again_text, True, blue)
	pygame.draw.rect(screen, green, again_rect)
	screen.blit(again_img, (screen_width // 2 - 55, screen_height // 2 + 40))



run = True
while run:
	draw_board()
	draw_markers()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

		if game_over == False:
			if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
				clicked = True
			if event.type == pygame.MOUSEBUTTONUP and clicked == True:
				clicked = False
				pos = pygame.mouse.get_pos()
				cell_x = pos[0] // 100
				cell_y = pos[1] // 100
				if markers[cell_x][cell_y] == 0:
					markers[cell_x][cell_y] = player
					player *= -1
					check_game_over()

	if game_over == True:
		draw_game_over(winner)
		if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
			clicked = True
		if event.type == pygame.MOUSEBUTTONUP and clicked == True:
			clicked = False
			pos = pygame.mouse.get_pos()
			if again_rect.collidepoint(pos):
				game_over = False
				player = 1
				pos = (0,0)
				markers = []
				winner = 0
				for x in range (3):
					row = [0] * 3
					markers.append(row)

	pygame.display.update()

pygame.quit()
