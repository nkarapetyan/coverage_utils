from pandas import read_csv
import pandas as pd
import sys
import os


def main():
    #test_slicing_after_sorting()
    #put_headline_to_the_file()
    input_file = sys.argv[1]
    output_file = str(os.path.splitext(input_file)[0]) + '_out.csv'
    print("WRITTEN IN " + output_file + "\n")
    add_seq(input_file, output_file)


def test_slicing_after_sorting():
    assert len(sys.argv)  == 2, "The usage is: python data_processing.py input_file "
    input_file = sys.argv[1]
    output_file = "out.csv"
    slice_data_after_sorting(input_file, output_file)


def test_keep_columns():
    assert len(sys.argv)  == 3, "The usage is: python data_processing.py input_file iput_file_with_id"
    input_file = sys.argv[1]
    input_file_with_id = sys.argv[2]
    output_file = "out.csv"
    keep_only_columns(input_file, input_file_with_id, output_file)


def put_headline_to_the_file():
    '''
        input comes from the terminal: name of file that headline shold be placed and headline.csv file
        in addition one new column of seq is added to the final file
        result is saved as _out.csv in same directory as input is
    '''
    input_file = ""
    headline_file = ""
    if __debug__:
        input_file = sys.argv[1]
        headline_file = sys.argv[2]
    else:
        input_df = sys.argv[2]
        headline_file = sys.argv[3]
        #FIXME: use parse to make sure user input is there and also do asserts
    output_file = str(os.path.splitext(input_file)[0]) + '_out.csv'
    print("WRITTEN IN " + output_file + "\n")
    add_headline(input_file, headline_file, output_file)
    add_seq(output_file, output_file)

def slice_data_after_sorting(input_file, output_file):
    df = pd.read_csv(input_file)
    df_new = df.sort_values("Timestamp")
    df_new = df_new[:-1400]
    df_new.to_csv(output_file, index=False)




#########################################
# FIXME: this is a very specific function based on waypoints, so both files have to have
# FIXME: was useless as the waypoints and actuall pattern have no intersection at all
# Lattitude and Longitude fields
# only saves entries that are in keep_file
# the way of using this function
# keep_only_columns input_file_to_modify input_file_with_ids_to_keep
#
# input: .csv data file and headline.csv
# output: .csv data file with headline
#
#########################################

def keep_only_columns(input_file, input_file_with_id, output_file):
    #FIXME: to be implemented
    keep_df = pd.read_csv(input_file_with_id)
    keep_df = keep_df[["Latitude", "Longitude"]]
    input_df = pd.read_csv(input_file)

    intersection = pd.merge(keep_df, input_df, on=["Latitude", "Longitude"])
    intersection.to_csv(output_file, index =False)


#########################################
# adds a heading to the csv file
#
# input: .csv data file and headline.csv
# output: .csv data file with headline
#
#########################################

def add_headline(input_file, headline_file, output_file):
    df = read_csv(input_file, index_col=False)
    headline = read_csv(headline_file, index_col = False)

    headline_list = headline.columns.tolist()
    df = add_headline_to_df(df, headline_list)
    df.to_csv(output_file, index=False)

#########################################
# adds a heading to the dataframe
#
# input: dataframe and  headline list
# output: new dataframe with a headline
#
#########################################

def add_headline_to_df(input_df, headline_list):
    if __debug__:
        print("the list of headline: " + str(headline_list))
    input_df.columns = headline_list
    if __debug__:
        print("resulting dataframe is:", input_df)
    return input_df

#########################################
# adds a sequence row in front of dataframe
#
# input: dataframe file
# output: enumerated dataframe
#
#########################################
def add_seq(input_file, output_file):
    df = read_csv(input_file, index_col=False)
    df = add_seq_to_df(df)
    df.to_csv(output_file, index= False)

#########################################
# adds a sequence row in front of dataframe
#
# input: dataframe
# output: hedline list
#
#########################################
def add_seq_to_df(input_df):
    input_df.insert(0, 'seq', range(0, len(input_df)))
    if __debug__:
        print("resulting dataframe is:", input_df)
    return input_df

#def save_every_other_k_th_line(step):

if __name__ == '__main__':
    main()
    assert len(sys.argv) == 3, "Usage: ./data_processing.py -o "OPTION" -s min max -f name_of_the_file"
