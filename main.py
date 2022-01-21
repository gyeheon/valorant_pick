import pyautogui
import time
import keyboard
import os
import random

dic = {
    1: (627,917),
    2: (716,915),
    3: (788,923),
    4: (885,917),
    5: (951,917),
    6: (1027,918),
    7: (1132,920),
    8: (1203,913),
    9: (1288,913),
    10: (629,1003),
    11: (711,999),
    12: (798,1000),
    13: (876,1003),
    14: (962,1000), 
    15: (1035,999),
    16: (1122,999),
    17: (1203,1003),
    18: (1294,1003)
}

def pick(agent):
    t_end = time.time() + 10
    t_start = time.time()
    while time.time() < t_end:
        print(f"실행 중")
        if keyboard.read_key() == "space":
            pyautogui.moveTo(dic[agent][0], dic[agent][1])
            pyautogui.click()
            pyautogui.moveTo(959, 811)
            pyautogui.click()
        os.system('cls')

def valpick():
    agent = input("agent number: ")
    if agent.isdecimal():
        agent = int(agent)

        if ( agent > 0 and agent < 19 ):            
            os.system('cls')
            pick(agent)
    if agent == 'r':
        pick(random.randint(1,18))
        

def random_map():
    for i in range(random.randint(20,50)):
        map = ['스플릿','바인드','헤이븐','어센트','아이스박스','브리즈','프랙처']
        r_map = random.choice(map)
        os.system('cls')
        print(r_map)
    os.system('pause')

def help():
    print("pick\n\n요원배치\n1\t2\t3\t4\t5\t6\t7\t8\t9\n10\t11\t12\t13\t14\t15\t16\t17\t18\n\n픽 하고자 하는 요원의 번호를 입력하면 10초 동안 활성화 됩니다. (r을 입력 시 랜덤 선택) \n활성화 상태일 때 스페이스 바를 누르고 있으면 자동으로 픽합니다.\n")
    os.system('pause')

def main():
    print("Valorant 4.01 이후 제작")
    os.system('pause')
    while 1:
        os.system('cls')
        menu = input("1.pick | 2.random map | 3.help: ")
        if menu == '1':
            os.system('cls')
            valpick()
        if menu == '2':
            os.system('cls')
            random_map()
        if menu == '3':
            os.system('cls')
            help()


main()