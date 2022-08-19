class UnionFind:
    def __init__(self,n) -> None:
        self.up = list(range(n))
        self.rank = [0] * n
        
    def find(self,x):
        if self.up[x] == x:
            return x
        else:
            self.up[x] = self.find(self.up[x])
            return self.up[x]
        
    def union(self,x,y):
        repr_x = self.find(x)
        repr_y = self.find(y)
        if repr_x == repr_y:   #included in same group
            return False
        if self.rank[repr_x] == self.rank[repr_y]:
            self.rank[repr_x] += 1
            self.up[repr_y] = repr_x
        elif self.rank[repr_x] > self.rank[repr_y]:
            self.up[repr_y] = repr_x
            self.rank[repr_x] += 1
        else:
            self.up[repr_x] = repr_y
            self.rank[repr_y] += 1
        return True
    
#------------------test----------------------
uf = UnionFind(15)
uf.union(0,1)
uf.union(0,3)
uf.union(0,5)
uf.union(0,7)
uf.union(0,9)
uf.union(2,4)
uf.union(2,6)
uf.union(2,8)
uf.union(2,10)
uf.union(8,14)
print(uf.find(1))
print(uf.find(3))
print(uf.find(5))
print(uf.find(7))
print(uf.find(9))
print(uf.up)
print(uf.rank)
            
        