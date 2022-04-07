#!/usr/bin/env python

import numpy as np
import sys
import re
import cv2 as cv
import pandas as pd
import math
import os

from generate_waypoints import *
'''
main that tests and runs f-n on test files
'''

def main():
    #test_generate_waypoints()
    #test_make_waypoint_file_icra19() #this is a code to test the location of after experiement data
    #test_fsr_data_make_waypoint()
    #generate_Feb_10_2021_simple_patterns()
    #--#generate_Feb_21_2021_simple_patterns()
    #generate_July_27_2021_lake_patterns()
    generate_Feb_25_2022_bcd_lake_patterns()

def test_generate_waypoints():
    test_generate_waypoints_congaree_long_sattelite()
    #test_generate_waypoints_congaree_safe()
    #test_generate_waypoints_congaree_long()

def generate_Feb_25_2022_bcd_lake_patterns():
    '''
    Feb 25 2022 Lake BCD Patterns trial
    '''
    input_dir = "input/iros_2022_feb_25/"

    skel_pttrn = "89_footprint_tourLines.txt"

    config_file = "img_conf.wf"

    out_file_type_m = "m"
    out_file_type_c = "c"

    generate_waypoints(input_dir + skel_pttrn, input_dir + config_file, out_file_type_m)
    generate_waypoints(input_dir + skel_pttrn, input_dir + config_file, out_file_type_c)

def generate_July_27_2021_lake_patterns():
    '''
    July 27 2021 Lake Skeleton Patterns trial
    '''
    input_dir = "input/lake_July_2021/"

    skel_pttrn = "coordinates_nk_testing_from_jason.txt"

    config_file = "find_starting_node_config.wf"

    out_file_type_m = "m"
    out_file_type_c = "c"

    generate_waypoints(input_dir + skel_pttrn, input_dir + config_file, out_file_type_m)
    generate_waypoints(input_dir + skel_pttrn, input_dir + config_file, out_file_type_c)

def generate_Feb_10_2021_simple_patterns():
    '''
    Feb 10 2021 Simple Patterns trial
    '''
    input_dir = "input/2021_simple_patterns_exp/"

    lnm_pttrn = "generated_xy_paths/lnm_Feb_10.txt"
    sprl_pttrn = "generated_xy_paths/sprl_Feb_10.txt"

    config_file = "murray_sensor_location.wf"

    out_file_type = "m"
    out_file_type = "c"

    generate_waypoints(input_dir + lnm_pttrn, input_dir + config_file, out_file_type)
    generate_waypoints(input_dir + sprl_pttrn, input_dir + config_file, out_file_type)

def generate_Feb_21_2021_simple_patterns():
    '''
    Feb 10 2021 Simple Patterns trial
    '''
    input_dir = "input/2021_simple_patterns_exp/"

    lnm_pttrn = "generated_xy_paths/lnm_Feb_21.txt"
    sprl_pttrn = "generated_xy_paths/sprl_Feb_21.txt"
    line_pttrn = "generated_xy_paths/line_Feb_21.txt"

    lnm_pttrn = "generated_xy_paths/lnm_Feb_21_sparse.txt"
    sprl_pttrn = "generated_xy_paths/sprl_Feb_21_sparse.txt"
    line_pttrn = "generated_xy_paths/line_Feb_21_sparse.txt"

    config_file = "murray_deep_sensor_Feb_21_2021.wf"
    config_file_line = "line_feb_21_2021.wf"

    out_file_type = "m"
    #out_file_type = "c"

    generate_waypoints(input_dir + line_pttrn, input_dir + config_file_line, out_file_type)
    generate_waypoints(input_dir + lnm_pttrn, input_dir + config_file, out_file_type)
    generate_waypoints(input_dir + sprl_pttrn, input_dir + config_file, out_file_type)

def test_generate_waypoints_congaree_long_sattelite():
    '''
    ICRA 18 final tests generation
    '''
    input_dir = "input/trial_sept_19_2018/"
    env_img = "congaree_long_sattelite_safe_binary_map.png"

    long_pattern1 = "generated_xy_paths/longitudinal_path_4passes_sattelite.txt"
    long_pattern2 = "generated_xy_paths/longitudinal_path_with_width.txt"
    t_pattern = "generated_xy_paths/t_cover_sattelite.txt"

    config_file = "congaree_long_sattelite.wf"

    out_file_type = "m"
    #out_file_type = "c"

    generate_waypoints(input_dir + long_pattern1, input_dir + config_file, out_file_type)
    generate_waypoints(input_dir + long_pattern2, input_dir + config_file, out_file_type)
    generate_waypoints(input_dir + t_pattern, input_dir + config_file, out_file_type)

def test_generate_waypoints_congaree_long():
    '''
    ICRA 18 zig_zag generation with others that were not used
    '''
    input_dir = "input/congaree_long/"
    env_img = "congaree_long_planner_binary_map_safe.png"

    zigzag_pattern1 = "generated_xy_paths/equal_triangles_congaree_long_planner_binary_map_safe.png.txt"
    long_pattern1 = "generated_xy_paths/longitudinal_path_4passes.txt"
    long_pattern2 = "generated_xy_paths/longitudinal_path_with_width.txt"

    config_file = "congaree_long.wf"

    out_file_type = "m"
    #out_file_type = "c"

    generate_waypoints(input_dir + zigzag_pattern1, input_dir + config_file, out_file_type)
    generate_waypoints(input_dir + long_pattern1, input_dir + config_file, out_file_type)
    generate_waypoints(input_dir + long_pattern2, input_dir + config_file, out_file_type)

def test_generate_waypoints_congaree_safe():
    input_dir = "input/congaree_safe/"
    env_img = "congaree_safe_binary_map.png"
    long_pattern1 = "generated_xy_paths/long_4passes.txt"
    long_pattern2 = "generated_xy_paths/long_5passes.txt"
    long_pattern3 = "generated_xy_paths/long_8passes.txt"
    zigzag_pattern1 = "generated_xy_paths/start_opposite_ramp_zigzag_60_degrees.txt"
    zigzag_pattern2 = "generated_xy_paths/start_ramp_zigzag_60_degree.txt"
    zigzag_pattern3 = "generated_xy_paths/start_ramp_zigzag_65_degree_Triangles.txt"


    config_file = "congaree_safe.wf"

    out_file_type = "m"
    out_file_type = "c"
    '''
    generate_waypoints(input_dir + long_pattern2, input_dir + config_file, out_file_type)
    generate_waypoints(input_dir + long_pattern3, input_dir + config_file, out_file_type)
    generate_waypoints(input_dir + zigzag_pattern1, input_dir + config_file, out_file_type)
    generate_waypoints(input_dir + zigzag_pattern2, input_dir + config_file, out_file_type)
    generate_waypoints(input_dir + zigzag_pattern3, input_dir + config_file, out_file_type)
    '''
    generate_waypoints(input_dir + zigzag_pattern2, input_dir + config_file, out_file_type)
    generate_waypoints(input_dir + long_pattern1, input_dir + config_file, out_file_type)

def test_make_waypoint_file():
    input_dir = "../icra_data_all/pi_data_csv/"
    env_img = "congaree_safe_binary_map.png"
    long_pattern1 = "parallel_4_pass/congaree_2018-09-06_parallel_just_in_case_out.csv"
    long_pattern2 = "parallel_4_pass/congaree_2018-09-06_parallel_last_out.csv"
    zigzag_pattern1 = "zig_zag/congaree_2018-09-06_4_out.csv"
    zigzag_pattern2 = "zig_zag/congaree_2018-09-06_3_out.csv"
    zigzag_pattern3 = "zig_zag/congaree_2018-09-06_lat_out.csv"


    config_file = "congaree_safe.wf"

    out_file_type = "m"
    out_file_type = "c"


    input_file1 = "../icra_data_all/old_data/congaree_3_out.csv"
    input_file2 = "../icra_data_all/old_data/congaree_4_out.csv"
    input_file3 = "../icra_data_all/old_data/congaree_5_out.csv"

    input_file = "out.csv"
    #input_file = "../icra_data_all/old_data/zig_zag_during_iser_out.csv"
    '''
    make_waypoint_file(input_dir + long_pattern2, out_file_type)
    make_waypoint_file(input_dir + zigzag_pattern1, out_file_type)
    make_waypoint_file(input_dir + zigzag_pattern2, out_file_type)
    make_waypoint_file(input_dir + zigzag_pattern3, out_file_type)

    make_waypoint_file(input_file1, out_file_type)
    make_waypoint_file(input_file2, out_file_type)
    make_waypoint_file(input_file3, out_file_type)
    '''
    make_waypoint_file(input_file, out_file_type)

def test_make_waypoint_file_icra19():
    input_dir = "../icra_data_all/pi_data_csv/"
    input_dir = "/home/nare/not_a_dropbox/coverage/from_trasher_MUST_BE_CLEANED/icra19_data/2018-09-06-Riverine-ICRA2019/pi_data_csv/"
    env_img = None
    Z_cover = "congaree_2018_09_18_Z_cover_out.csv"
    L_cover = "congaree_2018_09_19_L_cover_terminated_out.csv"
    T_cover = "congaree_2018_09_19_T_cover_out.csv"

    test_file = "congaree_2018-09-06_parallel_4_passes_out.csv"

    out_file_type = "c"
    out_file_type = "m"

    in_file = "out.csv"
    in_file = input_dir + test_file

    '''
    make_waypoint_file(input_dir + T_cover, out_file_type)
    make_waypoint_file(input_dir + L_cover, out_file_type)
    make_waypoint_file(input_dir + Z_cover, out_file_type)
    '''

    make_waypoint_file(in_file, out_file_type)


def test_fsr_data_make_waypoint():
    input_dir="~/not_a_dropbox/coverage/fsr2019/riverine_coverage_2019-04-06/pi_bags/"
    m_2_short="/home/nare/short_2_passes_meanders.csv"

    make_waypoint_file(m_2_short, 'c')

if __name__ == "__main__":
    main()
