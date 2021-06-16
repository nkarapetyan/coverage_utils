############################################
#   Author: Nare Karapetyan
#   Date: July 26 2018
#   
#   Comment: 
#   - convert_image_to_binary function converst rgb to binary
#   - main applies conversion function and shows it
############################################

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import sys
import os


def main():
    assert (len(sys.argv) == 2 or len(sys.argv)==3), "Usage: python script_name image_file [out_file_name if not default]"
    file_name = str(sys.argv[1])
    if(len(sys.argv) == 3):
        out_file_name = str(sys.argv[2])   
    else:
        out_file_name = "default"
    img = convert_image_to_binary(file_name, out_file_name)
    cv.imshow('grey', img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def convert_image_to_binary(in_file_name, out_file_name="default"):
    #NOTE: this works by whitening darker regions while 
    # lighter regions will become darker
    '''
    Input: takes in in_file_name for image to be converted
        file_name
    Output: return nothing
    Method: converts image located in in_file_name to binary
        and saves it as out_file_name
    '''

    img = cv.imread(in_file_name)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    #ret, thresh = cv.threshold(gray,200,255, cv.THRESH_BINARY_INV)
    #FOR brigher TO BE WHITE 
    ret, thresh = cv.threshold(gray,65,255, cv.THRESH_BINARY)
    if out_file_name == "default":
        file_components = os.path.splitext(in_file_name)
        out_file_name = str(file_components[0]) + "_binary" + str(file_components[1]) 
    cv.imwrite(out_file_name, thresh)
        
    #FIXME: this return is just for testing
    return thresh
    
if __name__ == "__main__":
    main()
