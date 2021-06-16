import numpy as np
import sys
import cv2 as cv


import pandas as pd


def main():
    #draw_on_white()
    draw_point();
    #test_print_white_points()

def test_print_white_points():
    assert len(sys.argv) == 2, 'Usage: python script image_file'

    img = cv.imread(sys.argv[1],0)
    cv.imshow("image", img)
    cv.waitKey(0)

    print(img.shape)

    print_white(img)


def print_white(img):
    rows,cols = img.shape
    for i in range(rows):
        for j in range(cols):
            if img[i][j] == 255: #it's white
                #print(i, j, img[i][j])
                print(i, j)
    cv.imshow("test", img)
    cv.waitKey(0)

def draw_on_white():
    assert len(sys.argv) == 3, "Usage: pyhton script points_file image_file"
    img = cv.imread(sys.argv[2])
    with open(sys.argv[1]) as point_file:
        line = point_file.readline()
        while line:
            a = line.strip()
            x, y = a[1:-1].split(',')
            print(x, y)
            line =point_file.readline()
            cv.circle(img, (int(y),int(x)), 2, (255, 0, 0), -1)
    cv.imshow('out',img)
    cv.waitKey(0)


def draw_point():
    assert len(sys.argv) == 3, "Usage: python script points_file image_file"
    points = pd.read_csv(sys.argv[1], sep =',')
    img = cv.imread(sys.argv[2])
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
    
if __name__ == "__main__":
    main()
