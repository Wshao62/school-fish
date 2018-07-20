# import自動修復 程式碼片段Stste
lestModName = ""
while 1:
    try:
        import sys
        import os
        sys.path.append(sys.path[0] + '/mods/')  # 將自己mods的路徑加入倒python lib裡面
        # 要import的東西放這下面
        import time
        import random
        import pygame
        from pygame.locals import *
        from pygame import event
        import threading
        import motorContor
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
til_background = pygame.image.load(sys.path[0] + "/img/123.jpg").convert()
fish = pygame.image.load(sys.path[0] + "/img/flash.png").convert_alpha()

# fish= pygame.transform.scale(fish,(200,160))
# 遊戲用變數
powd = 0
point = []
movex = 0
movey = 0
powdcount = 0


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

    if point[0] <= 0 or point[0] >= canvas_width - fish.get_rect()[2]:
        if point[0] <= 0:
            point[0] += 1
        else:
            point[0] -= 1
    else:
        point[0] += movex
    if point[1] <= 0 or point[1] >= canvas_height - fish.get_rect()[3]:
        if point[1] <= 0:
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


def fish_trus(fish, movex, movey):

    if movex > 0:
        if movey < 0:
            fish = pygame.transform.rotate(fish, 315)
        elif movey > 0:
            fish = pygame.transform.rotate(fish, 225)
        else:
            fish = pygame.transform.rotate(fish, 270)
    if movex < 0:
        if movey < 0:
            fish = pygame.transform.rotate(fish, 45)
        elif movey > 0:
            fish = pygame.transform.rotate(fish, 135)
        else:
            fish = pygame.transform.rotate(fish, 90)
    if movex == 0:
        if movey > 0:
            fish = pygame.transform.rotate(fish, 180)

    return fish


def fish_size(fish, point):
    if point[1] == 300:
        x = 1
    else:
        x = point[1]/300
    fish = pygame.transform.scale(fish,(int(65*x),int(116*x)))
    return fish

def win_check(powd):
    win_time=10
    count=0
    while True:
        if powd > 500 and powd < 600:
            count += 1
            if count >= win_time:
                print("you win")
        else:
            count=0

def fish_Game(point, fish, powd, movex, movey, canvas, powdcount):
    # 遊戲用的變數
    temp_fish=fish_trus(fish, movex, movey)
    point=[400, 300]
    wincount = 0
    # 硬體 變數處始畫

    while True:
        # 游戏主循环
        # movex = random.randint(-1, 1)
        # movey = random.randint(-1, 1)
        for event in pygame.event.get():
            if event.type == QUIT:
                # 接收到退出事件后退出程序
                exit()
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    movex=-1
                if event.key == K_RIGHT:
                    movex=+1
                elif event.key == K_UP:
                    movey=-1
                elif event.key == K_DOWN:
                    movey=+1
                if event.key == K_d:
                    powdcount=+2
            if event.type == KEYUP:
                if event.key == K_LEFT:
                    movex=0
                if event.key == K_RIGHT:
                    movex=0
                elif event.key == K_UP:
                    movey=0
                elif event.key == K_DOWN:
                    movey=0
                if event.key == K_d:
                    powdcount=0
        # 拉力條判斷
        if powd >= 600:
            showFont("掉魚線斷了，本次遊戲結束", 350, 300)
            pygame.display.update()
            time.sleep(3)
            break
        elif powd>500 and powd <600:
            wincount += 1
            if wincount>500:
                showFont("你贏了 獲得一條魚XD", 350, 300)
                pygame.display.update()
                time.sleep(3)
                break
        else:
            wincount == 0
        # 拉力條
        powd=powd_checkge(powd, powdcount-1)
        my_rect3=Rect(50, 0, powd, 20)
        # 魚 座標
        point=edge_checkge(point, movex, movey)
        
        # 繪圖區
        canvas.blit(background, (0, 0))
        if movex or movey:
            temp_fish=fish_trus(fish, movex, movey)
        temp_fish = fish_size(temp_fish, point)
        canvas.blit(temp_fish, point)

        factor=powd/600
        powdcolr=blend_color([0, 255, 0], [255, 60, 20], factor)
        pygame.draw.rect(canvas, powdcolr, my_rect3)
        # 寫字區
        showFont("拉力:" + str(powd), 0, 0)
        pygame.display.update()

def mainWindows():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
            # 接收到退出事件后退出程序
                exit()
            if event.type == KEYDOWN:
                fish_Game(point, fish, powd, movex, movey, canvas, powdcount)
        canvas.blit(til_background, (0, 0))
        showFont("案任意鍵開始遊戲", 300, 300)
        pygame.display.update()


if __name__ == '__main__':
    mainWindows()
"""
if powd >= 600:
            showFont("掉魚線斷了，本次遊戲結束", 350, 300)
            pygame.display.update()
            time.sleep(3)
            break
"""