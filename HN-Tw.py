import random, string
import time
import os
txtwriter=open("TWHTele.txt","w", encoding='utf-8')

print("密碼字典生成中...")
      
for n in range(int(100000000)):
   #尾數亂數生成
   possiblecode = random.randint(1000000, 99999999)
   #連結組合
   txtwriter.write(str(possiblecode))
   txtwriter.write("\n")
   print(possiblecode)
txtwriter.close()
