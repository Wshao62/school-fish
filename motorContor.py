# import自動修復 程式碼片段Stste
lestModName = ""
while 1:
    try:
        import sys
        import os
        sys.path.append(sys.path[0] + '/mods/')  # 將自己mods的路徑加入倒python lib裡面
        # 要import的東西放這下面
        import time
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
        import RPi.GPIO as GPIO
        del lestModName
        break
# import自動修復 程式碼片段


class Step_motor():

    def __init__(self, In1, In2):
        GPIO.setmode(GPIO.BCM)  # 選擇輸出腳位模式(BCM or BORAD)
        GPIO.setup(In1, GPIO.OUT)  # 設定輸出模式
        GPIO.setup(In2, GPIO.OUT)  # 設定輸出模式
        self.In1 = In1
        self.In2 = In2

    def run_clockwise(self, turns):

        for i in range(turns):
            GPIO.output(self.In1, True)
            GPIO.output(self.In1, False)

    def run_counter_clockwise(self, turns):

        GPIO.output(self.In2, True)

        for i in range(turns):
            GPIO.output(self.In1, True)
            GPIO.output(self.In1, False)

        GPIO.output(self.In2, False)


class DC_motor():

    def __init__(self, In1, In2, ENA):
        self.In1 = In1
        self.In2 = In2
        self.ENA = ENA

    def run_clockwise(self, sec):

        GPIO.output(self.In1, True)
        GPIO.output(self.In2, False)
        GPIO.output(self.ENA, True)
        time.sleep(sec)
        GPIO.output(self.ENA,False) # 關掉馬達