
class replace:
    def __init__(self,array):
        self.array = array

    def replace_element(self,old_value,new_value):
        for i in range(len(self.array)):
            if self.array[i] == old_value:
                self.array[i] = new_value
        return self.array

number = list(map(int, input("Enter the array : ").split()))
replace_obj = replace(number)
old_value = int(input("Enter the value to replace : "))
new_value = int(input("Enter the new value : "))
result = replace_obj.replace_element(old_value,new_value)
print("Updated array : ", result)