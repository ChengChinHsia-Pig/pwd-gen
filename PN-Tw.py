import random, string
import time
import os
txtwriter=open("TWTele.txt","w", encoding='utf-8')

print("密碼字典生成中...")
      
for n in range(int(1000000000)):
   #尾數亂數生成
   possiblecode = random.randint(900000000, 999999999)
   #連結組合
   txtwriter.write(str(0))
   txtwriter.write(str(possiblecode))
   txtwriter.write("\n")
   print(f"0{possiblecode}")
txtwriter.close()
