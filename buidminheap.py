from random import randint

def parent(i):
    x = i + 1
    y = x//2
    return y-1

def lchild(i):
    x = i + 1
    y = x*2
    return y-1

def rchild(i):
    x = i + 1
    y = x*2 + 1
    return y-1

def Min_Heapify(A,i,n):
    "n heapsize A"
    l = lchild(i)
    r = rchild(i)
    if l<n and A[l]<A[i]:
        minimum = l
    else:
        minimum =i
    if r <n and A[r]<A[minimum]:
        minimum = r
    if minimum!=i:
        tmp = A[minimum]
        A[minimum] =A[i]
        A[i] = tmp
        Min_Heapify(A,minimum,n)
def Build_Min_Heap(A):
    n=len(A)
    for i in range(n//2-1,-1,-1):
        Min_Heapify(A,i,n)
        
    

l = [40,30,65,25,35,50,76,10,28,27,33,36,34,48,60,68,80,69]
"""
dl = int(input())

for i in range (0, dl):
    x = int(randint(1,100)) 
    l.append(x)
"""
print len(l)
print l
Build_Min_Heap(l)
print l
"""
#l=[36, 58, 29, 10, 77, 96, 10, 22, 22, 29, 91, 29, 51, 88, 91, 67, 42, 33, 16, 7, 33, 64, 33, 23, 34, 51]
def bkop(l):
        j = 0
        for i in range(1, len(l)):
                if l[i] < l[parent(i)]:
                        l[i], l[parent(i)] = l[parent(i)], l[i]
                        j = j+1
                if j != 0:
                        bkop(l)
bkop(l)
print l

"""
