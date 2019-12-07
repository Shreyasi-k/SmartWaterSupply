import RPi.GPIO as GPIO
import time, sys
 
#GPIO (BOARD / BCM)
t = 0
p = 2
q = 5
r = 9
s = 10
in4 = 16
inpt = 13
levelA = 20
levelB = 40
levelC = 60
levelD = 80
Total_liters = 0


GPIO.setmode(GPIO.BOARD)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(inpt, GPIO.IN)

rate_cnt = 0
tot_cnt = 0
minutes = 0
constant = 0.010
time_new = 0.0


n = int(input("Enter no. of members in the family:"))
print(n)
if(n > t):
    if(n <= p):              #caseA
        #-----flow sensor------
        print('class A Water Flow - Approximate')
        while True:
            time_new = time.time() + 60
            rate_cnt = 0
            while time.time() <= time_new:
                if GPIO.input(inpt)!= 0:
                    rate_cnt += 1
                    tot_cnt += 1
                try:
                   print(GPIO.input(inpt), end='')
                except KeyboardInterrupt:
                   print('\nCTRL C - Exiting nicely')
                   GPIO.cleanup()
                   sys.exit()
            minutes += 1
            print('\nLiters / min',round(rate_cnt * constant,4))
            print('Total liters', round(tot_cnt * constant,4))
            print('Time (min & clock) ', minutes, '\t', time.asctime(time.localtime()))
            Total_liters = tot_cnt * constant
        GPIO.cleanup()
        
            #   -----relay sensor-----
        if(Total_litres >= levelA):
            GPIO.output(in4, False)
            time.sleep(2)
            GPIO.output(in4, True)
            time.sleep(2)
          #  ---------------
        #-------------------
        print("180 to 200 Litres")
    elif(n <= q):              #caseB
        #-----flow sensor------
        print('class B Water Flow - Approximate')
        while True:
            time_new = time.time() + 60
            rate_cnt = 0
            while time.time() <= time_new:
                if GPIO.input(inpt)!= 0:
                    rate_cnt += 1
                    tot_cnt += 1
                try:
                   print(GPIO.input(inpt), end='')
                except KeyboardInterrupt:
                   print('\nCTRL C - Exiting nicely')
                   GPIO.cleanup()
                   sys.exit()
            minutes += 1
            print('\nLiters / min',round(rate_cnt * constant,4))
            print('Total liters', round(tot_cnt * constant,4))
            print('Time (min & clock) ', minutes, '\t', time.asctime(time.localtime()))
            Total_liters = tot_cnt * constant            
        GPIO.cleanup()    
            #   -----relay sensor-----
        if(Total_litres >= levelB):
            GPIO.output(in4, False)
            time.sleep(2)
            GPIO.output(in4, True)
            time.sleep(2) #  ---------------
        #-------------------
        print("200 to 450 Litres") 
    elif(n <= r):              #caseC
        #-----flow sensor------
        print('class C Water Flow - Approximate')
        while True:
            time_new = time.time() + 60
            rate_cnt = 0
            while time.time() <= time_new:
                if GPIO.input(inpt)!= 0:
                    rate_cnt += 1
                    tot_cnt += 1
                try:
                   print(GPIO.input(inpt), end='')
                except KeyboardInterrupt:
                   print('\nCTRL C - Exiting nicely')
                   GPIO.cleanup()
                   sys.exit()
            minutes += 1
            print('\nLiters / min',round(rate_cnt * constant,4))
            print('Total liters', round(tot_cnt * constant,4))
            print('Time (min & clock) ', minutes, '\t', time.asctime(time.localtime()))
            Total_liters = tot_cnt * constant
            
        GPIO.cleanup()
            #   -----relay sensor-----
        if(Total_litres >= levelC):
            GPIO.output(in4, False)
            time.sleep(2)
            GPIO.output(in4, True)
            time.sleep(2)
          #  ---------------
        #-------------------
        print("450 to 800 Litres") 
    elif(n <= s):              #caseD
        #-----flow sensor------
        print('class D Water Flow - Approximate')
        while True:
            time_new = time.time() + 60
            rate_cnt = 0
            while time.time() <= time_new:
                if GPIO.input(inpt)!= 0:
                    rate_cnt += 1
                    tot_cnt += 1
                try:
                   print(GPIO.input(inpt), end='')
                except KeyboardInterrupt:
                   print('\nCTRL C - Exiting nicely')
                   GPIO.cleanup()
                   sys.exit()
            minutes += 1
            print('\nLiters / min',round(rate_cnt * constant,4))
            print('Total liters', round(tot_cnt * constant,4))
            print('Time (min & clock) ', minutes, '\t', time.asctime(time.localtime()))
            Total_liters = tot_cnt * constant            
        GPIO.cleanup()
            #  -----relay sensor-----
        if(Total_litres >= levelD):
            GPIO.output(in4, False)
            time.sleep(2)
            GPIO.output(in4, True)
            time.sleep(2)
         #   ---------------
        #-------------------
        print("800 to 1500 Litres")
    else:
        print("nothing")
        
else:
    print("Enter valid no.")