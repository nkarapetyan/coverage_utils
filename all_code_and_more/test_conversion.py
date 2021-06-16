############################################
#   Author: Nare Karapetyan
#   Date: July 26 2018
#   
#   Comment: a test script for testing 
#       - xy coordinates to latlong conversion
#       - latlong conversion to xy
#       - visually printing the values of conversion
############################################

import numpy as np
import sys
import re
import cv2 as cv
import pandas as pd
import math

from convert_coordinates import *

def main():
    #test_xy_to_latlong()
    #test_latlong_to_xy()
    test_distance_And_realtive_image_size_And_None() #2021_Feb_10_for_simple_patterns
    #test_convert_latlong_to_xy()

def test_xy_to_latlong():
    assert len(sys.argv) == 4, "Usage: python script points_file image_file config_file"
    xy_points = pd.read_csv(sys.argv[1], sep =',')
    img = cv.imread(sys.argv[2])
    config_file = sys.argv[3]

    xy_data = xy_points[['Y','X']]
    draw_points_for_visual_test(xy_points, img)
    #print(type(xy_data))
    for index, row in xy_data.iterrows():
        point = (int(row['X']), int(row['Y']))
        lat_long_coords = convert_xy_to_latlong(point[0], point[1], config_file)
        print (lat_long_coords)
    

def draw_points_for_visual_test(points, img):
    #print(list(points.columns.values))
    #print(points.shape)
    xy_data = points[['Y','X']]
    #print(type(xy_data))
    for index, row in xy_data.iterrows():
        point = (int(row['X']), int(row['Y']))
        print(type(point))
        cv.circle(img, point, 2, (255, 0, 0), -1)
    cv.imshow('points', img)
    cv.waitKey(0)


def test_latlong_to_xy():
    assert len(sys.argv) == 3, "Usage: python script config_file image"
    file_name = str(sys.argv[1])
    img = cv.imread(sys.argv[2])

    LAT, LONG = (33.972183,-81.042823)
    LAT, LONG = (33.973968, -81.044418)
    LAT, LONG = (33.964333, -81.037532)
    LAT, LONG = (33.973611,-81.042395)

    LAT = 33.9646651595523608	
    LONG = -81.0361862182617188
    LAT, LONG = (33.977536,-81.044418)
    LAT, LONG = (33.9648965152054814, -81.0368084907531738)
    LAT, LONG = (33.964333,-81.037532)

    LAT, LONG =( 33.9647897357514594, -81.0364437103271484) # start point test
    LAT, LONG = (33.9647363, -81.0362506) # start point of congaree_safe 
    LAT, LONG = (33.9645940, -81.0374093) # start point of congaree_safe on the opposite side of the previous one
    LAT, LONG = (33.7533536, -80.6455708)

    LAT, LONG = (34.03997, -81.23593) # center point of Feb 23 Buoy Location
    LAT, LONG = (34.03929, -81.23674) # start of the lwnmower
    LAT, LONG = (34.03023, -81.23435) # start of straight line



    coords = convert_latlong_to_xy(LONG, LAT, file_name)
    #coords = convert_latlong_to_xy_version2(LONG, LAT, file_name)
    print(coords)

    cv.circle(img, coords, 2, (255,0,0), -1)
    cv.imshow('Image', img)
    cv.waitKey(0)
    cv.destroyAllWindows()
    
def test_distance_And_realtive_image_size_And_None():
    upper_lat_long = (34.040239416480794, -81.23707064056055)
    bottom_lat_long = (34.03941439358027,-81.23535896224102)
    upper_long_lat = (upper_lat_long[1], upper_lat_long[0])
    bottom_long_lat = (bottom_lat_long[1], bottom_lat_long[0])
    print("-----*************------------")
    print(find_distance(upper_long_lat, bottom_long_lat))
    print("------*************-----------")
    
    print("-----------------")
    print(get_relative_image_size(upper_long_lat, bottom_long_lat))
    print("-----------------")
    
    
    a, b, c = get_world_information("input/2021_simple_patterns_exp/murray_sensor_location.wf")
    if a[1] == None:
        print("allala")
    print(a)
    print(b)
    print(c)

def test_convert_latlong_to_xy(): # this is without image size to find the x y start coordiantes for Feb 10 expoeriment
    #without image size (if image size will be undefined otherwise reads the size from wf)
    config_file = "input/2021_simple_patterns_exp/murray_sensor_location.wf"
    center_lat_long = (34.039725, -81.236218)
    #TAKES LONG LAT
    xy = convert_latlong_to_xy(center_lat_long[1], center_lat_long[0], config_file)
    a, upper_long_lat, bottom_long_lat = get_world_information(config_file)
    size = get_relative_image_size(upper_long_lat, bottom_long_lat)
    print("=======================")
    print(xy)
    print(size)
    print("=======================")

if __name__ == '__main__':
    main()
