from time import *
import random as r

def mistake(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i]!=usertest[i]:
                error = error+1
        except:
            error = error+1
    return error        

def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s 
    time_R = round(time_delay,2)
    speed = len(userinput)/time_R
    return round(speed)



test = ["Keep your face always toward the sunshine, and shadows will fall behind you.","You make a choice: continue living your life feeling muddled in this abyss of self-misunderstanding, or you find your identity independent of it. You draw your own box.","My name is Isha Gupta"]
test1 = r.choice(test)
print("*****Typing Speed Calculator*****")
print(test1)
print()
print()
time_1 = time()
testinput=input("Enter : ")
time_2 = time()

print('Speed : ',speed_time(time_1,time_2,testinput),"words/sec")
print("Error : ",mistake(test1,testinput))


