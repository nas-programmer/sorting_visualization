import pygame, sys, random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIDTH = 640
HEIGHT = 480
win_size = (WIDTH, HEIGHT)

pygame.init()

win = pygame.display.set_mode(win_size)
pygame.display.set_caption('Bubble Sort')
clock = pygame.time.Clock()

#width of the bars
n = 4

w = int(WIDTH/n)
h_arr = []
states = []

for i in range(w):
    #height of the bars
    height = random.randint(10, 450)
    h_arr.append(height)
    states.append(1)

counter = 0

while True:
    win.fill(BLACK)

    if counter < len(h_arr):
        for j in range(len(h_arr) - 1 - counter):
            if h_arr[j] > h_arr[j+1]:
                states[j] = 0
                states[j+1] = 0
                temp = h_arr[j]
                h_arr[j] = h_arr[j+1]
                h_arr[j+1] = temp
            else:
                states[j] = 1
                states[j+1] = 1
    else:
        print('Done')
    counter += 1

    if len(h_arr) - counter >= 0:
        states[len(h_arr) - counter] = 2

    for i in range(len(h_arr)):
        if states[i] == 0:
            color = (255, 0, 0)
        elif states[i] == 2:
            color = (0, 255, 0)
        else:
            color = WHITE
        pygame.draw.rect(win, color, pygame.Rect(int(i*n), HEIGHT - h_arr[i], n, h_arr[i]))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    clock.tick(20)
    pygame.display.flip()
