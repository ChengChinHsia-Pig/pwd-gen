import random, string
import time
import os
txtwriter=open("Number.txt","w", encoding='utf-8')

print("密碼字典生成中...")
      
for n in range(int(1000000000)):
   txtwriter.write(str(n))
   txtwriter.write("\n")
   print(n)
txtwriter.close()
