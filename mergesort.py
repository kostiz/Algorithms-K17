def merge_sort(array):
    #print("array:",array)
    lengh = len(array)

    # base case
    if lengh <= 1:
        return array

    # cutting array in half
    left = []
    right = []
    for i in range(1,lengh+1):
        if i <= lengh/2:
            left.append(array[i -1])
        else:
            right.append(array[i -1])
            
    #print("Left:",left)
    #print("Right:",right)

    # recursion yummyyyy
    left = merge_sort(left)
    right = merge_sort(right)
    
    return merge(left,right)

def merge(left,right):
    total_lenght = len(left) + len(right)
    #print("MERGING:", left , right, total_lenght)
    mergedArray = []
    leftpos = 0
    rightpos = 0
    for i in range(0, total_lenght):
        #print("i:", i, mergedArray, leftpos, rightpos)
        # makes sure it doesn't try to read an element that doesn't exist
        if leftpos  == len(left):
            mergedArray.append(right[rightpos])
            rightpos = rightpos + 1
            continue
        if rightpos == len(right):
            mergedArray.append(left[leftpos])
            leftpos = leftpos + 1
            continue
        # compares the 2 lowest (or only) elements
        if left[leftpos] > right[rightpos]:
            mergedArray.append(right[rightpos])
            rightpos = rightpos + 1
            continue
        else:
            mergedArray.append(left[leftpos])
            leftpos = leftpos + 1
            continue
    
    return mergedArray;


# Main program

arr = [10,5,7,3,1,-2,1]
sorted_arr = merge_sort(arr)

# printing messages
print("Original Array:", arr)
print("Sorted Array:  ", sorted_arr)

# End of Main
