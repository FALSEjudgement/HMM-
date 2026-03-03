def v(k,j):
    if k == 0:
        return pi[j]*pis[j][s_date[0]]
    else:
        V = 0
        for i in range(0,h):
            V = max(V,pij[i][j]*v(k-1,i))
        return V*pis[j][s_date[k]]

def maxv(k_last):
    V = 0
    z = 0
    for i in range(0,h):
        if V<v(k_last,i):
            V = v(k_last,i)
            z = i
    return z

def s(k,smax):
    k_last = len(s_date)-1
    V = maxv(k_last)
    smax.append(V)
    for l in range(k_last-1,0,-1):
        V = 0
        z = 0
        for i in range(0,h):
            a = pij[i][smax[0]]*v(l,i)
            if V<a:
                V = a
                z = i
        smax.insert(0,z)
    return smax
ß    