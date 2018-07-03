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

print(background)


def showFont(text, x, y):
    global canvas
    text = font.render(text, 1, (255, 0, 0))
    canvas.blit(text, (x, y))


block = (0, 0, 0)


x = 400
y = 300
movex = 0
movey = 0
def move():
    input
while True:
    # 游戏主循环
    for event in pygame.event.get():
        if event.type == QUIT:
            # 接收到退出事件后退出程序
            exit()
        if event.type==KEYDOWN:
            if event.key==K_LEFT:
                movex=-1
            if event.key==K_RIGHT:
                movex=+1
            elif event.key==K_UP:
                movey=-1
            elif event.key==K_DOWN:
                movey=+1
        if event.type==KEYUP:
            if event.key==K_LEFT:
                movex=0
            if event.key==K_RIGHT:
                movex=0
            elif event.key==K_UP:
                movey=0
            elif event.key==K_DOWN:
                movey=0
    x += movex
    y += movey
    canvas.blit(background, (0, 0))
    canvas.blit(fish, (x, y))
    pygame.display.update()
