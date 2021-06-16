import time
import datetime

from convert_to_world_coordinates import *
import pandas as pd

#spiral 1
start_time = "12:24:30"
end_time = "12:30:59" 

'''
#spiral 2
start_time = "1:9:50"
end_time = "1:15:37" 

#bsd1
start_time = "12:33:48"
end_time = "12:41:34"

#bsd2
start_time = "01:00:44"
end_time = "01:08:14"
'''
#Feb 23 2021 Experiment Larger
#spiral
start_time = "00:28:16"
end_time = "00:44:14"
#bsd
start_time = "01:56:54"
end_time = "02:14:49"
#line
start_time = "00:13:40"
end_time = "00:22:09"

data_dir = "input/iros_2021_waypoints/"


def get_duration(start_time, end_time):
    '''
        Input: start and end timestamps in HH:MM:SS string format
        Output: duration in %H:%M:%S format

	Method:  converst string to datetime and then resulting timestamp to datetime
    '''

    start_t_el = datetime.datetime.strptime(start_time, "%H:%M:%S")
    end_t_el = datetime.datetime.strptime(end_time, "%H:%M:%S")

    start_t = time.mktime(start_t_el.timetuple())
    end_t = time.mktime(end_t_el.timetuple())

    dur_el = time.strftime('%H:%M:%S', time.gmtime(end_t - start_t))
    return dur_el


print(get_duration(start_time, end_time))

def get_data(input_file):
    df = pd.read_csv(input_file)
    df_new = df.sort_values("Date")
    df = df[['Lat', 'Lon']]
    return df

def get_distance(input_filename):
    '''
        Input: csv file containign gps coordinates
        Output: computes the length of th path based on gps trajectory

	Method: need to make sure gps are sorted by timestamp
    '''
    df = get_data(input_filename)
    long_lat_start = (df['Lon'].iloc[0], df['Lat'].iloc[0])
    distance = 0
    for i, row in df.iterrows():
        if(i==0): 
            continue
        long_lat_end = (row['Lon'], row['Lat'])
        distance = distance + find_distance(long_lat_start, long_lat_end)
        long_lat_start = long_lat_end
    return distance


spiral_1_filename = "first-spiral.csv" # 753 meter manual approximation on google maps distance measure
spiral_2_filename = "second-spiral.csv"
bsd_1_filename = "first-boustrophedon.csv"
bsd_2_filename = "second-boustrophedon.csv"
test_filename = "test.csv"

print("=====Distances====")
print("Spiral1: ", get_distance(data_dir + spiral_1_filename))
print("Spiral2: ",get_distance(data_dir + spiral_2_filename))
print("Boustrophedon1: ", get_distance(data_dir + bsd_1_filename))
print("Boustrophedon2: ", get_distance(data_dir + bsd_2_filename))
print(get_distance(data_dir + test_filename)) #this must be around 33 feet
