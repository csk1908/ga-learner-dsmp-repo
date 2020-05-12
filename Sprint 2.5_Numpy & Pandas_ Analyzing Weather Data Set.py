#!/usr/bin/env python
# coding: utf-8

# Instructions
# Different functions that you would require to define for this project has been mentioned in the code block. All the parameters and the task, a function would do, have been mentioned there.
# 
# 1. Load the weather_2012 data csv file and store it in weather variable. The path of the dataset has been stored in the variable path for you.
# 
# 2. Check the categorical and numerical variables. You can check it by calling categorical and numerical functions.
# 
# 3. Check the distribution of a specific value like the number of times the weather was exactly Cloudy in the given column. Feel free to check on other values. You can check it by calling the function clear with respective parameters.
# 
# 4. By using the index of the value or name of the value you can check the number of counts. Now suppose you want to check some instances based on a specific condition like when the wind speed was above 35 and visibility was 25. You can directly check it by calling the function instances_based_condition with respective parameters and store the resulting dataframe in wind_speed_35_vis_25.
# 
# 5. You have temperature data and want to calculate the mean temperature recorded by month. You can generate a pivot table that contains the aggregated values(like mean, max, min, sum, len) recorded by month. You can call the function agg_values_ina_month with respective parameters.
# 
# 6. To groupby based on a column like you want to groupby on Weather column and then aggregate the mean values of each column for different types of weather using mean. You can call the function group_values and store the resulting dataframe in mean_weather. Feel free to try on different aggregated functions like max, min, sum, len
# 
# 7. You want to convert Celsius temperature into Fahrenheit temperatures. Call the function convert to do the same.

# 1. Load the weather_2012 data csv file and store it in weather variable. The path of the dataset has been stored in the variable path for you.

# In[2]:


import csv
import numpy as np
import pandas as pd
from scipy.stats import mode

#with open(r'E:\GreyAtom_Online_04.04.2020\NumPy&Pandas_Weather Dataset.csv') as csvDataFile:
      #weather = csv.reader(csvDataFile)


# In[3]:


weather = pd.read_csv("E:\\GreyAtom_Online_04.04.2020\\NumPy&Pandas_Weather Dataset.csv")


# 2. Check the categorical and numerical variables. You can check it by calling categorical and numerical functions.
# def categorical(df):
#     """ Extract names of categorical column
#     
#     This function accepts a dataframe and returns categorical list,
#     containing the names of categorical columns(categorical_var).
#     
#     Keyword arguments:
#     df - Pandas dataframe from which the columns name will be extracted
#         
#     Returns:
#     categorical_var - List of categorical features
#     """
#  

# In[4]:


def categorical(df):
    cat_var = df.select_dtypes(include = 'object')
    return(cat_var)


def numerical(df):
    num_var = df.select_dtypes(include = 'number')
    return(num_var)




categorical_var = categorical(weather)
#print(categorical_var)

numerical_var = numerical(weather)
#print(numerical_var)


# 3. Check the distribution of a specific value like the number of times the weather was exactly Cloudy in the given column. Feel free to check on other values. You can check it by calling the function clear with respective parameters.
# def clear(df,col,val):
#     """ Check distribution of variable
#     
#     This function accepts a dataframe,column(feature) and value which returns count of the value,
#     containing the value counts of a variable(value_counts)
#     
#     Keyword arguments:
#     df - Pandas dataframe
#     col - Feature of the datagrame
#     val - value of the feature
#     
#     Returns:
#     value_counts - Value count of the feature 
#     """
#    
# Call np. count_nonzero(array == value, axis=n) with n as 1 to count the occurrences of value in each row. Define n as 0 to count the occurrences of value in each column

# In[5]:


def clear(df,col,val):
    column_count = df[df[col]==val].count()[col]
    return(column_count)

col_count = clear(weather,'Weather', 'Clear')
print(col_count)

#without function
#column_count = weather[weather['Weather']=='Clear'].count()['Weather']
#print(column_count)

#Trial and Error(Failed)
#subset_df = weather[weather['Weather']=='Clear']
#column_count = subset_df.count()
#x = weather.where['Weather']=='Clear'
#column_count = np.count_nonzero([weather['Weather']] == 'Clear', axis = 0)


# 4. By using the index of the value or name of the value you can check the number of counts. Now suppose you want to check some instances based on a specific condition like when the wind speed was above 35 and visibility was 25. You can directly check it by calling the function instances_based_condition with respective parameters and store the resulting dataframe in wind_speed_35_vis_25.
# 
# def instances_based_condition(df,col1,val1,col2,val2):
#     """ Instances based on the condition
#     
#     This function accepts a dataframe, 2 columns(feature) and 2 values which returns the dataframe
#     based on the condition.
#     
#     Keyword arguments:
#     df - Pandas dataframe which has the data.
#     col1 - First feature of the dataframe on which you want to apply the filter
#     val1 - Value to be filtered on the first feature
#     col2 - Second feature of the dataframe on which you want to apply the filter
#     val2 - Value to be filtered on second feature
#     
#     Returns:
#     instance - Generated dataframe
#     """
#     

# In[6]:


#with function  
def instances_based_condition(df,col1,val1,col2,val2):
    speed_visibility = df[(df[col1]>val1) & (df[col2]==val2)]
    return (speed_visibility)
    
wind_speed_35_vis_25 = instances_based_condition(weather, 'Wind Spd (km/h)',35,'Visibility (km)',25)
#print(wind_speed_35_vis_25)

    
#without function    
#wind_speed_35_vis_25 = weather[(weather['Wind Spd (km/h)']>35) & (weather['Visibility (km)']==25)]
#print(wind_speed_35_vis_25)
                            


# 5. You have temperature data and want to calculate the mean temperature recorded by month. You can generate a pivot table that contains the aggregated values(like mean, max, min, sum, len) recorded by month. You can call the function agg_values_ina_month with respective parameters.
# 
# def agg_values_ina_month(df,date_col,agg_col, agg):
#     """  Aggregate values according to month
#     
#     This function accepts a dataframe, 2 columns(feature) and aggregated funcion(agg) which returns the Pivot 
#     table with different aggregated value of the feature with an index of the month.
#      
#     Keyword arguments:
#     df - Pandas dataframe which has the data.
#     date_col - Date feature of the dataframe on which you want to apply to_datetime conversion
#     agg_col - Feature of the dataframe on which values will be aggregated.
#     agg - Dictionary of aggregate functions with feature as the key and func as the value
#     
#     Returns:
#     aggregated_value - Generated pivot table
#     """
#     https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.dt.month.html
#     
#     https://www.google.com/amp/s/www.geeksforgeeks.org/python-pandas-to_datetime/amp/

# In[22]:



#with function 
def agg_values_ina_month(df,date_col,agg_col, agg):
    df[date_col] = pd.to_datetime(df[date_col],format = "%Y-%m-%d %H:%M:%S")
    aggregated_value = pd.pivot_table(df, index = df[date_col].dt.month, values = agg_col, aggfunc = agg)
    return aggregated_value



#a= {'Temp (C)': [np.mean,max, min, sum, len]}
aggregate = agg_values_ina_month(weather,'Date/Time','Temp (C)','a')

print(a)
print(aggregate)

#without function 
#print(weather.info())
#weather["Date/Time"] = pd.to_datetime(weather["Date/Time"]) 
#print(weather.info())
#print(weather.head())



#weather['Date/Time'] = pd.to_datetime(weather['Date/Time'],format = "%Y-%M-%D %H:%m:%S")
#aggregated_value = pd.pivot_table(weather,index = weather['Date/Time'].dt.month, values = 'Temp (C)',aggfunc = {'Temp (C)': [np.mean,max, min, sum, len]})
#print(aggregated_value)



# 6. To groupby based on a column like you want to groupby on Weather column and then aggregate the mean values of each column for different types of weather using mean. You can call the function group_values and store the resulting dataframe in mean_weather. Feel free to try on different aggregated functions like max, min, sum, len
# 
# def group_values(df,col1,agg1):
#     """ Agrregate values by grouping
#  
#     This function accepts a dataframe, 1 column(feature) and aggregated function(agg1) which groupby the 
#     datframe based on the column.
#    
#    Keyword arguments:
#     df - Pandas dataframe which has the data.
#     col1 - Feature of the dataframe on which values will be aggregated.
#     agg1 - Dictionary of aggregate functions with feature as the key and func as the value
#     
#     Returns:
#     grouping - Dataframe with all columns on which it is grouped on.
#     """
#     

# In[23]:


#with function 
def group_values(df,col1,agg1):
    x = df.groupby(col1).agg(agg1)
    return(x)


#a = [np.mean, max, min, sum, len]
#agg1 = {'Temp (C)':a,'Dew Point Temp (C)':a, 'Rel Hum (%)':a, 'Wind Spd (km/h)':a, 'Visibility (km)':a, 'Stn Press (kPa)':a}
agg1 = {'Temp (C)':np.mean,'Dew Point Temp (C)':np.mean, 'Rel Hum (%)':np.mean, 'Wind Spd (km/h)':np.mean, 'Visibility (km)':np.mean, 'Stn Press (kPa)':np.mean}
mean_weather = group_values(weather,'Weather',agg1)
mean_weather.tail()

#Without Function
#a = [np.mean,max, min, sum, len]
#x = weather.groupby('Weather').agg({'Temp (C)':np.mean, 'Dew Point Temp (C)':np.mean, 'Rel Hum (%)':np.mean, 'Wind Spd (km/h)':np.mean, 'Visibility (km)':np.mean, 'Stn Press (kPa)':np.mean})
#x = weather.groupby('Weather').agg({'Temp (C)':a,'Dew Point Temp (C)':a, 'Rel Hum (%)':a, 'Wind Spd (km/h)':a, 'Visibility (km)':a, 'Stn Press (kPa)':a})
#x.head()


# 7. You want to convert Celsius temperature into Fahrenheit temperatures. Call the function convert to do the same.
# def convert(df,celsius):
#     """ Convert temperatures from celsius to fahrenhheit
#     
#     This function accepts a dataframe, 1 column(feature) which returns the dataframe with converted values from 
#     celsius to fahrenhheit.
#          
#     Keyword arguments:
#     df - Pandas dataframe which has the data.
#     celsius - Temperature feature of the dataframe which you want to convert to fahrenhheit
#     
#     Returns:
#     converted_temp - Generated dataframe with Fahrenhheit temp.
#     
# 

# In[16]:


#with function 
def convert(df,celsius):
    f = (celsius * 9/5) + 32
    return(f)

cel = weather[['Temp (C)']]
print(cel.head())
converted_temp = convert(weather,cel)
print(converted_temp.head())

