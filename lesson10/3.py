numbers = [
    ["футболка", 2],
    ["шорты", 4],
    ["кофта", 6],
]
i = 0
n = len(numbers)
while i < n:
    arr = numbers[i]
    j = 0
    k = len(arr)
    print(arr)
    while j < k:
        print(arr[j])
        j += 1
    i += 1
#    i  j       0      1
#    0 ["футболка", 2],
#    1 ["шорты", 4],
#    2 ["кофта", 6],
# i -> 0,1,2
# j -> 0,1