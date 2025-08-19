

class linear_search:
    def __init__(self,array):
        self.array = array

    def search(self,target):
        for i in range(len(self.array)):
            if self.array[i] == target:
                return i
        return None


numbers = list(map(int, input("Enter the array : ").split()))
linear_search_obj = linear_search(numbers)
target = int(input("Enter the value to search : "))
result = linear_search_obj.search(target)

if result is not None:
    print("Value found at index : ", result)
else:
    print("Value not found.")