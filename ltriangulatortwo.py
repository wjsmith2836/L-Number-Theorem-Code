N = 20 # Grid dimension
C = 3
    
# A helper: get the Dimacs CNF variable number for the variable v_{r,c,v}
# encoding the fact that the cell at (r,c) has the value v
def var(r, c, v):
    assert(1 <= r and r <= N and 1 <= c and c <= N and 1 <= v and v <= N)
    return (r-1)*N*C+(c-1)*C+(v-1)+1
    
# Build the clauses in a list
cls = []  # The clauses: a list of integer lists
for r in range(1,N+1): # r runs over 1,...,N
    for c in range(r+1, N+1):
        # The cell at (r,c) has at least one value
        cls.append([var(r,c,v) for v in range(1,4)])
        # The cell at (r,c) has at most one value
        for v in range(1, C+1):
            for w in range(v+1,C+1):
                cls.append([-var(r,c,v), -var(r,c,w)])
        # There are no Ls of any size in the grid
        if c > r:
            for i in range(1, N-c+1):
                for v in range(1, C+1):
                    cls.append([-var(r,c,v), -var(r+i,c,v), -var(r+i,c+i,v)])
        else:
            for i in range(1, N-r+1):
                for v in range(1, C+1):
                    cls.append([-var(r,c,v), -var(r+i,c,v), -var(r+i,c+i,v)])


# Output the DIMACS CNF representation
# Print the header line
print("p cnf %d %d" % (N*N*C, len(cls)))
# Print the clauses
for c in cls:
    print(" ".join([str(l) for l in c])+" 0")


