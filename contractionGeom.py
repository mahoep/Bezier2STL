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


def downstreamCurve(contractionEndPoint,length):
    downCurve = np.zeros([3,2])
    downCurve[0,0] = contractionEndPoint[0] # this is the x coord 
    downCurve[1,0] = contractionEndPoint[1] # this is the y coord 
    downCurve[2,0] = contractionEndPoint[2] # this is the z coord 
    
    downCurve[0,1] = contractionEndPoint[0] + length # this is the x coord
    downCurve[1,1] = contractionEndPoint[1] # this is the y coord 
    downCurve[2,1] = contractionEndPoint[2] # this is the z coord 
    
    return downCurve


def outletCurve(downCurveEnd):
    outletLine = np.zeros([3,2])
    outletLine[0,0] = downCurveEnd[0] # this is the x coord 
    outletLine[1,0] = downCurveEnd[1] # this is the y coord 
    outletLine[2,0] = downCurveEnd[2] # this is the z coord 
    
    outletLine[0,1] = downCurveEnd[0] # this is the x coord
    outletLine[1,1] = 0 # this is the y coord 
    outletLine[2,1] = downCurveEnd[2] # this is the z coord
    
    return outletLine


def symmetryCurve(inletEnd):
    symmetryLine = np.zeros([3,2])
    symmetryLine[0,0] = 0 # this is the x coord 
    symmetryLine[1,0] = 0 # this is the y coord 
    symmetryLine[2,0] = 0 # this is the z coord 
    
    symmetryLine[0,1] = inletEnd[0] # this is the x coord
    symmetryLine[1,1] = inletEnd[1] # this is the y coord 
    symmetryLine[2,1] = inletEnd[2] # this is the z coord
    
    return symmetryLine


def inletCurve(maxR):
    inletLine = np.zeros([3,2])
    inletLine[0,0] = 0 # this is the x coord 
    inletLine[1,0] = 0 # this is the y coord 
    inletLine[2,0] = 0 # this is the z coord 
    
    inletLine[0,1] = 0 # this is the x coord
    inletLine[1,1] = maxR # this is the y coord 
    inletLine[2,1] = 0 # this is the z coord
    
    return inletLine

def topCurve(inletLineEnd, downCurveEnd):
    topLine = np.zeros([3,2])
    topLine[0,0] = inletLineEnd[0] # this is the x coord 
    topLine[1,0] = inletLineEnd[1] # this is the y coord 
    topLine[2,0] = inletLineEnd[2] # this is the z coord 
    
    topLine[0,1] = downCurveEnd[0] # this is the x coord
    topLine[1,1] = inletLineEnd[1] # this is the y coord 
    topLine[2,1] = downCurveEnd[2] # this is the z coord
    
    return topLine


def rightCurve(topLineEnd, R2):
    rightLine = np.zeros([3,2])
    rightLine[0,0] = topLineEnd[0] # this is the x coord 
    rightLine[1,0] = topLineEnd[1] # this is the y coord 
    rightLine[2,0] = topLineEnd[2] # this is the z coord 
    
    rightLine[0,1] = topLineEnd[0] # this is the x coord
    rightLine[1,1] = R2*1.5 # this is the y coord 
    rightLine[2,1] = topLineEnd[0]# this is the z coord
    
    return rightLine


def backSideCurve(upStreamDist, rightLineEnd):
    backSideLine = np.zeros([3,2])
    backSideLine[0,0] = rightLineEnd[0] # this is the x coord 
    backSideLine[1,0] = rightLineEnd[1] # this is the y coord 
    backSideLine[2,0] = rightLineEnd[2] # this is the z coord 
    
    backSideLine[0,1] = rightLineEnd[0] - upStreamDist/2 # this is the x coord 
    backSideLine[1,1] = rightLineEnd[1] # this is the y coord 
    backSideLine[2,1] = rightLineEnd[2] # this is the z coord 
    
    return backSideLine


    
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
    t = np.linspace(0,1,40)
    Q_mm = bezierFunc.Bezier(P,t)
    Q_mm[1,:] = Q_mm[1,:]
    
    plt.plot(Q_mm[0,:],Q_mm[1,:])
    plt.axis('equal')
