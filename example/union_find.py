class Partition:
    "Union_find structure for maintaining disjoint sets"
    #------------ nested Position class -----------------
    class Position:
        __slot__ = '_container','_element','_size','_parent'
        
        def __init__(self,container,e) -> None:
            "Create a new position that is the leader of its own group"
            self._container = container #reference to Partition instance
            self._element = e
            self._size = 1
            self._parent = self  #convention for a group leader
            
        def element(self):
            "return element stored at this position"
            return self._element
    
    #---------public Partition methods---------------
    def make_group(self,e):
        "make a new group containing element e return its position"
        return self.Position(self,e)
    
    def find(self,p):
        "find the group containing p return the position of its leader"
        if p._parent != p:
            p._parent = self.find(p._parent)
        return p._parent
    
    def union(self,p,q):
        "merge groups containing p and q"
        a = self.find(p)
        b = self.find(q)
        if a is not b:  # different group can merge
            if a._size > b._size:
                b._parent = a
                a._size += b._size
            else:
                a._parent = b
                b._size += a._size
                
# ----------------test-----------------
par = Partition()
p_set = []
for i in range(15):
    p_set.append(par.make_group(i)) # create some position object
par.union(p_set[2],p_set[1])
par.union(p_set[0],p_set[3])
par.union(p_set[3],p_set[14])
par.union(p_set[0],p_set[13])
par.union(p_set[0],p_set[10])

print(par.find(p_set[2]).element())  #find leader of a group
print(par.find(p_set[10]).element())
print(par.find(p_set[13]).element())
print(par.find(p_set[3]).element())


    
    
    
                