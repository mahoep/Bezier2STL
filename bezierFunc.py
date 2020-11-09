# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 18:21:40 2020

@author: mahoep
"""


import numpy as np
from math import factorial as factorial

def Bezier(P,t):
    """
    Bezier interpolation for given points.
    t should be a numpy array, [0.....1]
    P should be a numpy array of X,Y,Z points of control Bezier points
        row 1 are X values
        row 2 are Y values
        row 3 are Z values
        a column would  be (X_n, Y_n, Z_n)
    
    """
    if max(t) > 1:
        raise Exception('t should be a numpy array, starting with 0 and ending with 1')
    if P is not np.ndarray or t is not np.ndarray:
         Q = np.zeros([3,len(t)])
         for j in range(np.size(t)):
             for i in range(np.size(P,1)):
                 B = Bernstein(np.size(P,1)-1,i,t[j])
                 Q[:,j] = Q[:,j] + P[:,i] * B
                 
                 
    else:
         raise TypeError('inputs must be of numpy array (numpy.ndarray')
     
    return Q


def Bernstein(n,j,t):
    """
    This function is only for readability, it's only ever called under Bezier()
    """
    B=factorial(n)/(factorial(j)*factorial(n-j))*(t**j)*(1-t)**(n-j)
    return B


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    P = np.array([\
                 [0.773486364,0.756818182,0.739395455,0.720454545,0.5,0.5,0.5,0.721213636,0.763636364,0.813636364,1.236363636,1.395454545,1.445454545,1.5], #x
                 [0.491818182,0.491818182,0.49181818,0.491818182,0.484090909,0.46,0.438636364,0.443954545,0.440909091,0.435636364,0,0,0,0], #y
                 [0,0,0,0,0,0,0,0,0,0,0,0,0,0]]) #z
                 
    t = np.linspace(0,1,30)
    Q = Bezier(P,t)
    
    plt.scatter(P[0,:],P[1,:],c='g')
    plt.plot(Q[0,:],Q[1,:])
    plt.axis('equal')
    plt.show()
    