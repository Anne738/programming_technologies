
a = int(input("input first num -> "))
b = int(input("input second num -> "))

def num_minus (num1, num2):
    print(num1)
    if num1 > num2:
        return num_minus(num1-1)
    if num1 == 0:
        return 0  
    if num1 < 0:
        print("Число повинно бути натуральним")
        return 0

num_minus(a)    
