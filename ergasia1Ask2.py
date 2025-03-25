def findMissing(array):
    full_array = array + [0]
    print(full_array)
    for i in range(0,len(full_array)):
        if i+1 != full_array[i]:
            return i+1


A = [1,2,3,5,6,7,8,9,10]
B = [1,2,3,4,5,7,8,9,10]
C = [1,2,3,4,5,6,7,8,9]
D = [2,3,4,5,6,7,8,9,10]
E = [1,2,3,4,6,7,8,9,10]

print(findMissing(A),findMissing(B),findMissing(C),findMissing(D),findMissing(E))
