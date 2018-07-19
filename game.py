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


class Fish_Game():
    def __init__(self):
        # 視窗用變數
        self.canvas_width = 800
        self.canvas_height = 600
        pygame.init()
        pygame.display.set_caption(u"釣魚遊戲")
        self.canvas = pygame.display.set_mode(
            (self.canvas_width, self.canvas_height))
        # 字形
        self.font = pygame.font.SysFont('simhei', 18)
        # 圖片載入
        self.background = pygame.image.load(
            sys.path[0] + "/img/normal.jpg").convert()
        self.fish = pygame.image.load(
            sys.path[0] + "/img/flash2.png").convert_alpha()
        # 遊戲用變數
        self.powd = 0
        self.fishPoint = [400, 300]
        self.movex = 0
        self.movey = 0
        self.powdcount = 0
    # 在螢幕上顯示字
    def showFont(self, text, x, y):
        global canvas
        text = self.font.render(text, 1, (255, 0, 0))
        self.canvas.blit(text, (x, y))
    # 漸變色處理
    def blend_color(self, color1, color2, blend_factor):
        r1, g1, b1 = color1
        r2, g2, b2 = color2
        r = r1 + (r2 - r1) * blend_factor
        g = g1 + (g2 - g1) * blend_factor
        b = b1 + (b2 - b1) * blend_factor

        return int(r), int(g), int(b)
    # 邊緣檢測
    def edge_checkge(self, point, movex, movey):

        if point[0] <= 0 or point[0] >= self.canvas_width:
            if point[0] <= 0:
                point[0] += 1
            else:
                point[0] -= 1
        else:
            point[0] += movex
        if point[1] <= 0 or point[1] >= self.canvas_height:
            if point[1] <= 0:
                point[1] += 1
            else:
                point[1] -= 1
        else:
            point[1] += movey
        return point
    # 磅數檢測
    def powd_checkge(self, powd, powdcount):
        if powd > 599:
            powd = 599
        elif powd < 1:
            powd = 1
        else:
            powd += powdcount
        return powd
    # 魚圖片處理
    def fish_trus(self, fish, movex, movey):

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
    def gameState(self):
        
        temp_fish = self.fish_trus(self.fish, self.movex, self.movey)
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
                        print("11")
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
            # 拉力條判斷
            if self.powd >= 600:
                self.showFont("掉魚線斷了，本次遊戲結束", 350, 300)
                pygame.display.update()
                break

            # 拉力條
            self.powd = self.powd_checkge(self.powd, self.powdcount)
            my_rect3 = Rect(50, 0, self.powd, 20)
            # 魚 座標
            self.fishPoint = self.edge_checkge(self.fishPoint, self.movex, self.movey)

            # 繪圖區
            self.canvas.blit(self.background, (0, 0))
            if self.movex or self.movey:
                temp_fish = self.fish_trus(self.fish, self.movex, self.movey)
            self.canvas.blit(temp_fish, self.fishPoint)

            factor = self.powd/600
            powdcolr = self.blend_color([0, 255, 0], [255, 60, 20], factor)
            pygame.draw.rect(self.canvas, powdcolr, my_rect3)
            # 寫字區
            self.showFont("拉力:" + str(self.powd), 0, 0)
            pygame.display.update()
