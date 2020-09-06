from __future__ import division
from pylab import *
from scipy.special.orthogonal import p_roots

def gauss(f,n,a,b):
    [x,w] = p_roots(n+1)
    integ=0.5*(b-a)*sum(w*f(0.5*(b-a)*x+0.5*(b+a)))
    print(integ)

def my_f(x):
    return x**2

gauss(my_f,2,0,1)