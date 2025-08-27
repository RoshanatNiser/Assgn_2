# This code is part of a Python module for performing Gaussian elimination
# Name: Roshan Yadav
# Roll no: 2311144
import copy

def read_matrix(filename):
    with open( filename , 'r' ) as f :
        matrix =[]
        for line in f :
            # Convert each line into a list of floats
            row = [ float(num) for num in line.strip().split() ]
            matrix.append(row)
    return matrix


class matrix():
    def __init__(self,data=None):
        self.m=len(data)
        self.n=len(data[0])
        self.data=data
    def display(self):
        print(self.data)
        return None
    
    def row_swap(self,u=None,p=None):
        self.data[u], self.data[p] = self.data[p], self.data[u]
    
    def con_mul(self,c=0,p=0):
        '''This function does the 
        constant 'c' multiplication 
        to a row no 'p'.'''
        for i in range(len(self.data[p])):
            self.data[p][i]=float(c)*float(self.data[p][i])
    
    def row_ops(self,f=None,r=None,c=None):
        '''This function does the following row operation:
        Row[f] ->Row[f] + c*Row[r]'''
        for i in range(len(self.data[f])):
            self.data[f][i] = float(self.data[f][i]) + float(c) *  float(self.data[r][i])
    
    def aug(self,b=None):
        # Create a deep copy to avoid modifying original data
        A = copy.deepcopy(self.data)
        # Handle both 1D and 2D b vectors
        for i in range(len(A)):
            if isinstance(b[0], list):
                A[i].append(b[i][0])  # b is 2D, take first element
            else:
                A[i].append(b[i])     # b is 1D
        return A
    
    def zero(self,i=0):
        if i==0:
            return 0
        else:
            return float(1/i) 
    
    def gauss_jorden(self, b=None):
        A = self.aug(b)
        A = matrix(A)
        
        m = self.m
        n = self.n
        
        # Forward elimination with partial pivoting
        for i in range(min(m, n)):
            # Find pivot (largest element in column i from row i onwards)
            max_row = i
            for k in range(i + 1, m):
                if abs(A.data[k][i]) > abs(A.data[max_row][i]):
                    max_row = k
            
            # Swap rows if needed
            if max_row != i:
                A.row_swap(i, max_row)
            
            # Check if pivot is zero
            if abs(A.data[i][i]) < 1e-10:
                print(f"Matrix is singular at column {i}")
                return None
            
            # Make diagonal element 1
            pivot = A.data[i][i]
            A.con_mul(c=1.0/pivot, p=i)
            
            # Make elements below pivot zero
            for j in range(i + 1, m):
                if abs(A.data[j][i]) > 1e-10:
                    multiplier = -A.data[j][i]
                    A.row_ops(j, i, multiplier)
        
        # Back substitution (Jordan part)
        for i in range(min(m,n)-1, -1, -1):
            for j in range(i):
                if abs(A.data[j][i]) > 1e-10:
                    multiplier = -A.data[j][i]
                    A.row_ops(j, i, multiplier)
        
        A.display()  # Display the final matrix after elimination
        
        # Extract solution
        L = []
        for i in range(min(m, n)):
            L.append(A.data[i][n])  # Solution is in column n (last column)
        
        return L

