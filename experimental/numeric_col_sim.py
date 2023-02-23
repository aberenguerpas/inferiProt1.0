import numpy as np
import numpy as np

import time

def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0: 
       return v
    return v / norm

def isInteger(a):
    floa = 0
    inte = 0
    for i in a:
        try:
            if float(i).is_integer():
                inte+=1
            else:
                floa+=1
        except ValueError:
            pass

    if floa>inte:
        return 0
    else:
        return 1


def score(a, b):

    a_mean = np.mean(a)
    a_var = np.var(a)
    a_type = isInteger(a)

    b_mean = np.mean(b)
    b_var = np.var(b)
    b_type = isInteger(b)


    score_mean = 1 - abs(a_mean-b_mean)/(a_mean+b_mean)
    score_var = 1 - abs(a_var-b_var)/(a_var+b_var)
    score_type = 1 if a_type==b_type else 0

    return [score_mean, score_var, score_type]

# Temperaturas
A = np.array([15,12,14,15,13,14,11])
B = np.array([10,10,10,11,12,10,12,11])

# Precios
C = np.array([12.3,4.1,20.3,9.5,55.6,66.7,100.4,1.1])
D = np.array([194.33,344.11,264.14,433.13,485.42,552.13,215.1,2771.9])

# Años
E = np.array([2001,2002,2003,2004,2005])
F = np.array([1900,1920,1940,1960,1980,2000])

start = time.time()
for a in range(100000):
    np.mean(score(C,A))
    np.mean(score(C,B))
    np.mean(score(C,C))
    np.mean(score(C,D))
    np.mean(score(C,E))
    np.mean(score(C,F))


print(time.time()- start, 'seconds')

#print(similarity)
