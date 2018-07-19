# import自動修復 程式碼片段Stste
lestModName = ""
while 1:
    try:
        import sys
        import os
        sys.path.append(sys.path[0] + '/mods/')  # 將自己mods的路徑加入倒python lib裡面
        # 要import的東西放這下面
        import time
        import pygame
        from pygame.locals import *
        from pygame import event
        import threading
    except (ModuleNotFoundError, ImportError):  # python import error
        err = str(sys.exc_info()[1])[17:-1]
        if (lestModName != err):
            print("缺少mod: " + err + " 正在嘗試進行安裝")
            os.system("pip install " + err)
            lestModName = err
        else:
            print("無法修復import問題 請人工檢查", "mod name: " + err)
            sys.exit()
    else:
        del lestModName
        break
# import自動修復 程式碼片段

# 視窗大小.
canvas_width = 800
canvas_height = 600

# 初始.
pygame.init()
# 顯示Title.
pygame.display.set_caption(u"釣魚遊戲")
canvas = pygame.display.set_mode((canvas_width, canvas_height))
font = pygame.font.SysFont('simhei', 18)
background = pygame.image.load(sys.path[0] + "/img/normal.jpg").convert()
fish = pygame.image.load(sys.path[0] + "/img/2.jpg").convert()
powd = 0


def showFont(text, x, y):
    global canvas
    text = font.render(text, 1, (255, 0, 0))
    canvas.blit(text, (x, y))


def blend_color(color1, color2, blend_factor):
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    r = r1 + (r2 - r1) * blend_factor
    g = g1 + (g2 - g1) * blend_factor
    b = b1 + (b2 - b1) * blend_factor

    return int(r), int(g), int(b)


def edge_checkge(point, movex, movey):

    if point[0] == 0 or point[0] == canvas_width:
        if point[0] == 0:
            point[0] += 1
        else:
            point[0] -= 1
    else:
        point[0] += movex
    if point[1] == 0 or point[1] == canvas_height:
        if point[1] == 0:
            point[1] += 1
        else:
            point[1] -= 1
    else:
        point[1] += movey
    return point


def powd_checkge(powd, powdcount):
    if powd > 599:
        powd = 599
    elif powd < 1:
        powd = 1
    else:
        powd += powdcount
    return powd


block = (0, 0, 0)

point = [400, 300]
movex = 0
movey = 0
powdcount = 0


def move():
    input


while True:
    # 游戏主循环

    for event in pygame.event.get():
        if event.type == QUIT:
            # 接收到退出事件后退出程序
            exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                movex = -1
            if event.key == K_RIGHT:
                movex = +1
            elif event.key == K_UP:
                movey = -1
            elif event.key == K_DOWN:
                movey = +1
            if event.key == K_d:
                powdcount = +1
            elif event.key == K_a:
                powdcount = -1
        if event.type == KEYUP:
            if event.key == K_LEFT:
                movex = 0
            if event.key == K_RIGHT:
                movex = 0
            elif event.key == K_UP:
                movey = 0
            elif event.key == K_DOWN:
                movey = 0
            if event.key == K_d:
                powdcount = 0
            elif event.key == K_a:
                powdcount = 0

    # 拉力條
    powd = powd_checkge(powd, powdcount)
    my_rect3 = Rect(50, 0, powd, 20)
    # 魚 座標
    point = edge_checkge(point, movex, movey)

    # 繪圖區
    canvas.blit(background, (0, 0))
    canvas.blit(fish, point)
    factor = powd/600
    powdcolr = blend_color([0, 255, 0], [231, 99, 20], factor)
    pygame.draw.rect(canvas, powdcolr, my_rect3)
    # 寫字區
    showFont("拉力:" + str(powd), 0, 0)
    pygame.display.update()
"""
for event in pygame.event.get():
        if event.type == QUIT:
            # 接收到退出事件后退出程序
            exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                movex = -1
            if event.key == K_RIGHT:
                movex = +1
            elif event.key == K_UP:
                movey = -1
            elif event.key == K_DOWN:
                movey = +1
            if event.key == K_d:
                powdcount = +1
            elif event.key == K_a:
                powdcount = -1
        if event.type == KEYUP:
            if event.key == K_LEFT:
                movex = 0
            if event.key == K_RIGHT:
                movex = 0
            elif event.key == K_UP:
                movey = 0
            elif event.key == K_DOWN:
                movey = 0
            if event.key == K_d:
                powdcount = 0
            elif event.key == K_a:
                powdcount = 0

"""
