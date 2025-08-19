# numbers = map(int, input().split())
# total = sum(numbers)
# print("Total sum : ", total)

class numbers_sum:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_sum(self):
        return sum(self.numbers)

numbers_sum = numbers_sum([1, 2, 3, 4, 5])
print("Total sum : ", numbers_sum.calculate_sum())