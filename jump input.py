n= int (input("Enter how many numbers you want to check:"))

for i in range(1,n + 1 ):
    num= int(input(f"Enter number {i}:"))
    
    if num==3:
        print("Skiping number 3 using continue")
        continue
    
    if num==5:
       print("breaking the loop at number 5")
       break
    
    if num==7:
        pass
        print("this is pass, number 7")

    print("You entered:",num)
