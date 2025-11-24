import random
num = random.randint(1,10)
gusses = 1


def start():
    global gusses
    # num = random.randint(1,10)
    n = int(input("ENTER THE NUMBER FROM 0 TO 10 :"))

    if(n<num):
        print("TRY AGAIN...YOUR NUMBER IS LESS THAN RANDOM NUMBER 😁")
        print(f"RANDOM NUMBER IS : {num}")
        print(f"YOUR NUMBER IS : {n}")
        gusses = gusses + 1
        start()
    elif(n>num):
        print("TRY AGAIN...YOUR NUMBER IS GREATER THAN RANDOM NUMBER 🥶")    
        print(f"RANDOM NUMBER IS : {num}")
        print(f"YOUR NUMBER IS : {n}")
        gusses = gusses + 1
        start()
        
    else:
        print(f"CONGRATULATIONS YOU WON!!!!! THE CORRECT NUMBER IS : {n}  in attemept 🎉🎉")  
        print(f"{gusses} attempt ")    
start()