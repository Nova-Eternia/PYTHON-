numbers = list(map(int, input().split()))
num_avg = sum(numbers) / len(numbers) if numbers else 0
print("Average : ", num_avg)



# class array_average:
#     def __init__(self, array):
#         self.array = array

#     def calculate_average(self):
#         return sum(self.array) / len(self.array) if self.array else 0

# array_avg = array_average(list(map(int, input("Enter numbers separated by space: ").split())))
# print("Average : ", array_avg.calculate_average())