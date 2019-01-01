f=0
kel=0

def cel2f(temp):
    global f
    f=(temp*9/5)+32 #f is farenheit unit
    print(f)
   
   
   
def cel2k(temp):
    global kel
    kel=temp+273 #kel in kelvin unit
    print(kel)
   
def tempmenu():
    print("ENTER TEMP")
    temp=int(input())
    print("1. for  TEMP IN C  TO FARENHEIT")
    print("2. for  TEMP IN C  KELVIN")
    print("3. for  display in list")  #theyll ask you to print this in a 'list' data type,
    print("4. for  exit")
   
    while 1:
        print("enter choice")
        ch=int(input())
        if(ch==1):
            cel2f(temp) #function that converts your entered C to F
        elif(ch==2):
            cel2k(temp) #function that converts your entered C to K
        elif(ch==3):
            a=["the temp in C:",temp,"to F is",f,"the temp in K is",kel]
            print(a)
        else :
            print("program successfully terminated")
            exit()   
                
       
tempmenu() 
