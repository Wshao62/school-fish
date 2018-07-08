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


GPIO.setmode(GPIO.BCM)  # 選擇輸出腳位模式(BCM or BORAD)
GPIO.setup(IN1, GPIO.OUT)  # 設定輸出模式
GPIO.setup(IN2, GPIO.OUT)  # 設定輸出模式
try:

    for i in range(100):
        GPIO.output(IN1, True)
        GPIO.output(IN1, False)
        time.sleep(0.05)
    GPIO.output(IN2, True)
    GPIO.output(IN2, False)
    for i in range(100):
        GPIO.output(IN1, True)
        GPIO.output(IN1, False)
        time.sleep(0.05)
except:
    print("有問題")
finally:
    GPIO.cleanup()


# 指令樹查

# GPIO.PWM(LED_PIN, 50) #參數(腳位, 總時常50s)
# GPIO.PWM.start(0)配合上面使用 有start就要有stop()
