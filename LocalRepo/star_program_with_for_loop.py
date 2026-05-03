'''
* 
* * 
* * * 
* * * *
'''
def first_piraymid():
    for i in range(1,5,1):
        print("* "*i)
    
def second_piramid():
    for i in range(5,0,-1): #range(start,end,increment)
        print("*"*i)
second_piramid()
print("#"*25)
first_piraymid()

