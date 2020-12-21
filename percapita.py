# cook your dish here
"""Per Capita Income Problem Code: PERCAPTASolvedSubmit

 
Read problems statements in Hindi, Mandarin Chinese, Russian, Vietnamese, and Bengali as well.
Chefland consists of N provinces (numbered 1 through N) connected by M bidirectional roads (numbered 1 through M). For each valid i, the i-th road connects provinces Ui and Vi. It is possible to travel from each province to any other province using these roads.

For each valid i, the annual income of the i-th province is Ai and its population is Bi. The per-capita income of some provinces is lower than that of some other provinces. For this reason, the king of Chefland wants to choose one or more provinces to keep in his kingdom and abandon the rest, in such a way that the per-capita income of the whole resulting kingdom, i.e. the sum of annual incomes of the chosen provinces divided by the sum of their populations, would be maximum possible. However, it should also be possible to travel from each of the chosen provinces to any other chosen province without visiting any of the abandoned provinces. Among all such ways to form the new kingdom, the king would prefer the number of chosen provinces to be as large as possible.

Can you help the king choose which provinces should form the new kingdom? If there are multiple solutions that maximise the per-capita income, you should choose one with the maximum number of chosen provinces. If there are still multiple solutions, you may choose any one.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains two space-separated integers N and M.
The second line contains N space-separated integers A1,A2,…,AN.
The third line contains N space-separated integers B1,B2,…,BN.
M lines follow. For each valid i, the i-th of these lines contains two space-separated integers Ui and Vi.
Output
Print two lines.

The first of these lines should contain a single integer K denoting the number of provinces the king should choose.
The second line should contain K space-separated integers denoting these provinces.
Constraints
1≤T≤5
1≤N,M≤2⋅105
1≤Ui,Vi≤N for each valid i
Ui≠Vi for each valid i
there is at most one road between each pair of provinces
0≤Ai≤109 for each valid i
1≤Bi≤109 for each valid i
Example Input
1
3 3
10 1 2
5 1 1 
1 2
2 3
1 3
Example Output
2
1 3
Explanation
If the king chooses provinces 1 and 3, then the per-capita income is 10+25+1=2. This is the only optimal solution."""





import sys
sys.setrecursionlimit(1000000)
def DFS(v,visited,k,conn):
    visited[v]=1
    k.append(v+1)
    for i in conn[v]:
        if visited[i]==0:
            DFS(i,visited,k,conn)
def solve(visited,conn):
    q={}
    k=[]
    for i in d:
        if visited[i]==0:
            DFS(i,visited,k,conn)
            q[len(k)]=k
            k=[]
    return q
for _ in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    l=[]
    r=0
    for i in range(n):
        q=a[i]/b[i]
        l.append(q)
        r=max(r,q)
    d={}
    for i in range(n):
        if l[i]==r:
            d[i]=1
    conn=[[] for i in range(n)]
    for i in range(m):
        u,v=map(int,input().split())
        u-=1
        v-=1
        if u in d:
            if v in d:
                conn[u].append(v)
                conn[v].append(u)
    visited=[0 for i in range(n)]
    kk=solve(visited,conn)
    s=0
    j=max(kk)
    print(j)
    print(*kk[j])
    
            