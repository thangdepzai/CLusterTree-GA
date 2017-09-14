def InsertionSort(A):
    size = len(A)
    for i in range(1,size,1):
        last = A[i]
        j=i;
        while j>0 and A[j-1] >last:
            A[j] = A[j-1]
            j -= 1
        A[j] =last

A =[1,2,3,8,7,9,10,12,23,18,15,16,17,14]
#InsertionSort(A)
#print A

def SelectSort(A):
    n = len(A)
    for i in range(0,n-1,1):
        min =i
        for j in range(i+1,n,1):
            if A[j] < A[min]:
                min = j
        tmp = A[i]
        A[i] = A[min]
        A[min] = tmp
#SelectSort(A)
#print A

