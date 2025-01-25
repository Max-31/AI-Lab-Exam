class Solution:
    # def dls(node, vis, adj, ans, h): #WRONG SYNTAX
    # SELF include kortei hobe!!!
    def dls(self, node, vis, adj, ans, h):
        if(h):
            vis[node]= 1;
            ans.append(node);
            
            for x in adj[node]:
                if (not vis[x]):
                    self.dls(x, vis, adj, ans, h-1);
        
        
    
    def dlsOfGraph(self, adj, h):
        n= len(adj);
        
        vis= [0]*n;
        
        ans= [];
        
        self.dls(0, vis, adj, ans, h);
        
        return ans;
        

v= int(input("Enter No. of Vertices: "));
h= int(input("Enter Depth Limit: "));
adj= [[] for _ in range(v)];
for i in range(v):
    adj[i] = list(
            map(
                int,
                input(f"Enter Adjacent node for Vertex-{i}: ").split()
            )
        );
        
for i in range(v):
    print(i, ": ", end="");
    for x in adj[i]:
        print(x, ", ", end="");
    print();
    
obj= Solution();
ans= obj.dlsOfGraph(adj, h);

print("DLS: ")
for x in ans:
    print(x, ", ", end="");


#CUSTOM INPUT:
# Enter No. of Vertices: 5
# Enter Depth Limit: 2
# Enter Adjacent node for Vertex-0: 2 3 1
# Enter Adjacent node for Vertex-1: 0
# Enter Adjacent node for Vertex-2: 0 4
# Enter Adjacent node for Vertex-3: 0
# Enter Adjacent node for Vertex-4: 2
# 0 : 2 , 3 , 1 , 
# 1 : 0 ,
# 2 : 0 , 4 ,
# 3 : 0 ,
# 4 : 2 ,
# DLS:
# 0 , 2 , 3 , 1 ,