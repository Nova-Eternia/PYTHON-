

arr = list(map(int, input("Enter numbers separated by space: ").split()))
x = int(input("Enter the sum to find pairs for: "))
for i in arr:
    z = x - i
    if z in arr:
        print(i,z)