

array1 = list(map(int, input("Enter numbers for array1 separated by space: ").split()))

array2 = array1[1:] + array1[:1]
array3 = array1[-1:] + array1[:-1]

print("Array after left shift:", array2)
print("Array after right shift:", array3)

