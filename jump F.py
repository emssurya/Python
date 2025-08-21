for num in range(1, 10):
    if num==3:
        print("Skiping number 3 using continue")
        continue
    if num==5:
       print("breaking the loop at number 5")
       break
    
    if num==7:
        pass
        print("this is pass, number 7(won't be reached due to break)")

    print("Current number:",num)

    
