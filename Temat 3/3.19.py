x = int(input("Enter the dog's age in human years: "))
y = 0
for i in range(1,x+1):
    if i <=2:
        y = y + 10.5
    else:
        y = y + 4
        
print(f"The dog's age in dog’s years is {y} years.")