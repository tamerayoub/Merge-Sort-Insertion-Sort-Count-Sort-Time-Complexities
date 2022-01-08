import time
# Ichiro Part 1


def mergeSort(L, ascending=True):
    outcomelist = []

    if len(L) == 1:
        return L
    # The middle of the arrays
    mid = len(L) // 2

    nList1 = mergeSort(L[:mid])

    nList2 = mergeSort(L[mid:])

    x, y = 0, 0

# Comparing the two list values
    while x < len(nList1) and y < len(nList2):
        # If List 1 is less than list 2 increment y if not increment x (viceversa)
        if nList1[x] < nList2[y]:  # desending change to "<"
            # adding the respected values to outcomelist via List1&List2
            outcomelist.append(nList2[y])
            y = y + 1
        else:
            outcomelist.append(nList1[x])
            x = x + 1

# Combining both of the List to the outcomelist
    outcomelist = outcomelist + nList1[x:]
    outcomelist = outcomelist + nList2[y:]

# Another option to reverse/or descend the the order
    if ascending == True:
        return outcomelist
    else:
        outcomelist.reverse()
        return outcomelist


# Ignore this for computing time, just testing to make sure it works
list = [3, 3, 4, 1, 5, 9, 7, 6]
print(list)
print(mergeSort(list, True))  # sort in ascending order
print()
i = random.sample(range(1, 100), 10)
print(i)
print(mergeSort(i, True))  # sort in ascending order


# Karter Part 2

# Takes parameter A, which is a sorted list.
def InsertionSort(A, sortAscending):
    if sortAscending == True:
        # starting at 1 through the length of A, but NOT to its upper-bound allowing 1 to n - 1
        for i in range(1, len(A)):
            key = A[i]  # element that will be inserted each time we loop through A
            j = i
            while j > 0 and A[j - 1] > key:
                A[j] = A[j - 1]
                j -= 1
                A[j] = key
    else:
        for i in range(1, len(A)):
            key = A[i]
            j = i
            while j > 0 and A[j - 1] < key:
                A[j] = A[j - 1]
                j -= 1
                A[j] = key


def InputAssignment():  # Assigns globally three lists with desired input for use with InsertionSort
    # Input 1, 10,000
    global input1
    #input1 = list(range((10000 + 1)) )
    input1 = [2, 4, 3, 1, 8, 7, 5, 9, 6, 10]
    # Input 2, 100,000
    global input2
    #input2 = list(range((100000 + 1)) )
    input2 = [2, 4, 3, 1, -8, -7, 5, -9, 6, -10]
    # Input 3, 1000,000
    global input3
    #input3 = list(range((1000000 + 1)) )
    input3 = [1, 2, 2, 3, 4, -4, 5, 6, 5, 10]
    # NOTE: Commented out listrange to make sure unsorted lists work first before sharing for time effeciency check.
    # NOTE: global so I don't make the variables function-only(InsertionSort can't see them)


InputAssignment()
print("Case A: Ascending Sort")
InsertionSort(input1, True)
InsertionSort(input2, True)
InsertionSort(input3, True)
# I think it looks nice side by side with top down comparison
print(input1, input2, input3)
InputAssignment()  # Re-assign values for Case B
print("Case B: Descending Sort")
InsertionSort(input1, False)
InsertionSort(input2, False)
InsertionSort(input3, False)
print(input1, input2, input3)


# Arnavee Part 3

# Defining count_sort and assigning the size and the output of the program

def count_Sort(arr, ascending=True):
    size = len(arr)
    output = [0] * size

    count = [0] * 10  # Intializing the count

# Storing the count of each element in the array
    for i in range(0, size):
        count[arr[i]] += 1

# storing the cumulative values

    for i in range(1, 10):
        count[i] += count[i - 1]

# searching the index of each element and then putting them in output array

    i = size - 1
    while i >= 0:
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1

    for i in range(0, size):
        arr[i] = output[i]

    data = [4, 2, 2, 8, 3, 3, 1]
    count_Sort(data)
    print("Array in ascending order: ")
    print(data)

    if ascending == True:
        return arr
    else:
        arr.reverse()
        return arr


# Tamers Part 5
List10000asc = [i for i in range(10000)]
List10000desc = [i for i in range(10000, 0, -1)]

List100000asc = [i for i in range(100000)]
List100000desc = [i for i in range(100000)]

List1000000asc = [i for i in range(1000000)]
List1000000desc = [i for i in range(1000000, 0, -1)]


t = time.process_time()
# replace this line with appropriate function name
a = count_Sort(List1000000asc, False)
elapsed_time = time.process_time() - t
print(elapsed_time)  # Note down this time in the table
