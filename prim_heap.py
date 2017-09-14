import math
NUM_NODES =20

E= [(1,5),(1,2),(1,4),(5,3),(5,4),(2,4),(2,6),(2,3),(4,7),(7,6)]
V=[1,2,3,4,5,6,7]
costs=[[0, 5, 0, 7, 1, 0, 0],
      [5, 0, 3, 6, 0, 4, 0],
      [0, 3, 0, 0, 10, 0, 0],
      [7, 6, 0, 0, 2, 0, 8],
      [1, 0, 10, 2, 0, 0, 0],
      [0, 4, 0, 0, 0, 0, 9],
      [0, 0, 0, 8, 0, 9, 0]]
d=[0 for i in range(20)]
k=[0 for i in range(20)]
p=[0 for i in range(20)]
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

def Min_Heapify(A,i,n,pos):
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
        tmp= pos[i]
        pos[i]= pos[minimum]
        pos[minimum] =tmp
        Min_Heapify(A,minimum,n,pos)
def Build_Min_Heap(A,pos):
    n=len(A)
    for i in range(n//2-1,-1,-1):
        Min_Heapify(A,i,n,pos)
def Extract_Min(Q,pos):
    n= len(Q)
    k= pos[0]
    Q[0]=Q[n-1]
    tmp=pos[n-1]
    pos[n-1] =pos[0]
    pos[0] =tmp
    del Q[n-1]
    Min_Heapify(Q,0,n-1,pos)
    return k
def Decrease_Key(Q,i,k,pos):
    Q[i] =k
    while i>0:
        if Q[parent(i)]>Q[i]:
            c = parent(i)
            tmp = Q[c]
            Q[c] =Q[i]
            Q[i] = tmp
            tmp= pos[i]
            pos[i]= pos[c]
            pos[c] =tmp
            i = c
        else:
            break
def Ke(u,E,V):
    L1 =[]
    for i in V:
        if (u,i) in E or (i,u) in E:
            L1.append(i)
    return L1
            
        
def Dijkstra_Heap(E,V,s):
    global d,p,k
    for u in V:
        d[u-1] =float("inf")
        p[u-1] =0
        k[u-1]=0
    d[s-1] = 0
    Q =[0 for i in V]
    j=0
    pos =dict()
    for i in V:
        Q[j] = d[i-1]
        pos[j] = i
        j +=1
    Build_Min_Heap(Q,pos)
    while len(Q)!=0:
        u=Extract_Min(Q,pos)
        k[u-1] =1
        for v in Ke(u,E,V):
            if k[v-1]==0 and d[v-1]>d[u-1]+costs[u-1][v-1]:
                d[v-1]= d[u-1]+costs[u-1][v-1]
                p[v-1]= u
                for i in pos.keys():
                    if pos[i] == v:
                        break
                Decrease_Key(Q,i,d[v-1],pos)
    tree=[]
    T=V+[]
    T.remove(s)
    for i in T:
        tree.append({p[i-1],i})
    return tree


k= Dijkstra_Heap(E,V,1)
print k

        
