# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 22:33:10 2020

@author: Matt
"""

import numpy as np
import bezierFunc
import contractionGeom
import matplotlib.pyplot as plt

R1 = 0.4645
R2 = 0.2
maxR = 0.8
length_Radius = 1.944
upStreamDist = 0.3

points = contractionGeom.contractionGen(R1, length_Radius)
x = [points[i].x for i in range(np.size(points))]
y = [points[i].y for i in range(np.size(points))]
z = [points[i].z for i in range(np.size(points))]

P = np.array([x,y,z])
t = np.linspace(0,1,50)
Q = bezierFunc.Bezier(P,t)
Q[0,:] = Q[0,:] + upStreamDist - min(Q[0,:])
Q[1,:] = Q[1,:] + R2

contractionEndPoint = np.array([Q[0,-1], Q[1,-1], Q[2,-1]])
length = 0.3

downLine = contractionGeom.downstreamCurve(contractionEndPoint, length)

outletLine = contractionGeom.outletCurve(downLine[:,-1])

symmetryLine = contractionGeom.symmetryCurve(outletLine[:,-1])

inletLine = contractionGeom.inletCurve(maxR)

topLine = contractionGeom.topCurve(inletLine[:,-1], downLine[:,-1])

rightLine = contractionGeom.rightCurve(topLine[:,-1], R2)

backSideLine = contractionGeom.backSideCurve(upStreamDist, rightLine[:,-1])

cp1 = np.array([backSideLine[0,-1], backSideLine[1,-1], backSideLine[2,-1] ])
cp2 = np.array([backSideLine[0,-1]-0.2, backSideLine[1,-1], backSideLine[2,-1] ])
cp3 = np.array([Q[0,0]+0.2, Q[1,0], Q[2,0]])
cp4 = np.array([Q[0,0], Q[1,0], Q[2,0]])

backSide_P = np.array( [ [cp1[0], cp2[0], cp3[0], cp4[0]], [cp1[1], cp2[1], cp3[1], cp4[1]], [cp1[2], cp2[2], cp3[2], cp4[2]]]   )
backSide_t = np.linspace(0,1,50)
backSide_Q = bezierFunc.Bezier(backSide_P,backSide_t)


Xcurve = np.concatenate((Q[0,:], downLine[0,:], outletLine[0,:], symmetryLine[0,:], inletLine[0,:], topLine[0,:], rightLine[0,:], backSideLine[0,:], backSide_Q[0,:]))
Ycurve = np.concatenate((Q[1,:], downLine[1,:], outletLine[1,:], symmetryLine[1,:], inletLine[1,:], topLine[1,:], rightLine[1,:], backSideLine[1,:], backSide_Q[1,:]))
Zcurve = np.concatenate((Q[2,:], downLine[2,:], outletLine[2,:], symmetryLine[2,:], inletLine[2,:], topLine[2,:], rightLine[2,:], backSideLine[2,:], backSide_Q[2,:]))

#plt.plot(Q[0,:],Q[1,:])
#plt.axis('equal')

alpha = np.rad2deg(np.arctan( abs( y[-2] - y[4]) / abs( x[-2] - x[4])))
print(alpha)

plt.plot(Xcurve,Ycurve)
plt.axis('equal')
plt.ylim(0)
plt.xlim(0)


