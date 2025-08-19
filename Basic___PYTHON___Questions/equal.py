array1 = list(map(int, input("Enter numbers for array1 separated by space: ").split()))
array2 = list(map(int, input("Enter numbers for array2 separated by space: ").split()))

if array1 == array2:
    print("Both arrays are equal.")
else:
    print("Arrays are not equal.")