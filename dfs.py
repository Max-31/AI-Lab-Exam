class Solution:
    def dfs(self, node, vis, adj, ans):
        ans.append(node);
        
        for it in adj[node]:
            if (not vis[it]):
                vis[it]= 1;
                self.dfs(it, vis, adj, ans);
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, adj):
        n= len(adj);
        # print(n);
        
        vis= [0]*n;
        
        ans= [];
        
        vis[0]= 1;
        self.dfs(0, vis, adj, ans);
        
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
ans= ob.dfsOfGraph(adj);

print();
print("DFS: ");
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

# DFS:
# 0 , 2 , 4 , 3 , 1 ,