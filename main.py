import random, string
import time
import os
txtwriter=open("TWID.txt","w", encoding='utf-8')

print("密碼字典生成中...")
      
for n in range(int(1000000000)):
   #尾數亂數生成
   possiblecode = "%02d"%random.randint(100000000, 999999999)
   region = chr(random.randint(ord('A'), ord('Z')))
   #連結組合
   txtwriter.write(region)
   txtwriter.write(str(possiblecode))
   txtwriter.write("\n")
   print(f"{region}{possiblecode}")
txtwriter.close()
