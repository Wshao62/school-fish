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


def showFont(text, x, y):
    global canvas
    text = font.render(text, 1, (255, 0, 0))
    canvas.blit(text, (x, y))


block = (0, 0, 0)
locals_x = 400
locals_y = 300


def move_D(x, y):  # 往下
    for i in range(20):
        canvas.fill(block)
        showFont("魚", x, y + i*12)
        pygame.display.update()
        time.sleep(0.1)


def move_U(x, y):  # 往上
    for i in range(20):
        canvas.fill(block)
        showFont("魚", x, y - i*12)
        pygame.display.update()
        time.sleep(0.1)


def move_L(x, y):  # 往右
    for i in range(20):
        canvas.fill(block)
        showFont("魚", x + i*12, y)
        pygame.display.update()
        time.sleep(0.1)


def move_R(x, y):  # 往左
    for i in range(20):
        canvas.fill(block)
        showFont("魚", x - i*12, y)
        pygame.display.update()
        time.sleep(0.1)


def move_RU(x, y):  # 往左上
    for i in range(20):
        canvas.fill(block)
        showFont("魚", x - i*12, y + i*12)
        pygame.display.update()
        time.sleep(0.1)


def move_LU(x, y):  # 往右上
    for i in range(20):
        canvas.fill(block)
        showFont("魚", x + i*12, y - i*12)
        pygame.display.update()
        time.sleep(0.1)


def move_RD(x, y):  # 往左下
    for i in range(20):
        canvas.fill(block)
        showFont("魚", x - i*12, y + i*12)
        pygame.display.update()
        time.sleep(0.1)


def move_RD(x, y):  # 往右下
    for i in range(20):
        canvas.fill(block)
        showFont("魚", x + i*12, y + i*12)
        pygame.display.update()
        time.sleep(0.1)


move_U(400, 300)
move_D(400, 300)
move_L(400, 300)
move_R(400, 300)
move_RU(400, 300)
move_LU(400, 300)
move_RD(400, 300)
move_LD(400, 300)
