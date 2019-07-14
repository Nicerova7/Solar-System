# -*- coding: utf-8 -*-

# N cuerpos problem
import numpy as np

#Constante de gravitacion Universal
G = 6.673841e-11  #N.m²/kg²
N = 9
t = 1
dt = 0.001

def force(n, posi, velo, ma, dti,x):
        
    global G
    global N
    
    a_x = 0.0	
    for i in range(n):
            
        my_r_x = posi[x][i];
        for j in range(n):
                if(i!=j):
                        d = posi[x][j] - my_r_x
                        if(d==0.0):
                                a_x += 0.0
                        else:
                                a_x += G*ma[j]/(d*d)
        velo[x][i] += a_x * dti
        posi[x][i] += velo[x][i] * dti
        a_x = 0.0

    print(posi[x][0])
  

def main():

   global t
   global dt

   pos = np.zeros((3,N),dtype='d')  #m
   vel = np.zeros((3,N),dtype='d')  #m/s
   m = np.zeros((N,),dtype='d')     #kg

   #Sol
   pos[0,0] = 0.0
   pos[1,0] = 0.0
   pos[2,0] = 0.0
	
   vel[0,0] = 0.0
   vel[1,0] = 0.0
   vel[2,0] = 0.0

   #Mercurio
   pos[0,1] = 57909175e+3
   pos[1,1] = 0.0
   pos[2,1] = 0.0

   vel[0,1] = 0.0
   vel[1,1] = 47.89
   vel[2,1] = 0.0

   #Venus
   pos[0,2] = 108208930e+3
   pos[1,2] = 0.0
   pos[2,2] = 0.0

   vel[0,2] = 0.0
   vel[1,2] = 35.09
   vel[2,2] = 0.0

   #Tierra
   pos[0,3] = 149597870e+3
   pos[1,3] = 0.0
   pos[2,3] = 0.0

   vel[0,3] = 0.0
   vel[1,3] = 29.79
   vel[2,3] = 0.0

   #Marte
   pos[0,4] = 227936640e+3
   pos[1,4] = 0.0
   pos[2,4] = 0.0

   vel[0,4] = 0.0
   vel[1,4] = 24.13
   vel[2,4] = 0.0

   #Jupiter
   pos[0,5] = 778412010e+3
   pos[1,5] = 0.0
   pos[2,5] = 0.0

   vel[0,5] = 0.0
   vel[1,5] = 13.06
   vel[2,5] = 0.0

   #Saturno
   pos[0,6] = 1426725400e+3
   pos[1,6] = 0.0
   pos[2,6] = 0.0

   vel[0,6] = 0.0
   vel[1,6] = 9.640278
   vel[2,6] = 0.0

   #Urano
   pos[0,7] = 2870972200e+3
   pos[1,7] = 0.0
   pos[2,7] = 0.0

   vel[0,7] = 0.0
   vel[1,7] = 6.81 
   vel[2,7] = 0.0
   
   #Neptuno
   pos[0,8] = 4498252900e+3
   pos[1,8] = 0.0
   pos[2,8] = 0.0

   vel[0,8] = 0.0
   vel[1,8] = 5.43 
   vel[2,8] = 0.0


   #Masa de los planetas en kg   
   m[0] = 1.989e+30   #sol
   m[1] = 3.303e+23   #Mercurio
   m[2] = 4.869e+24   #Venus
   m[3] = 5.976e+24   #Tierra
   m[4] = 6.421e+23   #Marte
   m[5] = 1.8987e+27  #Jupiter
   m[6] = 5.6851e+26   #Saturno
   m[7] = 8.6849e+25   #Urano
   m[8] = 1.024e+26   #Neptuno

   for k in range(10):
       print("eje x")
       force(N,pos,vel,m,k/1000.0,0)
       print("eje y")
       force(N,pos,vel,m,k/1000.0,1)
   
main()
