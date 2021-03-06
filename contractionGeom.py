# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 23:52:57 2020

@author: mahoep
"""

import numpy as np


def _contractionGen(R1, lengthOverRadius):
    """
    DON'T CHANGE THESE VALUES USE THE OTHER FUNCTION
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
    cp1 = np.array([(0.7735-0.5)/_LR_unit*LR, topLipY, 0])
    cp2 = np.array([(0.7568-0.5)/_LR_unit*LR, topLipY, 0])
    cp3 = np.array([(0.7394-0.5)/_LR_unit*LR, topLipY, 0])
    cp4 = np.array([(0.7205-0.5)/_LR_unit*LR, topLipY, 0])
    cp5 = np.array([0, 0.4841/_R1_unit*R1, 0])
    cp6 = np.array([0, R1, 0])
    cp7 = np.array([0, 0.4386/_R1_unit*R1, 0])
    cp8 = np.array([(0.7212-0.5)/_LR_unit*LR, 0.444/_R1_unit*R1, 0])
    cp9 = np.array([(0.7636-0.5)/_LR_unit*LR, 0.4409/_R1_unit*R1, 0])
    cp10 = np.array([(0.8136-0.5)/_LR_unit*LR, 0.4356/_R1_unit*R1, 0])
    cp10 = np.array([(0.8136-0.5)/_LR_unit*LR, 0.4356/_R1_unit*R1, 0])
    cp11 = np.array([(1.236-0.5)/_LR_unit*LR, 0, 0])
    cp12 = np.array([(1.395-0.5)/_LR_unit*LR, 0, 0])
    cp12 = np.array([(1.445-0.5)/_LR_unit*LR, 0, 0])
    cp13 = np.array([(1.5-0.5)/_LR_unit*LR, 0, 0])
    
    points = np.array([cp1, cp2, cp3, cp4, cp5, cp6, cp7, cp8, cp9, cp10, cp11, cp12, cp13])
    return points


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
    cp1 = np.array([(0.7735-0.5)/_LR_unit*LR, topLipY, 0])
    cp2 = np.array([(0.7568-0.5)/_LR_unit*LR, topLipY, 0])
    cp3 = np.array([(0.7394-0.5)/_LR_unit*LR, topLipY, 0])
    cp4 = np.array([(0.7205-0.5)/_LR_unit*LR, topLipY, 0])
    cp5 = np.array([0, 0.4841/_R1_unit*R1, 0])
    cp6 = np.array([0, R1, 0])
    cp7 = np.array([0, 0.4386/_R1_unit*R1, 0])
    cp8 = np.array([(0.7212-0.5)/_LR_unit*LR, 0.444/_R1_unit*R1, 0])
    cp9 = np.array([(0.7636-0.5)/_LR_unit*LR, 0.4409/_R1_unit*R1, 0])
    cp10 = np.array([(0.8136-0.5)/_LR_unit*LR, 0.4356/_R1_unit*R1, 0])
    cp10 = np.array([(0.8136-0.5)/_LR_unit*LR, 0.4356/_R1_unit*R1, 0])
    cp11 = np.array([(1.236-0.5)/_LR_unit*LR, 0, 0])
    cp12 = np.array([(1.395-0.5)/_LR_unit*LR, 0, 0])
    cp12 = np.array([(1.445-0.5)/_LR_unit*LR, 0, 0])
    cp13 = np.array([(1.5-0.5)/_LR_unit*LR, 0, 0])
    
    points = np.array([cp1, cp2, cp3, cp4, cp5, cp6, cp7, cp8, cp9, cp10, cp11, cp12, cp13])
    return points


def downstreamCurve(contractionEndPoint,downStreamDist):
    """
    Parameters
    ----------
    contractionEndPoint : numpy.ndarray
        An x,y,z coordinate pair of the last point generated from the bezier curve (far right)
    upStreamDist : float
        defines the straightline distance from the end of the contraction to the end of the domain

    Returns
    -------
    downCurve : numpy.ndarray
        returns two (x,y,z) coordinates.
    """
    downCurve = np.zeros([3,2])
    downCurve[0,0] = contractionEndPoint[0] # this is the x coord 
    downCurve[1,0] = contractionEndPoint[1] # this is the y coord 
    downCurve[2,0] = contractionEndPoint[2] # this is the z coord 
    
    downCurve[0,1] = contractionEndPoint[0] + downStreamDist # this is the x coord
    downCurve[1,1] = contractionEndPoint[1] # this is the y coord 
    downCurve[2,1] = contractionEndPoint[2] # this is the z coord 
    
    return downCurve


def outletCurve(downCurveEnd):
    """
    Parameters
    ----------
    downCurveEnd : numpy.ndarray
        An x,y,z coordinate pair of the last point generated from straightline after bezier

    Returns
    -------
    outletLine : numpy.ndarray
        outletLine is two (x,y,z) coordinates.
    """
    outletLine = np.zeros([3,2])
    outletLine[0,0] = downCurveEnd[0] # this is the x coord 
    outletLine[1,0] = downCurveEnd[1] # this is the y coord 
    outletLine[2,0] = downCurveEnd[2] # this is the z coord 
    
    outletLine[0,1] = downCurveEnd[0] # this is the x coord
    outletLine[1,1] = 0 # this is the y coord 
    outletLine[2,1] = downCurveEnd[2] # this is the z coord
    
    
    return outletLine


def symmetryCurve(outletEnd):
    """
    Parameters
    ----------
    inletEnd : numpy.ndarray
        An x,y,z coordinate pair of the last point generated from outlet line

    Returns
    -------
    symmetryLine : numpy.ndarray
        returns two (x,y,z) coordinate that defines the bottom (symmetry) line

    """
    symmetryLine = np.zeros([3,2])
    symmetryLine[0,0] = outletEnd[0] # this is the x coord 
    symmetryLine[1,0] = outletEnd[1] # this is the y coord 
    symmetryLine[2,0] = outletEnd[2] # this is the z coord 
    
    symmetryLine[0,1] = 0 # this is the x coord
    symmetryLine[1,1] = 0 # this is the y coord 
    symmetryLine[2,1] = 0 # this is the z coord
    
    return symmetryLine


def inletCurve(maxR):
    """
    Parameters
    ----------
    maxR : float
        maxR is the overall radius of the geometry (greater than the lip radius).

    Returns
    -------
    inletLine : numpy.ndarray
        returns two (x,y,z) coordinate that defines the inlet (lef) line

    """
    inletLine = np.zeros([3,2])
    inletLine[0,0] = 0 # this is the x coord 
    inletLine[1,0] = 0 # this is the y coord 
    inletLine[2,0] = 0 # this is the z coord 
    
    inletLine[0,1] = 0 # this is the x coord
    inletLine[1,1] = maxR # this is the y coord 
    inletLine[2,1] = 0 # this is the z coord
    
    return inletLine


def topCurve(inletLineEnd, downCurveEnd):
    """
    Parameters
    ----------
    inletLineEnd : numpy.ndarray
        An x,y,z coordinate pair of the last point generated from inlet line
    downCurveEnd : numpy.ndarray
        An x,y,z coordinate pair of the last point generated from straightline after bezier curve

    Returns
    -------
    topLine : numpy.ndarray
        returns two (x,y,z) coordinates that defines the top boundary wall

    """
    topLine = np.zeros([3,2])
    topLine[0,0] = inletLineEnd[0] # this is the x coord 
    topLine[1,0] = inletLineEnd[1] # this is the y coord 
    topLine[2,0] = inletLineEnd[2] # this is the z coord 
    
    topLine[0,1] = (downCurveEnd[0] -inletLineEnd[0]) /2 # this is the x coord
    topLine[1,1] = inletLineEnd[1] # this is the y coord 
    topLine[2,1] = downCurveEnd[2] # this is the z coord
    
    return topLine


def rightCurve(topLineEnd, topLipEnd):
    """
    Parameters
    ----------
    topLineEnd : numpy.ndarray
         An x,y,z coordinate pair of the last point generated from top line
    topLipEnd : numpy.ndarray
        An x,y,z coordinate pair of the first point from the bezier curve (lip)

    Returns
    -------
    rightLine : numpy.ndarray
        returns (x,y,z) points that define the right wall (at the top) and the connection back to the start

    """
    rightLine = np.zeros([3,5])
    rightLine[0,0] = topLineEnd[0] # this is the x coord 
    rightLine[1,0] = topLineEnd[1] # this is the y coord 
    rightLine[2,0] = topLineEnd[2] # this is the z coord 
    
    rightLine[0,1] = topLineEnd[0] # this is the x coord 
    rightLine[1,1] = topLipEnd[1] # this is the y coord 
    rightLine[2,1] = topLineEnd[2] # this is the z coord 
    
    rightLine[0,2] = topLineEnd[0] # this is the x coord 
    rightLine[1,2] = topLipEnd[1] # this is the y coord 
    rightLine[2,2] = topLineEnd[2] # this is the z coord 
    
    rightLine[0,3] = topLipEnd[0] # this is the x coord
    rightLine[1,3] = topLipEnd[1] # this is the y coord 
    rightLine[2,3] = topLipEnd[2]# this is the z coord
    
    rightLine[0,4] = topLipEnd[0] # this is the x coord
    rightLine[1,4] = topLipEnd[1] # this is the y coord 
    rightLine[2,4] = topLipEnd[2]# this is the z coord
    
    return rightLine


def backSideCurve(upStreamDist, rightLineEnd):
    "CURRENLTY NOT BEING CALLED"
    """
    Parameters
    ----------
    upStreamDist : float
        the straightline distance after the bezier curve
    rightLineEnd : numpy.ndarray
        An x,y,z coordinate pair of the last point on the right line

    Returns
    -------
    backSideLine : numpy.ndarray
        returns (x,y,z) points that define the curve on the backside of the bezier curve.

    """
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
    points = _contractionGen(5, 2)
    X = points[:,0]
    Y = points[:,1]
    Z = points[:,2]
    plt.scatter(X,Y)
    plt.axis('equal')
    
    P = np.array([X,Y,Z])
    t = np.linspace(0,1,40)
    Q_mm = bezierFunc.Bezier(P,t)
    Q_mm[1,:] = Q_mm[1,:]
    
    plt.plot(Q_mm[0,:],Q_mm[1,:])
    plt.axis('equal')
