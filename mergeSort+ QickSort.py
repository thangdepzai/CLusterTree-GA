# merge 2 array A[first:mid] and A[mid:last]
def Merge(A,left, mid, right):
    i = left
    j = mid+1
    B =[]
    while i<=mid and j<=right:
        if A[i] < A[j]:
            B.append(A[i])
            i +=1
        else:
            B.append(A[j])
            j += 1
    while i<=mid:
        B.append(A[i])
        i +=1
    while j<= right:
        B.append(A[j])
        j += 1
    k=0
    for i in range(left, right+1,1):
        A[i] =B[k]
        k += 1

def MergeSort(A, left, right):
    if left <right:
        mid =(left+right)//2
        MergeSort(A, left, mid)
        MergeSort(A, mid+1, right)
        Merge(A, left, mid, right)

A =[23,-20,24,-13,28,26,25,21]
"""
print A
MergeSort(A,0,len(A)-1)
print A
"""


def Partition(A, L, R):
    i= L+1
    j = R
    p = A[L]
    while i<=j:
        while i <= R:
            if A[i] <= p:
                i +=1
            else:
                break
        while j>= L :
            if A[j] >p:
                j -= 1
            else:
                break
        if i <j:
            tmp= A[j]
            A[j]= A[i]
            A[i]= tmp
            i +=1
            j -=1
            
    tmp= A[j]
    A[j]= A[L]
    A[L]= tmp
    return j
        
def Quick_Sort(A,left, right):
    if left < right:
        pivot = Partition(A, left, right)
        if left < pivot-1:
            Quick_Sort(A, left, pivot-1)
        if right > pivot+1:
            Quick_Sort(A, pivot+1, right)
print len(A)

Quick_Sort(A,0,len(A)-1)
print A
    
    
