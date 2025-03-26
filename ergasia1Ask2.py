def findMissing(array):
    left = 0
    right = len(array)
    mid = 0
    while array[mid] != right or mid != left:
        mid = (left + right) // 2
        if mid + 1 >= array[mid]:
            left = mid
        else:
            if left == right == 0:
                return 1
            right = mid
    return array[mid] + 1


A = [1,2,3,5,6,7,8,9,10] #4 is missing
B = [1,2,3,4,5,7,8,9,10] #6 is missing
C = [1,2,3,4,5,6,7,8,9]  #10 is missing
D = [2,3,4,5,6,7,8,9,10] #1 is missing
E = [1,2,3,4,6,7,8,9,10] #5 is missing
F = [1,2,3,4,5,6,7,8,10] #9 is missing
G = [1,3,4,5,6,7,8,9,10] #2 is missing

print(findMissing(A), findMissing(B),findMissing(C),findMissing(D),findMissing(E),findMissing(F),findMissing(G))
