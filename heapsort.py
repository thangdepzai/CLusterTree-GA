def lchild(i):
    x = i + 1
    y = x*2
    return y-1

def rchild(i):
    x = i + 1
    y = x*2 + 1
    return y-1

def Max_Heapify(A,i,n):
    "n heapsize A"
    l = lchild(i)
    r = rchild(i)
    if l<n and A[l]>A[i]:
        largest = l
    else:
        largest =i
    if r <n and A[r]>A[largest]:
        largest = r
    if largest!=i:
        tmp = A[largest]
        A[largest] =A[i]
        A[i] = tmp
        Max_Heapify(A,largest,n)
def Build_Max_Heap(A):
    n=len(A)
    for i in range(n//2-1,-1,-1):
        Max_Heapify(A,i,n)

def HeapSort(A):
    Build_Max_Heap(A)
    n=len(A)
    for i in range(n-1,0,-1):
        tmp = A[0]
        A[0] =A[i]
        A[i] = tmp
        Max_Heapify(A,0,i)
l = [87,43,68,6,77,33,9,11,19,99,6,23,89,2,14,1,5,27,35,7,42,12,71,3,67,22]
HeapSort(l)
print len(l)
print l
