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


class StepMotor():
    #           =====init 函數=====
    # 滑軌　約　5500步　到底
    # In1 　 脈波輸出腳　   接PUL
    # In2 　 正反轉控制腳   接DIR
    # left 　右邊微動開關   靠近馬達的微動開關　高電位智能
    # right　左邊微動開關　 遠離馬達的微動開關　高電位智能
    def __init__(self, In1, In2, left, right):
        GPIO.setmode(GPIO.BCM)  # 選擇輸出腳位模式(BCM or BORAD)
        GPIO.setup(In1, GPIO.OUT)  # 設定輸出模式
        GPIO.setup(In2, GPIO.OUT)  # 設定輸出模式

        GPIO.setup(left, GPIO.IN)
        GPIO.setup(right, GPIO.IN)

        #GPIO.add_event_detect(left, GPIO.RISING, callback=self.leftCellBack)
        #GPIO.add_event_detect(right, GPIO.RISING, callback=self.rightCellBack)
        self.In1 = In1
        self.In2 = In2
        self.left = left
        self.right = right
        self.maxstep = 5500
        self.Last_degree = 0

        # self.run_Zone()

    def run_degree(self, degree):
        if degree>100 or degree<0:
            return -1
        tempDegree = degree-self.Last_degree
        self.Last_degree = degree
        if tempDegree > 0:
            self.run_clockwise(tempDegree*55)
        elif tempDegree <0:
            self.run_counter_clockwise(-tempDegree*55)
        else:
            pass
        return 1

    def run_clockwise(self, turns):  # 向右

        turns = int(turns)
        GPIO.output(self.In2, False)
        time.sleep(0.0001)
        for i in range(turns):
            if(GPIO.input(self.right) == 1):
                print('右開關觸發 座標到100')
                self.Last_degree = 100
                return -1
            GPIO.output(self.In1, False)
            time.sleep(0.0001)
            GPIO.output(self.In1, True)

    def run_counter_clockwise(self, turns):  # 向左

        turns = int(turns)
        GPIO.output(self.In2, True)
        time.sleep(0.0001)
        for i in range(turns):
            if((GPIO.input(self.left) == 1)):
                print('左開關觸發 座標到0')
                self.Last_degree = 0
                return -1
            GPIO.output(self.In1, False)
            time.sleep(0.0001)
            GPIO.output(self.In1, True)

        GPIO.output(self.In2, False)

    def run_Zone(self):  # 回到中心
        self.run_counter_clockwise(55500)
        self.run_clockwise(2250)
        self.Last_degree = 50

    def motorTest(self):
        self.run_clockwise(1100)
        self.run_counter_clockwise(1100)
        self.run_Zone()
        

    def leftCellBack(self,a):
        print('left中斷',a)
        pass

    def rightCellBack(self,a):
        print('right中斷',a)
        pass


class DcStepMotor():
    #           =====init 函數=====
    # 滑軌　約　1100步　到底
    # In1 　 脈波輸出腳　   接PUL
    # In2 　 正反轉控制腳   接DIR
    def __init__(self, In1, In2):
        GPIO.setmode(GPIO.BCM)  # 選擇輸出腳位模式(BCM or BORAD)
        GPIO.setup(In1, GPIO.OUT)  # 設定輸出模式
        GPIO.setup(In2, GPIO.OUT)  # 設定輸出模式

        self.In1 = In1
        self.In2 = In2

    def run(self, turns):
        GPIO.output(self.In1, True)
        for i in range(turns):
            GPIO.output(self.In1, False)
            time.sleep(0.001)
            GPIO.output(self.In1, True)


class DCmotor():

    def __init__(self, In1, In2, ENA):

        GPIO.setmode(GPIO.BCM)  # 選擇輸出腳位模式(BCM or BORAD)
        GPIO.setup(ENA, GPIO.OUT)  # 設定輸出模式
        GPIO.setup(In1, GPIO.OUT)  # 設定輸出模式
        GPIO.setup(In2, GPIO.OUT)  # 設定輸出模式
        GPIO.output(In1, False)
        GPIO.output(In2, False)
        GPIO.output(ENA, False)

        self.In1 = In1
        self.In2 = In2
        self.ENA = ENA

    def run_clockwise(self, sec):

        GPIO.output(self.In1, True)
        GPIO.output(self.In2, False)
        GPIO.output(self.ENA, True)
        time.sleep(sec)
        GPIO.output(self.ENA, False)  # 關掉馬達

    def run_counter_clockwise(self, sec):

        GPIO.output(self.In1, True)
        GPIO.output(self.In2, False)
        GPIO.output(self.ENA, True)
        time.sleep(sec)
        GPIO.output(self.ENA, False)  # 關掉馬達
