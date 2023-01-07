import random 

def gen():
    code=[random.randint(0,9) for i in range(4)]
    print(f"Random code generated")
    return code

def check(code=[] , num=[]):
    res=[]
    ##check the values passed to the function
    #print (f"code={code} num={num}") 
    for i in range(1,11):
        ##iterates from 1 to 10
        try:
        ##get valid input
            print(f"Guess the correct num try {i}:")
            #num=list(map(int,input('Enter the four digit code ').split()))   ##type conversion with map
            num=[int(i) for i in input('Enter the four digit code ').split()] ##type conversion with list comprehension 
            ##check the input for debug
            #print(f"num = {num}")
            if len(num) == 1:
            ##if input is passed without spaces
                lst=[str(x) for x in num]
                num=[int(k) for j in lst for k in j]
                lst=[]
                #print(f"num verified={num}")
            ##check the iteration and the num                     
            # print(f"iteration {i} num = {num} ")
        except ValueError:
            print("please enter only positve integers from 0 to 9")
        else:
            ##check length of the digits
            if len(code) != len(num):
                print(f"Please enter only 4 digits")
                ##skip the iteration
                continue
            for j in range(len(code)):
                if num[j] in code:
                    ##check for the number match at the same pos and different pos
                    #print(f"num[j]= {num[j]} j= {j}")
                    if num[j] == code[j]:
                        res.append('R')
                    else:
                        res.append('Y')
                else:
                    res.append('B')
            print(f"result={res}")
            if num == code:
                print(f"Correct")
                ##answer is correct break
                break
            else:
                print("try again")
                #reset the value
                res=[]


# print(f"Guess the number!")
# check(gen())


