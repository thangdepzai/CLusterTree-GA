import random
import time
import math
import sys
start_time = time.time()
random.seed(int(sys.argv[8]))
costs = [] # list gia trimmmm
TOADO = [] # list toa do diem
dem = 0

with open(sys.argv[1], 'r') as lines:# dem so thanh pho
    for line in lines:
        TOADO.append(line.split())
n = NUM_NODES = int(TOADO[0][0])
NUM_GROUP = int(TOADO[0][1])
ROOT = int(TOADO[1][0])
L = [[] for i in range(NUM_GROUP)]
for i in range(1,NUM_GROUP+1, 1):
	for j in range(len(TOADO[i])):
		L[i-1].append(int(TOADO[i][j]))
costs = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        costs[i][j] = int(round(math.sqrt((int(TOADO[i+NUM_GROUP+1][1])-int(TOADO[j+NUM_GROUP+1][ 1]))**2 +(int(TOADO[i+NUM_GROUP+1][2])-int(TOADO[j+NUM_GROUP+1][2]))**2), 0))
# ---------------------------------------------------------
d=[]
K=[]
p=[]
# ---------------------------------------------------------
# ham xay dung cay khung tu tap con


def subtree(ListNode):
    List = ListNode + []
    k = random.choice(List)
    edge = []
    vertex = [k]
    List.remove(k)
    while len(edge) < len(ListNode)-1:
        k = random.choice(List)
        List.remove(k)
        m = random.choice(vertex)
        vertex.append(k)
        edge.append({m, k})
    return edge
# ---------------------------------------------------------
#ham noi cac cay con

def connectsubtree():
    global L
    vertex = []
    trace =dict()
    for i in range(NUM_GROUP):
        k = random.choice(L[i])
        vertex.append(k)
        trace[i] = k
    tmp = subtree(vertex)
    return [tmp,vertex,trace]
# ---------------------------------------------------------
# ham tim duong path giua 2 diem tren cay
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
                    
        

def FindPathBFS(tree,vertex, start):
    global NUM_NODES
    queue = []
    truoc = [0 for i in range(NUM_NODES)]
    chuaxet = [1 for i in range(NUM_NODES)]
    queue.append(start)
    chuaxet[start-1] = 0
    while len(queue) != 0:
        p = queue.pop(0)
        L1= DsKe(p,tree,vertex)
        for u in L1:
            if chuaxet[u-1] == 1:
                truoc[u-1] = p
                queue.append(u)
                chuaxet[u-1] = 0
    return truoc
# ---------------------------------------------------------

#ham tinh trong so giua 2 diem tren cay
def C(start, finish, truoc):
    weight = 0
    j = finish
    while j != start:
        weight += costs[j-1][truoc[j-1]-1]
        j = truoc[j-1]
    return weight

# ham fitness
def fitness(tree,vertex):
    global dem
    weight = 0
    truoc = FindPathBFS(tree,vertex,ROOT)
    for i in range(1, NUM_NODES+1,1):
        if i !=ROOT:
            weight += C(ROOT, i,truoc)
    return weight

# -------------------------khoi tao ca the--------------------------------


def individual():
    global L
    tree = []
    tmp1 = connectsubtree()
    tree.append(tmp1[0])
    for i in range(1, NUM_GROUP):
        tmp = subtree(L[i])
        tree.append(tmp)
    return [fitness(tree, tmp1[1]),tree,tmp1[1],tmp1[2]]


# -----------------------tao quan the----------------------------------


def population(size):
    popul = []
    while len(popul) < size:
        ind = individual()
        if ind not in popul:
            popul.append(ind)
    return popul
# ------------------------dijkstra-heap---------------------------------
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
    global d,p,K
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
        L1 = Ke(u,E,V)
        for v in L1:
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
# ------------------------Prim-heap---------------------------------
def Prim_Heap(E,V,s):
    global d,p,K
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
        L1 = Ke(u,E,V)
        for v in L1:
            if K[v-1]==0 and d[v-1]>costs[u-1][v-1]:
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
# --------------------------lai ghep1-------------------------------



def crossover1(ind1,ind2):
    new = []
    global d,p,K,L
    d=[0 for i in range(NUM_NODES)]
    K=[0 for i in range(NUM_NODES)]
    p=[0 for i in range(NUM_NODES)]
    if random.random() <0.5:
        new.append(ind1[1][0])
        m = ind1[2]+[]
        trace = ind1[3]
    else:
        new.append(ind2[1][0])
        m = ind2[2]+[]
        trace = ind2[3]
    for i in range(1,NUM_GROUP):
        tmp = ind1[1][i]+ind2[1][i]
        new_graph = Prim_Heap(tmp,L[i], trace[i])
        new.append(new_graph)
    return [fitness(new,m), new, m,trace]
# --------------------------lai ghep2-------------------------------
def crossover2(ind1,ind2):
    new = []
    global d,p,K,L
    d=[0 for i in range(NUM_NODES)]
    K=[0 for i in range(NUM_NODES)]
    p=[0 for i in range(NUM_NODES)]
    if random.random() <0.5:
        new.append(ind1[1][0])
        m = ind1[2]+[]
        trace = ind1[3]
    else:
        new.append(ind2[1][0])
        m = ind2[2]+[]
        trace = ind2[3]
    for i in range(1,NUM_GROUP):
        tmp = ind1[1][i]+ind2[1][i]
        new_graph = Dijkstra_Heap(tmp,L[i], trace[i])
        new.append(new_graph)
    return [fitness(new,m), new, m,trace]
# ------------------------local search---------------------------------

# tim canh nho nhat giua 2 nhom


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
    return {k1, k2}

# tim 2 nhom ma canh noi


def GroupEdgeConnect(edge):
    tmp = []
    for i in edge:
        for k in range(NUM_GROUP):
            if i in L[k]:
                tmp.append(k)
                break
    return tmp

# local search


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
            elif k in L[tmp[1]] and k not in L1[tmp[1]] :
                L1[tmp[1]].append(k)
        for j in new_edge:
            if j not in vertexconnect:
                vertexconnect.append(j)
    for i in range(NUM_GROUP):
        trace[i] = random.choice(L1[i]);
    return [fitness(new_ind,vertexconnect), new_ind, vertexconnect,trace]



# ------------------------dot bien---------------------------------

def mutation(ind):
    global NUM_GROUP,L
    ind_copy = ind[1]+[]
    k = random.randint(1, NUM_GROUP-1)
    L1 = L[k]+[]
    n1 = random.choice(L1)
    n2 = random.choice(L1)
    truoc = FindPathBFS(ind[1],ind[2], n1)
    while n1 == n2 or {n1, n2} in ind_copy[k] or truoc[n2-1] not in L1:
        n2 = random.choice(L1)
    ind_copy[k].remove({n2, truoc[n2-1]})
    ind_copy[k].append({n1, n2})
    return [fitness(ind_copy,ind[2]), ind_copy, ind[2],ind[3]]

# -----------------------main----------------------------------

loop = int(sys.argv[2])
size = int(sys.argv[3])
pc = float(sys.argv[4])
pm = float(sys.argv[5])
ph = float(sys.argv[6])
population1 = population(size)
best = tuple(population1[0])
for i in range(1,len(population1)):
    if population1[i][0]<best[0]:
        best = tuple(population1[i])
best1=list(best+())
print best
i=0
thehe = 0
population2 = []
while i < loop:
    i +=1 
    if random.random() < pc:
        k1 = random.randint(0, size-1)
        k2 = random.randint(0, size-1)
        while k1 == k2:
            k2 = random.randint(0, size-1)
        if sys.argv[7] =="1":
            new_ind = crossover1(population1[k1], population1[k2])
        else:
            new_ind = crossover2(population1[k1], population1[k2])
        if new_ind not in population2:
            population2.append(new_ind)
        if new_ind[0] < best[0]:
	    best = tuple(new_ind)
    if len(population2) == size-1:
        population2.append(best1)
        population1 = population2+[]
        for k in range(int(ph*size)):
            k1= random.randint(1,size-1)
            new1 = LocalSearch(population1[k1])
            if new1 not in population1:
                population1[k1]= new1+[]
        for k in range(int(pm*size)):
            k1= random.randint(1,size-1)
            new2 = mutation(population1[k1])
            if new2 not in population1:
                population1[k1]= new2+[]
        for k in range(len(population1)):
            if population1[k][0]<best[0]:
                best = tuple(population1[k])
        best1 =list(best+())
        #if dem>(test*size):
           # break
        thehe += 1
        population2 = []
end_time = time.time()
TIME = round(end_time - start_time,3)       
f = open("ketqua12.txt","a")
f.write("\n---------------------------------------------------------\n")
f.write("seed = "+sys.argv[8]+'\n')
f.write("crossover = "+sys.argv[7]+'\n')
f.write("local search = %f\n"%ph)
f.write("fitness = %d\n"%best[0])
f.write("loop = %d\n"%loop)
f.write("size population= %d\n"%size)
f.write("pc= %f\n"%pc)
f.write("pm= %f\n"%pm)
f.write("TIME = %fs"%TIME)
f.write("\nthe he = %d "%thehe)
for i in range(NUM_GROUP):
    value = best[1][i]
    s="\n"+ str(value)
    f.write(s)
f.close()
print "ket thuc"

