# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 12:29:00 2020

@author: mahoep
"""

import numpy as np
from stl import mesh
import stl
from os import remove


def main(lineAll,width):
    """
    Parameters
    ----------
    lineAll :  numpy.ndarray
        a 3,N vector of X,Y,Z points that define the contraction geometry, all in z0
    width : float
        width of the 2D mesh, defines the z+ plane

    Returns
    -------
    faces : numpy.ndarray
        faces is an array that is a series of 3,3 matricies. Each row is an 
        x,y,z pair. The 3,3 are the verticies for a triangle for STL

    """
    lineAll_z = np.copy(lineAll)
    lineAll_z[2,:] = lineAll_z[2,:] + width
    
    faces = np.zeros([np.size(lineAll,1), 3, 3])
    
    faces[0,:,:] = np.array([ lineAll[:,0], lineAll_z[:,0], lineAll[:,1]])
    for i in range(1,len(lineAll[0,:])):
        if (is_odd(i) == 1):
            faces[i,:,:] = np.append( faces[i-1,1:3,:], [lineAll_z[:,i]], axis=0)
        else:
            faces[i,:,:] = np.append( faces[i-1,1:3,:], [lineAll[:,i]], axis=0)    
        
        # Keeping this for reference
        # faces[1,:] = np.array([ faces[0,1:2], lineAll_z[:,1]])
        # faces[2,:] = np.array([ faces[1,1:2], lineAll[:,2]])
        # faces[3,:] = np.array([ faces[2,1:2], lineAll_z[:,2]])
        # faces[4,:] = np.array([ faces[3,1:2], lineAll[:,3]])
        # faces[5,:] = np.array([ faces[4,1:2], lineAll_z[:,3]])
    
    createMesh(faces)
    addPatchNum()
    
    return faces


def createMesh(faces):
    """
    Parameters
    ----------
    faces : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    contractionMesh = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    contractionMesh.vectors = faces
    contractionMesh.save('test.stl', mode=stl.Mode.ASCII)
    
    
def addPatchNum():
    """
    removes the string '.stl' anytime it appears in the stl file. 
    Creates the new one and deletes the old one

    """
    word = ".stl"
    with open("test.stl",'r') as f:
        text = f.readlines()
        f.close()
        
    with open("contraction.stl",'w') as t:
        k = 0
        for line in text:
            if word  in line:
                linefix = line.replace('.stl','')
                t.write(linefix)
            else:
                t.write(line)
            k+=1
        t.close()
    remove("test.stl")


def is_odd(num):
    """
    Parameters
    ----------
    num : int
        logical check to see if a number is odd (true) or not (false)

    Returns
    -------
    TYPE
        boolean
    """
    return num & 0x1


if __name__ == "__main__":
    addPatchNum()
