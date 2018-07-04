# import自動修復 程式碼片段Stste
lestModName = ""
while 1:
    try:
        import sys
        import os
        sys.path.append(sys.path[0] + '/mods/')  # 將自己mods的路徑加入倒python lib裡面
        # 要import的東西放這下面
        import RPi.GPIO as GPIO
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
        del lestModName
        break
# import自動修復 程式碼片段
IN1 = 2
IN2 = 3
ENA = 4

GPIO.setmode(GPIO.BCM) # 選擇輸出腳位模式(BCM or BORAD)
GPIO.setup(ENA, GPIO.OUT)# 設定輸出模式
GPIO.setup(IN1, GPIO.OUT)# 設定輸出模式
GPIO.setup(IN2, GPIO.OUT)# 設定輸出模式

# init
GPIO.output(IN1,False)
GPIO.output(IN2,False)
GPIO.output(ENA,False)
try:
    # 正轉
    GPIO.output(IN1,True)
    GPIO.output(IN2,False)
    GPIO.output(ENA,True)
    time.sleep(5)
    GPIO.output(ENA,False) # 關掉馬達
    # 反轉設置
    GPIO.output(IN1,False)
    GPIO.output(IN2,True)
    time.sleep(0.1)
    GPIO.output(ENA,True)
    time.sleep(5)
except:
    print("有問題")
finally:   
    GPIO.cleanup()


# 指令樹查

# GPIO.PWM(LED_PIN, 50) #參數(腳位, 總時常50s)
# GPIO.PWM.start(0)配合上面使用 有start就要有stop()