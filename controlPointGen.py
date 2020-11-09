# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 23:52:57 2020

@author: Matt
"""

import numpy as np


class ControlPoint():
    """
    Class which holds x,y,z points
    """
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

def contractionGen(R1, lengthOverRadius):
    """
    Parameters
    ----------
    R1 : float
        Big radius (upstream)
    lengthOverRadius : float
        defines how long the contraction is

    Returns
    -------
    points : tuple
        tuple of control points

    """
    _LR_unit = 1.9443489471422435
    _R1_unit = 0.4654
    _topLip_unit = 0.4918
    LR = lengthOverRadius*2*R1
    
    
    topLipY = _topLip_unit/0.4654*R1
    cp1 = ControlPoint((0.7735-0.5)/_LR_unit*LR, topLipY, 0)
    cp2 = ControlPoint((0.7568-0.5)/_LR_unit*LR, topLipY, 0)
    cp3 = ControlPoint((0.7394-0.5)/_LR_unit*LR, topLipY, 0)
    cp4 = ControlPoint((0.7205-0.5)/_LR_unit*LR, topLipY, 0)
    cp5 = ControlPoint(0, 0.4841/_R1_unit*R1, 0)
    cp6 = ControlPoint(0, R1, 0)
    cp7 = ControlPoint(0, 0.4386/_R1_unit*R1, 0)
    cp8 = ControlPoint((0.7212-0.5)/_LR_unit*LR, 0.444/_R1_unit*R1, 0)
    cp9 = ControlPoint((0.7636-0.5)/_LR_unit*LR, 0.4409/_R1_unit*R1, 0)
    cp10 = ControlPoint((0.8136-0.5)/_LR_unit*LR, 0.4356/_R1_unit*R1, 0)
    cp10 = ControlPoint((0.8136-0.5)/_LR_unit*LR, 0.4356/_R1_unit*R1, 0)
    cp11 = ControlPoint((1.236-0.5)/_LR_unit*LR, 0, 0)
    cp12 = ControlPoint((1.395-0.5)/_LR_unit*LR, 0, 0)
    cp12 = ControlPoint((1.445-0.5)/_LR_unit*LR, 0, 0)
    cp13 = ControlPoint((1.5-0.5)/_LR_unit*LR, 0, 0)
    
    points = (cp1, cp2, cp3, cp4, cp5, cp6, cp7, cp8, cp9, cp10, cp11, cp12, cp13)
    return points
    
if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import bezierFunc
    points = contractionGen(5, 2)
    X = [points[i].x for i in range(np.size(points))]
    Y = [points[i].y for i in range(np.size(points))]
    Z = [points[i].z for i in range(np.size(points))]
    plt.scatter(X,Y)
    plt.axis('equal')
    
    P = np.array([X,Y,Z])
    t = np.linspace(0,1,30)
    Q_mm = bezierFunc.Bezier(P,t)
    Q_mm[1,:] = Q_mm[1,:]
    
    plt.plot(Q_mm[0,:],Q_mm[1,:])
    plt.axis('equal')
