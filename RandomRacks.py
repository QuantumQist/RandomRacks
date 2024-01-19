#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 13:47:42 2024

@author: qunatum_qist
"""

import numpy as np
import matplotlib.pyplot as plt
import random

def PlotLayout(seq):
    """
    

    Parameters
    ----------
    seq : array with 14 elements of type string and possibe values: "solid", "stripe"
        Generates a plot with the ball layout in 8-ball

    Returns noting

    """
    
    #plot the Balls
    
    #Rows - y coordinates
    y1 = 2 * np.sqrt(3)
    y2 = np.sqrt(3)
    y3 = 0
    y4 = - np.sqrt(3)
    y5 = - 2 * np.sqrt(3)
    
    #Coordinates of the balls
    x_coords = [0, -1, 1, -2, 2, -3, -1, 1, 3, -4, -2, 0, 2, 4]
    y_coords = [y1, y2, y2, y3, y3, y4, y4, y4, y4, y5, y5, y5, y5, y5]
    
    #Colors on the plot
    col_list = []
    for k in range( len(seq) ):
        if seq[k] == "solid":
            col_list.append( "orange" )
        elif seq[k] == "stripe":
            col_list.append("blue")
    
    #Plot the setup
    ball8 = plt.Circle((0, 0), 1, color='black', alpha = 0.5)
    ball8border = plt.Circle((0, 0), 1, color='black', fill=  False)
    
    ax = plt.gca()
    ax.cla() # clear things for fresh plot
    ax.set_aspect( 1.0 )
    
    # change default range so that new circles will work
    ax.set_xlim((-5.5, 5.5))
    ax.set_ylim((-5.5, 5.5))
    # some data
    
    for k in range( len(seq) ):
        ball = plt.Circle((x_coords[k], y_coords[k]), 1, color=col_list[k], alpha = 0.5)
        ballborder = plt.Circle((x_coords[k], y_coords[k]), 1, color='black', fill=  False)
        
        ax.add_patch(ball)
        ax.add_patch(ballborder)
    
        
    ax.add_patch(ball8)
    ax.add_patch(ball8border)
    plt.axis('off')
    plt.rcParams['figure.dpi'] = 300
    plt.show()
    
 
def generate_rack():
    """
    Input: None
    
    Returns a random rack of balls 

    """
    #Generate a random ball layout
    
    #Corner balls one must be a solid, other stripe
    corners = [ "solid", "stripe" ]
    #Shuffle the balls
    random.shuffle( corners )
    
    #Generate a random sequence of 12 remaining other balls
    a = "solid"
    b = "stripe"
    balls = [a,a,a,a,a,a,b,b,b,b,b,b]
    #Shuffle the balls
    random.shuffle(balls)
    
    #Insert the corners to balls sequence
    balls.insert(9, corners[0])
    balls.append( corners[1] )
    
    return balls
#________________________________


random.seed(147) 
for k in range(8):
    rack = generate_rack()

#Rack number 7
PlotLayout(rack)

for k in range(5):
    rack = generate_rack()

#Rack number 12
PlotLayout(rack)