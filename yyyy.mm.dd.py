import random, string
import time
import os
txtwriter=open("Birth.txt","w", encoding='utf-8')

print("密碼字典生成中...")
      
for n in range(int(1000000000)):
   #尾數亂數生成
   year = random.randint(1930, 2022)
   month = "%02d"%random.randrange(1, 13)
   day = "%02d"%random.randrange(1, 32)
   #連結組合
   txtwriter.write(str(year))
   txtwriter.write(str(month))
   txtwriter.write(str(day))
   txtwriter.write("\n")
   print(f"{year}{month}{day}")
txtwriter.close()
