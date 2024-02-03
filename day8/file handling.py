import os
import time



try:
   f= open("hellos.txt","x")
#    f.write("overide\n")
#    print(f.read(5))
#    text=f.readlines()
#    print(text[-1])
   f.close()
   print("it will be deleted soon")
   time.sleep(3)
   os.remove('hellos.txt')

except Exception as e:
    print (e)
    
