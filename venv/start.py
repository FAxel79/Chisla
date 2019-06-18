import pygame, random
import matrix as M
import window as W
run = True
okno = W.Wind()
sleep = 1000
show = 1

a = 0
an = 0
sleep = 0

def get_matrix():
    a = M.Matr(12, 12, 9)
    an = a.x * a.y
    sleep = 25 * an
    return a,an,sleep

def draw_matr(win, matr):
    y = len(matr.matrica)
    x = len(matr.matrica[y-1])
    for i in range (y):
        for j in range(x):
            text = win.font.render(str(matr.matrica[i][j]), 0, (50, 80, 50))
            win.win.blit(text, (25*(j+1), 25*(i+1)))
    pass
def proverka (matr):
    s =[]
    for i in matr.matrica:
        for j in i:
            s.append(j)
    k = matr.n
    ss = []
    for h in range(k+1):
        ss.append(0)
    for t in s:
        ss[t] +=1

    ma = 0
    noo = 0
    for d in range(len(ss)):
        if ss[d] > ma:
            ma = ss[d]
            noo = d

    return (ss,noo)

a, an, sleep =get_matrix()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_SPACE]):
        a, an, sleep = get_matrix()
        show = 1

    pass
    if show == 1:
        draw_matr(okno, a)
        show = 0
        pygame.display.update()
        pygame.time.delay(sleep)
    elif show == 0:
        show = 2
        okno.win.fill((250,250,250))
        pygame.display.update()
        c = proverka(a)
        nam = int(input())
        if c[0][nam] == c[0][c[1]]:
            print(' Угадал')
        else:
            print("Неверно, максимум было цифр " + str(c[1]))
        print(c[0])
    pygame.display.update()

pass
pygame.quit()
