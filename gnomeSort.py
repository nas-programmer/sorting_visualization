import pygame, sys, random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIDTH = 720
HEIGHT = 400
win_size = (WIDTH, HEIGHT)

pygame.init()

win = pygame.display.set_mode(win_size)
pygame.display.set_caption('Gnome Sort')
clock = pygame.time.Clock()

#width of the bars
n = 5

w = int(WIDTH/n)
h_arr = []
states = []

def maps(num, in_min, in_max, out_min, out_max):
  return (num - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

for i in range(w):
    #height of the bars
    height = random.randint(10, 380)
    h_arr.append(height)
    states.append(1)

counter, finish = 0, len(h_arr)

flag = False

while True:
    win.fill(BLACK)

    if flag:
        if counter < len(h_arr):
            if counter == 0 or h_arr[counter] >= h_arr[counter - 1]:
                states[counter], states[counter - 1] = 1, 1
                counter += 1
            else:
                h_arr[counter], h_arr[counter-1] = h_arr[counter-1], h_arr[counter] 
                states[counter], states[counter - 1] = 0, 0
                counter -= 1

        else:
            states[finish-1] = 2
            if finish > 0:
                finish -=1


    for i in range(len(h_arr)):
        # if states[i] == 0:
        #     color = (255, 0, 0)
        # elif states[i] == 2:
        #     color = (0, 255, 0)
        # else:
        #     color = WHITE
        h_ar = maps(h_arr[i], 0, 400, 20, 255)
        # gap = win.get_height() - h_arr[i]
        # pygame.draw.rect(win, (h_ar//4, h_ar, h_ar//2), pygame.Rect(int(i*n), gap//2, n, h_arr[i]))
        pygame.draw.rect(win, (h_ar//3, h_ar, h_ar//4), pygame.Rect(int(i*n), (HEIGHT - h_arr[i])//2, n, h_arr[i]))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                flag = True 
    
    clock.tick(60)
    pygame.display.flip()
