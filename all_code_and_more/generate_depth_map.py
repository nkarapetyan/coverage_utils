#!/usr/bin/env python

"""
    A script that will generate two plots - depth data and RMSE uncertainty map

    Parameters
    ----------
       filename: this is a csv file that contain information about seq, depth, Lat and Long
                    filename is taken from the command line it is sys.argv[1]

    Example
    -------
        ./generate_depth_map.py filename

    TODO
    ----
        clean up to be generic and take as an input name of the field to generate the plot



    File Name: generate_depth_map.py
    Author: Nare Karapetyan, Alberto Quattrini Li
    Data Created: Feb 2018
    Date Last Modified: Feb 24 2019

"""

import matplotlib
import matplotlib.pyplot as plt

#from mpl_toolkits.basemap import Basemap
from mpl_toolkits.mplot3d import axes3d

import numpy as np
from numpy import ma

import pandas as pd
from pandas import DataFrame

import GPy

import sys

FONTSIZE = 10
FONTSIZE_LABEL = 20

# INPUT TO MODIFY
filename = sys.argv[1] 
MEASUREMENT_STEP = 5 # Take measurements every MEASUREMENT_STEP
#1-1249: launching; 1250-2019: Dock parallel current sensors; 2020-2299: dock x-paralled, y-perpendicular; 2649-3059: autonomous wp mission single parraled; 4535-4630: auto perpendicular y, parralel x
SEQUENCE_MIN = 1
SEQUENCE_MAX = 13000
TRAINING_DATA_RULE = "[0:len(pattern):MEASUREMENT_STEP]"
GRID_LATITUDE_NUM_CELLS = 10000 
GRID_LONGITUDE_NUM_CELLS = 40
VARIANCE_RBF_DEPTH = 0.1
LENGTHSCALE_RBF_DEPTH = 0.00001

# END INPUT TO MODIFY

# CONSTANTS
# Names of the fields in the CSV file
SEQUENCE_STRING = "seq"
LATITUDE_STRING = "Latitude"
LONGITUDE_STRING = "Longitude"
DEPTH_SENSOR_STRING = "depth"
COLORBAR_FORMAT = '%1.6f' # https://stackoverflow.com/questions/42153735/disabling-scientific-notation-of-imshow-colorbar-in-matplotlib
# END CONSTANTS

# DO NOT MODIFY UNLESS YOU KNOW WHAT YOU'RE DOING

# Read in data from CSV
readcsv = pd.read_csv(filename)
#Change sequence bounds to filter whole csv file for areas of interest.
pattern = readcsv.loc[(readcsv[SEQUENCE_STRING] > SEQUENCE_MIN) & (readcsv[SEQUENCE_STRING] < SEQUENCE_MAX)]

# Now the data is sliced in the region and sequence that we wanted.
# Here calculation of the wind vector, according to the transformations wrt boat and wind sensor measurement.

# Variables storing info from the CSV file
timestamp = readcsv.Timestamp
lat = pattern[LATITUDE_STRING]
lon = pattern[LONGITUDE_STRING]
depth_sensor_reading = pattern[DEPTH_SENSOR_STRING] * 0.3048 #feet to meter by multiplying


exec('X = pd.concat([lon' + TRAINING_DATA_RULE + ', lat' + TRAINING_DATA_RULE + '], axis=1).values')
exec('Z = pd.concat([depth_sensor_reading' + TRAINING_DATA_RULE + '], axis=1).values')

#GPy
# Kernel creation
# RBF Kernel def
gp_kernel_depth = GPy.kern.RBF(input_dim=2, variance=VARIANCE_RBF_DEPTH, lengthscale=LENGTHSCALE_RBF_DEPTH)

#Matern32 Kernel def
#gp_kernel_depth = GPy.kern.Matern32(input_dim=2, variance=VARIANCE_RBF_DEPTH, lengthscale=LENGTHSCALE_RBF_DEPTH)

depthGprMdl = GPy.models.GPRegression(X, np.reshape(Z[:,0],(len(Z[:,0]),1)),gp_kernel_depth, noise_var=0.1 )
#END GPy

#Test set over a grid.
# Create the grid and the test dataset.
grid_latitude = np.linspace(min(X[:,1]), max(X[:,1]), GRID_LATITUDE_NUM_CELLS) #50 jm
grid_longitude = np.linspace(min(X[:,0])-0.002, max(X[:,0])+0.002, GRID_LONGITUDE_NUM_CELLS) #50 jm

LON, LAT = np.meshgrid(grid_longitude, grid_latitude)
Xtest = np.array([LON.flatten(), LAT.flatten()]).T

#GPy
depthGprMdl.optimize_restarts(num_restarts=5, messages=True)

depthPred, depthsigma = depthGprMdl.predict(Xtest)
#print (depth_sensor_reading)
#END GPy

# Plot
# Reshaping predictions in a grid form
grid_depth_pred = np.reshape(depthPred, LAT.shape);
depthsigma = np.reshape(depthsigma, LAT.shape)

#prepare uncertainty for instensity coloring on plot

def plot_contour(x, y, z, title, xlabel, ylabel, cbar_label, measurements=None):
    """  Plot contour with measurement points.
    Args:
        x: 1d vector
        y: 1d vector
        z: 1d vector
        measurements: 2d vector
        title: 1d vector
    """
    plt.figure()
    plt.contourf(x, y, z,linewidth=0)
	#plt.plot(X[:,0], X[:,1], 'r+')
    #if measurements is not None:
    #    plt.plot(measurements[:,0], measurements[:,1], 'r+')
    cbar = plt.colorbar()#format = COLORBAR_FORMAT)
    cbar.set_label(cbar_label, labelpad = 40 , rotation=270, fontsize=FONTSIZE_LABEL)
    #cbar.ax.set_title('cbar_label')
    plt.title(title, fontsize=FONTSIZE_LABEL)
    plt.xlabel(xlabel, fontsize=FONTSIZE_LABEL)
    plt.ylabel(ylabel, fontsize=FONTSIZE_LABEL)
    plt.ticklabel_format(style='plain', useOffset=False)
    ax = plt.gca()
    ax.tick_params(axis = 'both', which = 'major', labelsize=FONTSIZE)
    ax.tick_params(axis = 'both', which = 'minor', labelsize=FONTSIZE)
    cbar.ax.tick_params(labelsize=FONTSIZE_LABEL)
 
plot_contour(LON, LAT, grid_depth_pred, "Depth Map", "Longitude", "Latitude", "Meters", X)

plot_contour(LON, LAT, depthsigma, "Depth Uncertainty", "Longitude", "Latitude", "RMSE", X)

plt.show()
