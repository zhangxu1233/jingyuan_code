import time
import random
output=[0,0,0,0]

def addition():
    choice=random.randint(1, 5)
    if choice==1:
        while (output[0] + output[1] + output[2] >= 24 or output[0] + output[1] + output[2] <= 14):
            output[0]=random.randint(0, 9)
            output[1]=random.randint(0, 9)
            output[2]=random.randint(0, 9)
        output[3]=24 - (output[0] + output[1] + output[2])
    elif choice==2:
        #TODO
        while (output[choice] + output[choice + 1] <  15):
        
            choice = random.randint(0, 3)
            output[choice] = random.randint(0, 3) + 6
            output[(choice + 1) % 4] = random.randint(0, 3) + 6
        
        output[(choice + 2) % 4] = 24 - (output[choice] + output[choice + 1])
        output[(choice + 3) % 4] = random.randint(0, 9)
        
    elif choice==3:
        choice = random.randint(0, 1)#choice in [0,1]
        if (choice == 0):
        
            choice = random.randint(0, 3)#choice in [0,3]
            output[choice] = 1
            x1 = choice
            while (choice == x1):
            
                choice = random.randint(0, 3)
            
            output[choice] = random.randint(0, 9)
            x2 = choice
            while (choice == x1 and choice == x2):
            
                choice = random.randint(0, 3)
            
            if (output[x2] < 5):
            
                while (24 - 10 - output[x2] - output[choice] > 9):
                
                    output[choice] = random.randint(0, 9)
                
                
            
            else :
                #TODO
                output[choice] = (random.randint(0, (24 - 10 - output[x2]-1))  ) % 10#choice a number in [0,24-10-output[x2]]
            
            x3 = choice
            choice = 0
            while (choice == x1 and choice == x2 and choice == x3):
            
                choice = random.randint(0, 3)
            
            output[choice] = 24 - 10 - output[x2] - output[x3]
        
        else:
            choice = random.randint(0, 3)#choice in [0,3]
            output[choice] = 2
            x1 = choice
            while (choice == x1):
            
                choice = random.randint(0, 3)
            
            x2 = choice
            while (choice == x1 and choice == x2):
            
                choice = random.randint(0, 3)
            
            x3 = choice
            while (choice == x1 and choice == x2 and choice == x3):
            
                choice = random.randint(0, 3)
            
            output[x2] = random.randint(0, 4)
            output[x3] = random.randint(0, 4)
            while (output[x2] + output[x3] > 4):
            
                output[x2] = random.randint(0, 4)
                output[x3] = random.randint(0, 4)
            
            output[choice] = 4 - output[x2] - output[x3]
        
    elif choice==4:
        output[0] = random.randint(0, 9)
        output[1] = random.randint(0, 9)
        output[2] = random.randint(0, 9)
        output[3] = random.randint(0, 9)

        choice = random.randint(0, 1) % 2#choice in [0,1]
        if (choice == 0):#1_ + x
        
            choice = random.randint(0, 3) % 4#choice in [0,3]
            output[choice] = 1
            x1 = choice
            while (choice == x1):
            
                choice = random.randint(0, 3)
            
            output[choice] =random.randint(0, 4) + 5
            x2 = choice
            while (choice == x1 or choice == x2):
            
                choice = random.randint(0, 3)
            
            output[choice] = 24 - 10 - output[x2]
        
        else:#2_ + x
        
            choice = random.randint(0, 3)#choice in [0,3]
            output[choice] = 2
            x1 = choice
            while (choice == x1):
            
                choice = random.randint(0, 3)
            
            output[choice] = random.randint(0, 3)
            x2 = choice
            while (choice == x1 or choice == x2):
            
                choice = random.randint(0, 3)
            
            output[choice] = 4 - output[x2]

    else:
        choice = random.randint(0, 3)
        output[choice] = 1
        x1 = choice
        while (choice == x1):
        
            choice = random.randint(0, 3)
        
        output[choice] = 1
        x2 = choice
        while (choice == x1 or choice == x2):
        
            choice = random.randint(0, 3)
        
        output[choice] = random.randint(0, 4)
        x3 = choice
        choice = 0
        while (choice == x1 or choice == x2 or choice == x3):
        
            choice +=1
        
        output[choice] = 4 - output[x3]
        

def subtraction():

    choice = random.randint(0, 1)
    if (choice == 0):#2 - 2
    
        minuend = random.randint(34, 99)#in [34,99]
        subtrahend = minuend - 24
        choice = random.randint(0, 3)
        output[choice] = minuend // 10
        x1 = choice
        while (choice == x1):
        
            choice =  random.randint(0, 3)
        
        output[choice] = minuend % 10
        x2 = choice
        while (choice == x1 or choice == x2):
        
            choice =  random.randint(0, 3)
        
        output[choice] = subtrahend // 10
        x3 = choice
        choice = 0
        while (choice == x1 or choice == x2 or choice == x3):
        
            choice +=1
        
        output[choice] = subtrahend % 10
    
    else:#2 - 1
    
        output[0] =  random.randint(0, 9)
        output[1] = random.randint(0, 9)
        output[2] = random.randint(0, 9)
        output[3] = random.randint(0, 9)
        minuend = random.randint(0, 4)+24#in [24,33]
        subtrahend = minuend - 24
        choice = random.randint(0, 3)
        output[choice] = minuend // 10
        x1 = choice
        while (choice == x1):
        
            choice = random.randint(0, 3)
        
        output[choice] = minuend % 10
        x2 = choice
        while (choice == x1 or choice == x2):
        
            choice = random.randint(0, 3)
        
        output[choice] = subtrahend
    

def multiplication():




    output[0] = random.randint(0, 9)
    output[1] = random.randint(0, 9)
    output[2] = random.randint(0, 9)
    output[3] = random.randint(0, 9)
    choice = random.randint(0, 5)
    if (choice == 0):#2 * 2 * 2 * 2
    
        output[0] = 2
        output[1] = 2
        output[2] = 2
        output[3] = 2
        choice = random.randint(0, 3)
        output[choice] = 3
    
    elif (choice == 1):#2 * 3 * 4
    
        choice = random.randint(0, 3)
        output[choice] = 2
        x1 = choice
        while (choice == x1):
        
            choice = random.randint(0, 3)
        
        output[choice] = 3
        x2 = choice
        while (choice == x1 or choice == x2):
        
            choice = random.randint(0, 3)
        
        output[choice] = 4
    
    elif (choice == 2):#2 * 2 * 6
    
        choice = random.randint(0, 3)
        output[choice] = 2
        x1 = choice
        while (choice == x1):
        
            choice = random.randint(0, 3)
        
        output[choice] = 2
        x2 = choice
        while (choice == x1 or choice == x2):
        
            choice = random.randint(0, 3)
        
        output[choice] = 6
    
    elif (choice == 3):#12 * 2
    
        choice = random.randint(0, 3)
        output[choice] = 1
        x1 = choice
        while (choice == x1):
        
            choice = random.randint(0, 3)
        
        output[choice] = 2
        x2 = choice
        while (choice == x1 or choice == x2):
        
            choice = random.randint(0, 3)
        
        output[choice] = 2
    
    elif (choice == 4):#24 * 1
    
        choice = random.randint(0, 3)
        output[choice] = 2
        x1 = choice
        while (choice == x1):
        
            choice = random.randint(0, 3)
        
        output[choice] = 4
        x2 = choice
        while (choice == x1 or choice == x2):
        
            choice = random.randint(0, 3)
        
        output[choice] = 1
    
    else:#4 * 6
    
        choice = random.randint(0, 3)
        output[choice] = 4
        x1 = choice
        while (choice == x1):
        
            choice = random.randint(0, 3)
        
        output[choice] = 6
    


def division():

    
    
    choice = random.randint(0, 1)
    if (choice == 0):#x * 24, x in [1,4]
    
        output[0] = random.randint(0, 9)
        output[1] = random.randint(0, 9)
        output[2] = random.randint(0, 9)
        output[3] = random.randint(0, 9)
        
        choice = random.randint(0, 3)
        output[choice] = random.randint(0, 3) + 1
        x1 = choice
        while (choice == x1):
        
            choice = random.randint(0, 3)
        
        output[choice] = (output[x1] * 24) // 10
        x2 = choice
        while (choice == x1 or choice == x2):
        
            choice = random.randint(0, 3)
        
        output[choice] = output[x1] * 24 % 10
    
    else:#x * 24, x in [5,9]
    
        choice = random.randint(0, 3)
        output[choice] = random.randint(0, 4) + 5
        x1 = choice
        while (choice == x1):
        
            choice = random.randint(0, 3)
        
        output[choice] = output[x1] * 24 // 100
        x2 = choice
        while (choice == x1 or choice == x2):
        
            choice = random.randint(0, 3)
        
        output[choice] = output[x1] * 24 // 10 % 10
        x3 = choice
        choice = 0
        while (choice == x1 or choice == x2 or choice == x3):
        
            choice +=1
        
        output[choice] = output[x1] * 24 % 10
    


if __name__=='__main__':
    print("Hello World")
    choice = 0
    choice=random.randint(1, 4)
    
    
    if choice==1:
        addition()
        print("+")
    elif choice==2:
        subtraction()
        print("-")
    elif choice==3:
        multiplication()
        print("*")
    else:
        division()
        print("/")
        
    print(str(output[0])+"|"+str(output[1])+"|"+str(output[2])+"|"+str(output[3]))
