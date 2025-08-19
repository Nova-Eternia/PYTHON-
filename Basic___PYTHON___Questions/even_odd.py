
class even_odd:
    def __init__(self,array):
        self.array = array
    
    def count_EvenOdd(self):
        count_even = 0
        count_odd = 0
        for i in range(len(self.array)):
            if self.array[i] % 2 == 0:
                count_even += 1
            else:
                count_odd += 1

numbers = list(map(int, input("Enter the array : ").split()))
eo = even_odd(numbers)
eo.count_EvenOdd()
print("Even count : ", count_even)
print("Odd count : ", count_odd)