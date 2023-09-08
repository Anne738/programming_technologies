
a = int(input("input num -> "))

def num_minus (num):
    print(num)
    if num > 0:
        return num_minus(num-1)
    if num == 0:
        return 0  
    if num < 0:
        print("Число повинно бути натуральним")
        return 0

num_minus(a)    