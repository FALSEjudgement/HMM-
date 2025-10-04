def v(k,j):
    if k == 0:
        return pi[j]*pis[j][s_date[0]]
    else:
        V = 0
        for i in range(0,h):
            V = max(V,pis[j][s_date[k]]*pij[i][j]*v(k-1,i))
        return V
    
def S(k,smax):
    for l in range(0,k):
        V = 0
        z = 0
        for i in range(0,h):
            a = v(l,i)
            if V<a:
                V = a
                z = i
        smax.append(z)
    return smax
