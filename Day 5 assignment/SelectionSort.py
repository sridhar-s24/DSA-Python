#selection sort

inp = [int(i) for i in input('Enter values... ').split()]
length = len(inp)

for i in range(0, length - 1):
    pos = i
    for j in range(i+1, length):
        if inp[pos] > inp[j]:
            inp[pos],inp[j] = inp[j],inp[pos]
print (inp)
