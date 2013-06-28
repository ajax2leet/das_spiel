#!/usr/bin/env python

###perlin_noise_test.py
###Algorithm test for generating terrain###


from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.colors as colors
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from matplotlib import pyplot as plt
import scipy.interpolate as intp
import numpy as np
import math

import random

class Noise():
    def __init__(self,seed):
        self.seed = seed   
    
    def cosineInterpolation(self,y1,y2,mu):       
        mu2 = (1-math.cos(mu*math.pi))/2
        return y1*(1-mu2)+y2*mu2

    def interpolatedNoise(self,x):
        int_x = int(x)
        frac_x = x- int_x    
        return self.cosineInterpolation(self.smoothNoise(int_x),self.smoothNoise(int_x+1),frac_x)

    def noiseAtPoint(self,x):
        random.seed(self.seed+x)
        return random.random()

    def smoothNoise(self,x):
        return (self.noiseAtPoint(x) + self.noiseAtPoint(x-1)/2 + self.noiseAtPoint(x+1)/2 + self.noiseAtPoint(x-2)/4 + self.noiseAtPoint(x+2)/4)/(2.5)
        #return self.noiseAtPoint(x)


    def perlinNoise1D(self, x,persistance,n):
        tot = 0
        
        for i in range(n):
            frequency = pow(2,i)
            amplitude = pow(persistance,i)
            tot = tot + self.interpolatedNoise(x*frequency)*amplitude  

        return tot

class Noise2D(Noise):
    def __init__(self,seed):
        Noise.__init__(self,seed)

    def noiseAtPoint(self,x,y):
        random.seed(self.seed+1E6*x+y)
        return random.random()

    def smoothNoise(self,x,y):
        n = self.noiseAtPoint
        corners = (n(x-1,y-1) + n(x+1,y-1) + n(x-1,y+1)+ n(x-1,y-1))/16
        sides = (n(x-1,y) + n(x+1,y) + n(x,y-1) + n(x,y+1))/8
        center = n(x,y)/4
    
        return corners+sides+center
   
    
    def interpolatedNoise(self,x,y):
        int_x = int(x)
        frac_x = x- int_x
        int_y = int(y)
        frac_y = y- int_y

        #Create Noise on edges
        a = self.smoothNoise(int_x,int_y)
        b = self.smoothNoise(int_x+1,int_y)
        c = self.smoothNoise(int_x, int_y+1)
        d = self.smoothNoise(int_x+1, int_y+1)
        
        #Interpolate ab and cd seperately (x)
        i1 = self.cosineInterpolation(a,b,frac_x)
        i2 = self.cosineInterpolation(c,d,frac_x)

        #Interpolate y
        return self.cosineInterpolation(i1,i2,frac_y)

    def perlinNoise2D(self,x,y,persistance,n):
        tot = 0
        for i in range(n):
            frequency = pow(2,i)
            amplitude = pow(persistance,i)
            tot = tot + self.interpolatedNoise(x*frequency,y*frequency)*amplitude  

        return tot
              


#Parameters
persistance = 1/3. # 1 is roughest
nBins = 100

#Create Noise object
noise = Noise2D(2000)


#Create arrays to hold data
x = np.linspace(0,10,num=nBins)
y = np.linspace(0,10,num=nBins)
xi,yi = np.meshgrid(x,y)
z=[]

#Simulate noise
for i in range(nBins):
    row = []
    for i2 in range(nBins):
        row.append(noise.perlinNoise2D(x[i],y[i2],persistance,3)*10+40)
    z.append(row)


#Surface plot
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(xi,yi,z,rstride=1,cstride=1,cmap=cm.coolwarm,linewidth=0,antialiased=False)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
ax.set_zlim3d(30,60) 
fig.colorbar(surf,shrink=0.5,aspect=5)

plt.show() 
  
"""
for i in range(nBins):
    for i2 in range(nBins):
        if z[i][i2] <= threshold:
            z[i][i2] = threshold


#Rebin data

nBins_new = 10

H = np.zeros([nBins_new,nBins_new])

for i in range(nBins):
    i_hist = int(i/nBins_new)    
    for i2 in range(nBins):
        i2_hist = int(i2/nBins_new)
        H[i_hist][i2_hist] += z[i][i2]

x = np.linspace(0,10,num=nBins_new)
y = np.linspace(0,10,num=nBins_new)

fig = plt.figure()
ax = fig.gca(projection='3d')
xpos,ypos = np.meshgrid(x,y)
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros(nBins_new*nBins_new)

dx = np.ones_like(xpos)
dy=dx.copy()
dz = H.flatten()

fracs = dz.astype(float)/dz.max()
norm = colors.normalize(fracs.min(), fracs.max())
colors = cm.jet(norm(fracs))

ax.bar3d(xpos,ypos,zpos,dx,dy,dz,color=colors)
       

     

plt.figure()
im = plt.imshow(z,extent=extent,cmap=cm.coolwarm,origin='upper') # drawing the function
# adding the Contour lines with labels
#cset = plt.contour(z,np.arange(0,1,100),linewidths=2,cmap=cm.Set2)
plt.colorbar(im) # adding the colobar on the right
"""

    

