import time

timestamp=time.strftime('%H:%M:%S')
# print(timestamp)

timestamp1=time.strftime('%H')
# print(timestamp1)

if (int(timestamp1) < 12 ):
    print("Good morning sir")

elif (int(timestamp1) < 16 ): 
    print("Good afternoon sir")

elif (int(timestamp1) < 22 ):      
    print("Good evening sir")

else :
    print("Good night sir")    


