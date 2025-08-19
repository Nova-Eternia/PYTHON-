

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
num = int(input("Enter a number to check: "))

if num in numbers:
    print("YES")
else:
    print("NO")