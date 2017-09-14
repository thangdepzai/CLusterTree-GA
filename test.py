"""
ROOT = 1
NUM_GROUP = 2
def DsKe(v,tree):
    if v == ROOT:
        return tree[0][ROOT]
    elif v in tree[0].keys():
        for i in range(1,NUM_GROUP):
            if v in L[i]:
                return tree[0][v]+tree[i][v]
    else:
        for i in range(1,NUM_GROUP):
            if v in L[i]:
                return tree[i][v]
            else:
                return []

            
L=[{1:[3],2:[4],3:[5]},{1:[4]}]
for i in range(6):
    print DsKe(i,L)
"""
import math
import random
"""
NUM_NODES =20

E= [{1,2},{1,3},{2,3},{2,4},{3,4},{3,5},{4,5},{5,6},{4,6}]
V=[1,2,3,4,5,6]
costs=[[0, 33, 17, 0, 0, 0],
      [33, 0, 18, 20, 0, 0],
      [17, 18, 0, 16, 4, 0],
      [0, 20, 16, 0, 9, 8],
      [0, 0, 4, 9, 0, 14],
      [0, 0, 0, 8, 14, 0]]
d=[0 for i in range(20)]
K=[0 for i in range(20)]
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
        if {u,i} in E:
            L1.append(i)
    return L1
            
        
def Dijkstra_Heap(E,V,s):
    global d,p,k
    for u in V:
        d[u-1] =float("inf")
        p[u-1] =0
        K[u-1]=0
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
        K[u-1] =1
        for v in Ke(u,E,V):
            if K[v-1]==0 and d[v-1]>d[u-1]+costs[u-1][v-1]:
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
# ------------------------prim-heap---------------------------------
def Prim_Heap(E,V,s):
    global d,p,k
    for u in V:
        d[u-1] =float("inf")
        p[u-1] =0
        K[u-1]=0
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
        K[u-1] =1
        for v in Ke(u,E,V):
            if K[v-1]==0 and d[v-1]> costs[u-1][v-1]:
                d[v-1]= costs[u-1][v-1]
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
tree2= Dijkstra_Heap(E,V,1)
tree= Prim_Heap(E,V,1)
print tree
print tree2
"""
NUM_GROUP =4
L=[[1],[2,3,5],[4,6,7],[8,9,10]]
tree =[150000,[[{1,5},{1,9},{3,6}],[{2,5},{3,5}],[{6,4},{7,4}],[{9,8},{9,10}]],[1,5,9,3,6],{0:1,1:5,2:6,3:9}]
def DsKe(v, tree, vex):
    L1 =[]
    for j in range(1,NUM_GROUP):
        if v in L[j]:
            for i in L[j]:
                if {v,i} in tree[j]:
                    L1.append(i)
            break
    if v in vex:
        for j in vex:
            if {v,j} in tree[0]:
                L1.append(j)
    return L1
print DsKe(1,tree[1], tree[2])
print DsKe(2,tree[1], tree[2])
print DsKe(3,tree[1], tree[2])
print DsKe(4,tree[1], tree[2])
print DsKe(5,tree[1], tree[2])
print DsKe(6,tree[1], tree[2])
print DsKe(7,tree[1], tree[2])
print DsKe(8,tree[1], tree[2])
print DsKe(9,tree[1], tree[2])
print DsKe(10,tree[1], tree[2])

"""
costs=[[0,6,7,8,9,10,11,12,13,14],
       [6,0,5,11,2,12,14,15,16,17],
       [7,5,0,7,3,8,9,10,11,12],
       [8,11,7,0,10,3,2,9,11,12],
       [9,2,3,10,0,11,9,13,14,15],
       [10,12,8,3,11,0,1,10,11,12],
       [11,14,9,2,9,1,0,9,8,11],
       [12,15,10,9,13,10,9,0,2,1],
       [13,16,11,11,14,11,8,2,0,1],
       [14,17,12,12,15,12,11,1,1,0]]
def MINIMUM_EDGE(list_vertex_1, list_vertex_2):
    MIN = 1000000
    k1= 0
    k2 = 0
    for i in list_vertex_1:
        for j in list_vertex_2:
            if costs[i-1][j-1] < MIN:
                MIN = costs[i-1][j-1]
                k1 = i
                k2 = j
    return [k1, k2]
def GroupEdgeConnect(edge):
    tmp = []
    for i in edge:
        for k in range(NUM_GROUP):
            if i in L[k]:
                tmp.append(k)
                break
    return tmp
def LocalSearch(ind):
    new_ind = ind[1]+[]
    vertexconnect = []
    trace = dict()
    new_ind[0] = []
    L1 = [[] for i in range(NUM_GROUP)]
    for i in ind[1][0]:
        tmp = GroupEdgeConnect(i)
        new_edge = MINIMUM_EDGE(L[tmp[0]], L[tmp[1]])
        new_ind[0].append(new_edge)
        for k in new_edge:
            if k in L[tmp[0]] and k not in L1[tmp[0]] :
                L1[tmp[0]].append(k)
            elif k in L[tmp[1]] and  k not in L1[tmp[1]] :
                L1[tmp[1]].append(k)
        for j in new_edge:
            if j not in vertexconnect:
                vertexconnect.append(j)
    for i in range(NUM_GROUP):
        trace[i] = random.choice(L1[i]);
    return [ new_ind, vertexconnect,trace]
tree1 =LocalSearch(tree)
print tree1
"""
