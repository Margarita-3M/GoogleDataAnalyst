import os
import pandas as pd

def get_combined_csv(location, output_file='combined.csv'):
    '''
    The function gets all csv files from a directory and combine them in one csv
    and save to the current location.
    All csv files should have the same format.
    
    Parameters:
    - location: path to the folder with csv
    - file_name: name of the file for consolidated data
    '''

    # define that we need csv files only with -divvy-tripdata.csv ending
    ext = '-divvy-tripdata.csv'
    # get the full path all files in the directory
    # input_files = [i for i in glob('{}/*{}'.format(location, ext))]
    input_files = [(os.path.abspath(location + '/' + f)) for f in os.listdir(location) if ext in f]

    output_file_path = os.path.abspath(location + '/' + output_file)
    print(f"Out file: {os.path.abspath(output_file_path)}")
    
    # reading each file line by line and write to output file
    with open(output_file_path, 'w') as out:
        need_to_write_header = True
        for input_file in input_files:
            print(f"Working with: {input_file}")
            with open(input_file, 'r') as input_f:
                is_first_line = True
                for line in input_f:
                    if not is_first_line:
                        out.write(line)
                    else:
                        is_first_line = False
                        if need_to_write_header:
                            out.write(line)
                            need_to_write_header = False
                            
    print('The file is ready')
    return None

def get_cleaned_csv(location, input_file, output_file='cleared.csv'):
    # import combined data
    ## types adjustment
    dtypes = {'ride_id': 'string', 
              'rideable_type': 'string', 
              'start_station_name': 'string', 
              'start_station_id': 'string', 
              'end_station_name': 'string',
              'end_station_id': 'string', 
              'member_casual': 'string',
              'start_lat': 'float32', 
              'start_lng': 'float32', 
              'end_lat': 'float32', 
              'end_lng': 'float32'}
    df = pd.read_csv(location + '/' + input_file, dtype=dtypes)
    df['started_at'] = pd.to_datetime(df['started_at'],format='%Y-%m-%d %H:%M:%S')
    df['ended_at'] = pd.to_datetime(df['ended_at'],format='%Y-%m-%d %H:%M:%S')
    print(f'Initial shape: {df.shape}')

    ## create a table with min required data
    df_rides = df[['ride_id', 'rideable_type', 'started_at', 'ended_at', 
                   'start_lat', 'start_lng', 'end_lat', 'end_lng',
                   'member_casual']].copy()
    ## round coordinates to 3rd decimal
    geo_cols = ['start_lat', 'start_lng', 'end_lat', 'end_lng']
    df_rides[geo_cols] = df_rides[geo_cols].astype('float').round(3)
    df_rides = df_rides.drop_duplicates()
    df_rides = df_rides[~df_rides['end_lat'].isna()]
    df_rides = df_rides[~df_rides['end_lng'].isna()]
    
    print(f'Drop duplicates, rows with NULL and extra cols - new shape: {df_rides.shape}. Removed {df.shape[0] - df_rides.shape[0]} lines.')

    # save to the separate file
    df_rides.to_csv(location + '/' + output_file)
    print('The file is ready')
    return None
    