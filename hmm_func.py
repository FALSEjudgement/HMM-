import numpy as np

#---------------------------------------------------

"""

h = 2 #hide state
s = 3 #date

def pis(h, s):      #p of transfer : h*s
    mat = np.random.rand(h, s)             
    p = mat / mat.sum(axis=1, keepdims=True) 
    return p                                                                    R
                                                                                A
def pij(h):         #p of state -> date : h*h                                   N
    mat = np.random.rand(h, h)                                                  D
    p = mat / mat.sum(axis=1, keepdims=True)                                    O
    return p                                                                    M

    #p of state -> date : h*h

def pi(h):          #begin p of hide state : 1*h
    vec = np.random.rand(h)
    p = vec / vec.sum()
    return p

pi = pi(h)
pis = pis(h,s)      #p of transfer : h*s
pij = pij(h)  

"""

"""

h = 2                                                                           #T
s = 2                                                                           #E
pi = [0.8,0.2]     #p(x1=i)                                                     #s
                                                                                #T
pij=[
    [0.9,0.1],
    [0.0,1.0]
]

pis = [
    [0.99,0.01],
    [0.96,0.04]
]

s_date = [0,1,0,0,1]

"""

#----------------------------------------------------------------------------

def F(n,j):
    if n == 0:
        return pi[j]*pis[j][s_date[0]]
    else:
        f = 0 
        for i in range(0,h):
            f += F(n-1,i)*pij[i][j]
        return f*pis[j][s_date[n]]

def B(k,j):
    if k == len(s_date)-2:
        b = 0
        for i in range(0,h):
            b += pij[j][i]*pis[i][s_date[-1]]
        return b
    else:
        b = 0
        for i in range(0,h):
            b += pij[j][i]*pis[i][s_date[k+1]]*B(k+1,i)
        return b

#----------------------------------------------------------------------------
                                                                            
def Fp(n):                                                                  
    s = 0
    for i in range(0,h):                                                    
        s += F(n,i)
    return s

def Bp(n):
    s = 0
    for i in range(0,h):
        s += pis[i][s_date[0]]*B(0,i)*pi[i]
    return s

def FBp(k):
    s = 0
    for i in range(0,h):
        s += F(k,i)*B(k,i)
    return s



