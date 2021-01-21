inputList = [int(i) for i in input('Enter values... ').split()]
length = len(inputList)

inputList.sort()
print('Sorted Array: ', inputList)

search = eval(input('Enter number to be searched: '))
first = 0
last = length - 1

def binarySearch(li,first,last,search):
    middle = int((first + last) / 2)
    if first <= last:
            if inputList[middle] == search:
                return middle
            elif inputList[middle] > search:
                return binarySearch(li,first,middle-1,search)
            else:
                return binarySearch(li,middle+1,last,search)
    else: 
        return -1

pos = binarySearch(inputList,first,last,search)

if pos == -1:
    print('Element ', search, 'not found -> STATUS: -1')
else:
    print('Element ', search, 'found at index', pos)
