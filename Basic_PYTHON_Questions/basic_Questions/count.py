
class count:
    def __init__(self,array):
        self.array = array

    def count_elements(self,target):
        return self.array.count(target) if target in self.array else None


number = list(map(int, input("Enter the array : ").split()))
count_obj = count(number)
target = int(input("Enter the value to count : "))
result = count_obj.count_elements(target)

if result is not None:
    print("Count of", target, "is:", result)
else:
    print("Value not found.")