i = 0
n = 5


while i < n:
    print("External loop")
    j = 0
    k = 9
    while j < k:
        print("Inner loop")
        j += 1
    i += 1
