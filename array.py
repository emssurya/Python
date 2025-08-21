#Pythone programe using list an a array

#Create an array(list)
numbers=[10,20,30,40,50]
#Display the array
print("Array element are:",numbers)
#access element
print("First element:",numbers[0])
print("Last element:",numbers[-1])
#modify element
numbers[2]=35
print("After modifying:",numbers)
#add new element
numbers.append(60)
print("After appending:",numbers)
#remove element
numbers.remove(20)
print("After removing 20:",numbers)
#Length of array
print("Length of array:",len(numbers))
