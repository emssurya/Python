import array as arr

numbers = arr.array('i',[])

n=int(input("Enter how many numbers you want in the array:"))

for i in range(n):
    num = int(input(f"Enter element {i+1}:"))
    numbers.append(num)

print("\nArray elements are:",numbers)

print("First element:", numbers[0])
print("Last element:", numbers[-1])

print("length of array:",len(numbers))

numbers[0] = numbers[0] + 10
print("After modifying first element:",numbers)
numbers.append(100)
print("After append 100:",numbers)
numbers.remove(numbers[1])
print("After removing second element:",numbers)
numbers.reverse()
print("Reversed Elements:",numbers)
numbers.append(5)
print(numbers)
print(numbers.count(5))
    
    
