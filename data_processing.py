import pandas as pd 
import os 


# Saving all Data 
if not os.path.exists('origin_destination_analysis/transformed_data'):
    os.makedirs('origin_destination_analysis/transformed_data')

# ORIGIN 
# Only making an api call if we don't already have the origin data 
if os.path.isfile("origin_destination_analysis/initial_data/origin_data.csv"):
    # data was created using this url: https://data.ny.gov/Transportation/MTA-Subway-Origin-Destination-Ridership-Estimate-2/jsu2-fbtj/explore/query/SELECT%0A%20%20%60day_of_week%60%2C%0A%20%20%60hour_of_day%60%2C%0A%20%20%60origin_station_complex_id%60%2C%0A%20%20sum%28%60estimated_average_ridership%60%29%20AS%20%60sum_estimated_average_ridership%60%0AGROUP%20BY%20%60day_of_week%60%2C%20%60hour_of_day%60%2C%20%60origin_station_complex_id%60%0AHAVING%20%60sum_estimated_average_ridership%60%20%3E%3D%200.5/page/column_manager
    # ridership needs to be a sum because it's the avg ridership b/n specific pairs, not overall
    origin_df = pd.read_csv("origin_destination_analysis/initial_data/origin_data.csv", index_col=0).round(0)
    origin_df = origin_df[origin_df['Estimated Average Ridership'] > 0].reset_index()
    # averaging the ridership over 7 months
    origin_df['Estimated Average Ridership'] = origin_df['Estimated Average Ridership'] / 7
    origin_df.to_csv("origin_destination_analysis/transformed_data/origin_data_transformed.csv")
else: 
    print("The origin data does not exist. Please download from the url to get the data.")

## DESTINATION 
# Only making an api call if we don't already have the destination data 
if os.path.isfile("origin_destination_analysis/initial_data/destination_data.csv"):
    # data was created using this url: https://data.ny.gov/Transportation/MTA-Subway-Origin-Destination-Ridership-Estimate-2/jsu2-fbtj/explore/query/SELECT%0A%20%20%60day_of_week%60%2C%0A%20%20%60hour_of_day%60%2C%0A%20%20%60destination_station_complex_id%60%2C%0A%20%20sum%28%60estimated_average_ridership%60%29%20AS%20%60sum_estimated_average_ridership%60%0AGROUP%20BY%20%60day_of_week%60%2C%20%60hour_of_day%60%2C%20%60destination_station_complex_id%60%0AHAVING%20%60sum_estimated_average_ridership%60%20%3E%3D%200.5/page/filter
    # ridership needs to be a sum because it's the avg ridership b/n specific pairs, not overall
    destination_df = pd.read_csv("origin_destination_analysis/initial_data/destination_data.csv", index_col=0).round(0)
    destination_df = destination_df[destination_df['Estimated Average Ridership'] > 0].reset_index()
    # averaging the ridership over 7 months
    destination_df['Estimated Average Ridership'] = destination_df['Estimated Average Ridership'] / 7
    destination_df.to_csv("origin_destination_analysis/transformed_data/destination_data_transformed.csv")
else: 
    print("The destination data does not exist. Please download from the url to get the data.")

## STOP NAMES 
if os.path.isfile("origin_destination_analysis/initial_data/station_names.csv"):
    # data was created using this url: https://data.ny.gov/Transportation/MTA-Subway-Origin-Destination-Ridership-Estimate-2/jsu2-fbtj/explore/query/SELECT%0A%20%20%60origin_station_complex_id%60%2C%0A%20%20%60origin_station_complex_name%60%2C%0A%20%20%60origin_latitude%60%2C%0A%20%20%60origin_longitude%60%0AGROUP%20BY%0A%20%20%60origin_station_complex_id%60%2C%0A%20%20%60origin_station_complex_name%60%2C%0A%20%20%60origin_latitude%60%2C%0A%20%20%60origin_longitude%60/page/aggregate
    station_names_df = pd.read_csv("origin_destination_analysis/initial_data/station_names.csv", index_col=0).reset_index()
    station_names_df.columns = ['Station Complex ID', 'Station Complex Name', 'Latitude', 'Longitude']
    station_names_df.to_csv("origin_destination_analysis/transformed_data/station_names_transformed.csv")
else: 
    print("The stop names data does not exist. Please download from the url to get the data.")



# attempt at making data into half hour intervals 
# # make new datetime
# # split difficult rows into 2 
# destination_df_w_time_interval = pd.DataFrame(columns=['Day of Week', 'Hour of Day', 'Destination Station Complex ID',
#        'Estimated Average Ridership', 'Station Complex Name', 'time_interval'])
# for idx in range(len(destination_df[0:2])):
#     row_time = destination_df['Hour of Day'][idx]
#     if row_time in [6, 9, 15]:
#         row_1 = destination_df['Hour of Day'][idx]
#         row_1['Estimated Average Ridership'] = row_1['Estimated Average Ridership'] / 2
#         row_2
#         for row in [row_1, row_2]:
#             interval_string = determine_train_time_intervals(row_time
#                                                          , destination_df['Day of Week'][idx])
#             new_row = row
    #         new_row['time_interval'] = interval_string
    #         destination_df_w_time_interval = pd.concat([new_row.to_frame().T, destination_df_w_time_interval])
    # else: 
    #     interval_string = determine_train_time_intervals(row_time
    #                                                      , destination_df['Day of Week'][idx])
    # new_row = destination_df.iloc[0]
    # new_row['time_interval'] = interval_string
    # destination_df_w_time_interval = pd.concat([new_row.to_frame().T, destination_df_w_time_interval])
    # # assign interval string to list and add to dataframe 