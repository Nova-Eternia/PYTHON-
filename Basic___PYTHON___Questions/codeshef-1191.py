

# i have a string of "ssas" 
# each letter denotes one jewel, and the same letters denote the same colors
# of jewels, and the different letters denote the different colors of jewels.
# The cost of each jewel is 1. For 1 jewel of each color, there is additional one jewel of availability.
# generate the code

s = "ssas" 

jewel_count = {}
for char in s:
    jewel_count[char] = jewel_count.get(char, 0) + 1

total_cost = 0
for count in jewel_count.values():
    total_cost += count // 2 + 1

print(total_cost)


# second method:
T = int(input())

while T > 0:
    
    s = input()
    set_chars = set()
    list_chars = []
    total = 0

    for char in s:
        set_chars.add(char)
        list_chars.append(char)

    for char in set_chars:
        index = list_chars.count(char)
        if index % 2 == 0:
            total += (index//2)
        else:
            total += (index//2 + 1)

    print(total)
    
    T -= 1