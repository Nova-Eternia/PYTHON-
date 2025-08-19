class min_max:
    def __init__(self, array):
        self.array = array

    def find_min(self):
        return min(self.array) if self.array else None

    def find_max(self):
        return max(self.array) if self.array else None

numbers = list(map(int , input("Enter the array : ").split()))
min_max_obj = min_max(numbers)
print("Minimum : ", min_max_obj.find_min())
print("Maximum : ", min_max_obj.find_max())
