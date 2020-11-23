import pygame, sys, random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIDTH = 720
HEIGHT = 400
win_size = (WIDTH, HEIGHT)

pygame.init()

win = pygame.display.set_mode(win_size)
pygame.display.set_caption('Cocktail Sort')
clock = pygame.time.Clock()

#width of the bars
n = 4

w = int(WIDTH/n)
h_arr = []
states = []

for i in range(w):
    #height of the bars
    height = random.randint(10, 400)
    h_arr.append(height)
    states.append(1)

start = 0
end = len(h_arr) - 1
swapped = True

def maps(num, in_min, in_max, out_min, out_max):
  return (num - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

flag = False

while True:
    win.fill(BLACK)

    if flag:
        if swapped:
            swapped = False
            for i in range(start, end):
                if h_arr[i] > h_arr[i+1]:
                    h_arr[i], h_arr[i+1] = h_arr[i+1], h_arr[i]
                    states[i], states[i+1] = 0, 0
                    swapped = True
                states[i], states[i+1] = 1, 1
        
            if not swapped:
                continue

            swapped = False

            end -= 1
            for i in range(end - 1, start - 1, -1):
                if h_arr[i] > h_arr[i+1]:
                    h_arr[i], h_arr[i+1] = h_arr[i+1], h_arr[i]
                    states[i], states[i+1] = 0, 0
                    swapped = True
                states[i], states[i+1] = 1, 1

            start += 1



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
