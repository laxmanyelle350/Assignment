height=int(input("enter the value:"))
def pyramid(height):
    for i in range(1,height+1):
        space=" "*(height-i)
        star="*"*(2*i-1)
        print(space+star)

pyramid(height)
            

    
word=input("enter the  value:")
patten="abc"
count= word.count(patten)
print(count)



num=int(input("enter the value:"))
for i in range(num):
    for j in range(num):
        if (i+j)%2==0:
            print("X",end=" ")
        else:
             print("O",end=" ")
    print()
    

        
        