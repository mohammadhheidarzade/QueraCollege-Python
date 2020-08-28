import pygame
pygame.init()
screen = pygame.display.set_mode((300, 300))
screen.fill((255,255,255))
pygame.display.update()
size = 1
color = (0, 0, 0)

while True:
    pygame.event.pump()
    en = input().split()
    if en[0] == 'change':
        if en[1] == 'size':
            size = int(en[2])
        elif en[1] == 'color':
            color = (int(en[2]), int(en[3]), int(en[4]))
    elif en[0] == 'draw':
        if en[1] == 'line':
            pygame.draw.line(screen, color, (int(en[2]), int(
                en[3])), (int(en[4]), int(en[5])), size)
        elif en[1] == 'polygon':
            li = []
            print(len(en))
            for i in range(2, len(en), 2):
                print(i , i + 1)
                li.append((int(en[i]), int(en[i + 1])))
            print(li)
            pygame.draw.polygon(screen, color, li, size)
        elif en[1] == 'circle':
            pygame.draw.circle(screen,color,(int(en[2]) , int(en[3])) , int(en[4]) , size)
            pass
    else:
        break
    pygame.display.update()
    pygame.time.delay(200)
pygame.image.save(screen, 'draw.png')
