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

downLine = contractionGeom.downstreamCurve(contractionEndPoint, upStreamDist)

outletLine = contractionGeom.outletCurve(downLine[:,-1])

symmetryLine = contractionGeom.symmetryCurve(outletLine[:,-1])

inletLine = contractionGeom.inletCurve(maxR)

topLine = contractionGeom.topCurve(inletLine[:,-1], downLine[:,-1])

rightLine = contractionGeom.rightCurve(topLine[:,-1], [Q[0,0], Q[1,0], Q[2,0]])

Xcurve = np.concatenate((Q[0,:], downLine[0,:], outletLine[0,:], symmetryLine[0,:], inletLine[0,:], topLine[0,:], rightLine[0,:]))
Ycurve = np.concatenate((Q[1,:], downLine[1,:], outletLine[1,:], symmetryLine[1,:], inletLine[1,:], topLine[1,:], rightLine[1,:]))
Zcurve = np.concatenate((Q[2,:], downLine[2,:], outletLine[2,:], symmetryLine[2,:], inletLine[2,:], topLine[2,:], rightLine[2,:]))

M = np.array([Xcurve, Ycurve, Zcurve])
idx = np.unique(M,axis=1, return_index=True)[1]
LineALL = np.transpose(np.array([M[:,i] for i in sorted(idx)]))

alpha = np.rad2deg(np.arctan( abs( y[-2] - y[4]) / abs( x[-2] - x[4])))
print(alpha)

#plt.plot(Xcurve,Ycurve)
plt.plot(LineALL[0,:],LineALL[1,:])
plt.axis('equal')
plt.ylim(0)
plt.xlim(0)


