from collections import deque

class Solution:
    def bfsOfGraph(self, adj):
        n= len(adj);
        
        vis= [0]*n;
        ans= [];
        
        q= deque([0]);
        vis[0]= 1;
        
        while q:
            node = q.popleft();
            
            ans.append(node);
            
            for it in adj[node]:
                if (not vis[it]):
                    vis[it]= 1;
                    q.append(it);
                    
        return ans;


v= int(input("Enter number of Vertices: "));
adj = [[] for _ in range(v)]
print("Enter adjacency Matrix:");
for i in range(v):
    adj[i]= list( 
            map(
                int, 
                input(f"Enter adjacent vertex for Vectex- {i}: ").split()
            )
        );
    # adj[i].append(int(input(f"Enter adjacent vertex for Vectex- {i}: ")))

for i in range(v):
    print(i, ": ", end="");
    for x in adj[i]:
        print(x, ", ", end="");
    print();


ob= Solution();
ans= ob.bfsOfGraph(adj);

print();
print("BFS: ");
for x in ans:
    print(x, ", ", end="");


#CUSTOM INPUT:
# Enter number of Vertices: 5
# Enter adjacency Matrix:
# Enter adjacent vertex for Vectex- 0: 2 3 1
# Enter adjacent vertex for Vectex- 1: 0
# Enter adjacent vertex for Vectex- 2: 0 4
# Enter adjacent vertex for Vectex- 3: 0
# Enter adjacent vertex for Vectex- 4: 2
# 0 : 2 , 3 , 1 , 
# 1 : 0 ,
# 2 : 0 , 4 ,     
# 3 : 0 ,
# 4 : 2 ,

# BFS:
# 0 , 2 , 3 , 1 , 4 ,