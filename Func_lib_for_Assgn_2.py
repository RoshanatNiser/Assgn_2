# This code is performing Gaussian elimination
# Name: Roshan Yadav
# Roll no: 2311144

import copy

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
        ''''This fuction does the 
        constant 'c'multpication 
        to a row no 'p'.'''
        for i in range(len(self.data[p])):
            self.data[p][i]=float(c)*float(self.data[p][i])

    def row_ops(self,f=None,r=None,c=None):
        '''This function does the following row operation:
        Row[f] ->Row[f] + c*Row[r]'''
        for i in range(len(self.data[f])):
            self.data[f][i] = float(self.data[f][i]) + float(c) *  float(self.data[r][i])
    
    def aug(self,b=None):
        A = copy.deepcopy(self.data)

        for i in range(len(A)):
            if isinstance(b[0], list):
                A[i].append(b[i][0])  
            else:
                A[i].append(b[i])    
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
        
        for i in range(m):
            # Finding pivot
            max_row = i
            for k in range(i + 1, m):
                if abs(A.data[k][i]) > abs(A.data[max_row][i]):
                    max_row = k
            
            # Swap the current row with the max row
            if max_row != i:
                A.row_swap(i, max_row)
            
            # Make diagonal element 1
            if A.data[i][i] != 0:
                A.con_mul(c=A.zero(A.data[i][i]), p=i)
            
            # Make other elements in column i zero
            for j in range(m):
                if j != i and A.data[j][i] != 0:
                    A.row_ops(j, i, -A.data[j][i])
        
        # Extract solution
        L = []
        for i in range(len(A.data)):
            L.append(A.data[i][len(A.data[i])-1])
        
        A.display()
        
        return L


