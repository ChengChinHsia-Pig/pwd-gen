import random, string
import time
import os
txtwriter=open("TWHTele0X.txt","w", encoding='utf-8')
codes = ["02", "03", "037", "04", "049", "05", "6", "7", "8", "89", "82", "826", "836"]
print("密碼字典生成中...")
      
for n in range(int(100000000)):
   #尾數亂數生成
   possiblecode = random.randint(1000000, 99999999)
   code = random.choice(codes)
   #連結組合
   txtwriter.write(str(code))
   txtwriter.write(str(possiblecode))
   txtwriter.write("\n")
   print(possiblecode)
txtwriter.close()
