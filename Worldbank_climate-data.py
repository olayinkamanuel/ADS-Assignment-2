# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 16:48:21 2023

@author: Olayinka Abolade
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def read_data(filename):
    """To clean and manipulate the data, we have to write a function that takes a 
    filename as an argument and reads a dataframe in World-bank format. 
    The function should then return two dataframes: one with years as columns and 
    one with countries as columns"""
    
    # Read the worldbank data into a dataframe
    worldbank_data = pd.read_csv(filename, skiprows=4)

    # Transpose the dataframe
    worldbank_data_t = worldbank_data.T
    
    # Drop unnecessary rows and columns
    worldbank_data_t = worldbank_data_t.drop(['Indicator Code', 'Country Code'], axis=0)

    # Create a new dataframe with countries as columns
    worldbank_data_t.columns=worldbank_data_t.iloc[0]
    worldbank_data_t=worldbank_data_t.iloc[1:]

    return worldbank_data, worldbank_data_t
# Call the clean_data function to create the two dataframes
worldbank_data, worldbank_data_t = read_data(r"C:\Users\USER\OneDrive\world_bank_data.csv")

print(worldbank_data)
print(worldbank_data_t)

# select 5 relevant indicators for analysis 
indicators_data = worldbank_data[worldbank_data['Indicator Name'].isin
                                 (['Arable land (% of land area)','Population, total',
                                    'Urban population',
                                    'CO2 emissions (kt)',
                                   'Electric power consumption (kWh per capita)'])]
print(indicators_data.head())

# Transpose the data, drop unnecessary rows and set 'Country Name' as index
worldbank_dataT = indicators_data.T
worldbank_dataT = worldbank_dataT.drop(['Country Code', 'Indicator Code'])
worldbank_dataT.columns = worldbank_dataT.iloc[0]
worldbank_dataT = worldbank_dataT[1:]

print(worldbank_dataT)

"""Select the 5 countries whose indicators would be analysed."""
world_data_Countries = worldbank_dataT.loc[:, ['China', 'Nigeria', 'United Kingdom', 'United States', 'Australia']]

print(world_data_Countries)

# Drop missing values from the dataframe
world_data_Countries.dropna(inplace=True)
#print the resulting dataframe
print(world_data_Countries)

"""for ease of analysis, we need to create new dataframes for 
specific indicators that are common to the selected countries. To achieve this
we need to slice the existing dataframe 'world_data_Countries' to provide only
data that are related to the period within 2010 & 2014 while we explore 
necessary statistical properties of the corresponding indicator."""

# Create Urban population dataframe for all selected countries
Urban_population = world_data_Countries.iloc[[21,22,23,24,25],[0,5,10,15,20]]
# converting dataframe data type to a numeric format 
Urban_population = Urban_population.apply(pd.to_numeric) 
# converting index values to numeric format
Urban_population.index = pd.to_numeric(Urban_population.index) 
print(Urban_population)

#statistical function for urban population
print(Urban_population.describe())
print(Urban_population.mean()) # checking the mean urban population
print(Urban_population.median()) # checking the median urban population
print(Urban_population.std()) # checking the urban population standard deviation

# Create Total population dataframe for all selected countries
Total_population = world_data_Countries.iloc[[21,22,23,24,25],[1,6,11,16,21]] 
Total_population = Total_population.apply(pd.to_numeric) # converting dataframe data type to a numeric format
Total_population.index = pd.to_numeric(Total_population.index) # converting index values to numeric format
print(Total_population)

#statistical function for Total population
print(Total_population.describe())
print(Total_population.mean())# checking the mean urban population
print(Total_population.median())# checking the median urban population
print(Total_population.std())# checking the urban population standard deviation

# Create CO2_emissions dataframe for all selected countries
CO2_emissions = world_data_Countries.iloc[[21,22,23,24,25],[2,7,12,17,22]] 
CO2_emissions = CO2_emissions.apply(pd.to_numeric) # converting dataframe data type to a numeric format
CO2_emissions.index = pd.to_numeric(CO2_emissions.index) # converting index values to numeric format
print(CO2_emissions)

#statistical function for CO2 Emissions
print(CO2_emissions.describe())
print(CO2_emissions.mean())# checking the mean urban population
print(CO2_emissions.median())# checking the median urban population
print(CO2_emissions.std())# checking the urban population standard deviation

#Create Electric power consumption dataframe for all selected countries
Power_consumption = world_data_Countries.iloc[[21,22,23,24,25],[3,8,13,18,23]]
#converting dataframe data type to a numeric format
Power_consumption = Power_consumption.apply(pd.to_numeric) 
#converting index values to numeric format
Power_consumption.index = pd.to_numeric(Power_consumption.index) 
print(Power_consumption)

#statistical function for Electric power consumption
print(Power_consumption.describe())
print(Power_consumption.mean())# checking the mean urban population
print(Power_consumption.median())# checking the median urban population
print(Power_consumption.std())# checking the urban population standard deviation

#Create Arable land (% of land area) dataframe for all selected countries
Arable_land = world_data_Countries.iloc[[21,22,23,24,25],[4,9,14,19,2]]
#converting dataframe data type to a numeric format
Arable_land = Arable_land.apply(pd.to_numeric) 
#converting index values to numeric format
Arable_land.index = pd.to_numeric(Arable_land.index) 
print(Arable_land)

#statistical function for Arable land (% of land area)
print(Arable_land.describe())
print(Arable_land.mean())#checking the mean urban population
print(Arable_land.median())#checking the median urban population
print(Arable_land.std())#checking the urban population standard deviation

"""Plotting a grouped bar of CO2 emission for the 5 countries  
from year 2010 to 2014"""
plt.style.use('seaborn')
CO2_emissions.T.plot(kind='bar')
plt.title(' CO2 Emissions in Five Countries between 2010 and 2014')
plt.xlabel('Countries Names')
plt.ylabel('Co2 Emission (kt)')
plt.savefig('bar Urban_population.png', dpi=300)
plt.show()

"""Line plot showing Urban population trends for 5 countries  
from year 2010 to 2014"""
plt.figure(figsize=(10,5))
plt.style.use('ggplot')
Urban_population.plot()
plt.title('Urban Population Trend for five countries')
plt.xlabel('Year')
plt.ylabel('Urban Population')
plt.xticks([2010,2011,2012,2013,2014])
plt.savefig('Line plot Urban_population.png', dpi=300)
plt.show()

"""Plotting a grouped bar showing trend of Energy consumption in the 5 countries  
from year 2010 to 2014"""
plt.style.use('seaborn')
Power_consumption.T.plot(kind='bar')
plt.title(' Trend of Energy Consumption in Five Countries between 2010 and 2014')
plt.xlabel('Countries Names')
plt.ylabel('Power_consumption')
plt.savefig('Line plot Power_consumption.png', dpi=300)
plt.show()

"""Line plot showing CO2 Emissions trends for 5 countries  
from year 2010 to 2014"""
CO2_emissions.plot()
plt.xlabel('Year')
plt.ylabel('CO2 Emissions (KT)')
plt.title('CO2 Emissions by Country')
plt.xticks([2010,2011,2012,2013,2014])
plt.savefig('Line plot CO2_emissions.png', dpi=300)
plt.legend()
plt.show()

"""Line plot showing Electric Power Consumption trends for 5 countries  
from year 2010 to 2014"""
Power_consumption.plot()
plt.xlabel('Year')
plt.ylabel('Electricity Consumption (kWh per capita)')
plt.title('Electricity Consumption by Country')
plt.xticks([2010,2011,2012,2013,2014])
plt.legend()
plt.savefig('Line plot Power_consumption.png', dpi=300)
plt.show()

Arable_land.plot()
plt.xlabel('Year')
plt.ylabel('Arable Land (% of total population)')
plt.title('Arable Land by Country')
plt.xticks([2010,2011,2012,2013,2014])
plt.legend()
plt.savefig('Line plot Arable Land.png', dpi=300)
plt.show()

"""Scatter plot showing relationship between Electric Power Consumption & CO2 Emmission in China  
from year 2010 to 2014"""
plt.style.use('ggplot')
plt.scatter(Power_consumption['China'], CO2_emissions['China'])
plt.title('Relationship between Electric power consumption & CO2 Emissions in China')
plt.xlabel('Power Consumption')
plt.ylabel('CO2 emmission')
plt.savefig('scatter plot Arabl.png', dpi=300)
plt.show()

