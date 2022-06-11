import os
import time


def execute(cmd):
    adbstr = 'adb shell {}'.format(cmd)
    os.system(adbstr)


def click0():
    execute("input tap 578 2136")


def click1():
    execute("input tap 250 1500")


def click2():
    execute("input tap 540 1500")


def click3():
    execute("input tap 850 1500")


def click4():
    execute("input tap 250 1700")


def click5():
    execute("input tap 540 1700")


def click6():
    execute("input tap 850 1700")


def click7():
    execute("input tap 250 1900")


def click8():
    execute("input tap 540 1900")


def click9():
    execute("input tap 858 1883")


if __name__ == '__main__':
    startNum = 984200
    endNum = 990000
    sleepFlag = 0
    while startNum < endNum:
        a = list(str(startNum))
        print(a)
        for i in a:
            if i == '0':
                click0()
            elif i == '1':
                click1()
            elif i == '2':
                click2()
            elif i == '3':
                click3()
            elif i == '4':
                click4()
            elif i == '5':
                click5()
            elif i == '6':
                click6()
            elif i == '7':
                click7()
            elif i == '8':
                click8()
            else:
                click9()
        time.sleep(1)
        sleepFlag = sleepFlag + 1
        while sleepFlag == 5:
            time.sleep(30)
            sleepFlag = 0
        startNum = startNum + 1
