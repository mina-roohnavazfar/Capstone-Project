# Capstone Project: Demand Forecasting in Bike Shring Systems
## Introduction
Bike sharing systems have emerged as a new generation of transportation services, offering convenient and automated rental processes. These systems allow users to easily rent bikes from one location and return them to another, providing flexibility and accessibility for urban commuters and tourists alike. Bike-sharing rental process is highly correlated to the environmental and seasonal settings. For instance, weather conditions, precipitation, day of week, season, hour of the day, etc. can affect the rental behaviors. 
These systems have gained immense popularity due to their convenience and accessibility. With the entire process, from membership to rental and return, being automated, users can effortlessly rent bikes from one location and return them at another. Currently, there are more than 500 bike-sharing programs worldwide, featuring over 500,000 bicycles. These systems have become crucial players in addressing traffic, environmental, and health concerns.

My project aims to forecast the number of bike rentals for the years 2011 and 2012 in Washington D.C., USA. The avaiable dataset also includes crucial weather and seasonal information, as these factors play a significant role in bike-sharing rental behaviors. Weather information for the dataset is sourced from https://www.freemeteo.com , ensuring that relevant environmental conditions are taken into account during the analysis.

The dataset comprises 17 columns and 17379 records, providing valuable information for analysis. Among the columns, we have independent variables such as 'dteday', 'season', 'yr', 'mnth', 'hr', 'holiday', 'weekday', 'workingday', 'weathersit', 'temp', 'atemp', 'hum', and 'windspeed'. Additionally, there are three target variables: 'cnt', 'casual', and 'registered'. The 'cnt' variable represents the total sum of bike rentals for both 'casual' and 'registered' users.

To model the dataset, we adopt two distinct approaches. The first approach treats 'cnt' as the target variable and endeavors to predict its value based on the other independent variables. Here, 'cnt' serves as the comprehensive outcome we aim to forecast.

Alternatively, the second approach involves developing two separate models, each associated with 'casual' and 'registered' users. We then aggregate the predictions from these models to compute the 'cnt' variable. This method grants us deeper insights into the dataset, allowing us to comprehend the respective contributions of 'casual' and 'registered' users to the overall 'cnt' variable.

Project Organization
------------
    
    ├── README.md          <- The main README document for developers utilizing this project.
    |
    ├── Presentation_Bike Sharing System.pdf    <- Initial presentation of the project
    |
    ├── notebooks
    |   ├── EDA_Bike Sharing System.ipynb   <- Project notebook 1 - data preparation and exploration
 
This part will be completed in alignment with the progress of the project


## Table of contents
- Data Download, Cleaning & Exploratory Data Analysis
- Modelling
- Conclusions

## Data Download, Cleaning & Exploratory Data Analysis
Our exploratory data analysis (EDA) process consists of three main steps. Firstly, we download the dataset from the UCI Machine Learning Repository (https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset). Secondly, we examine the dataset's structure and contents, checking for duplicated rows, columns, and missing values. In the third step, we analyze and visualize the data to gain insights into its distribution and identify correlations between variables and the target variables ('cnt', 'casual', and 'registered'). Here are some key observations from the EDA:

- The columns 'month' and 'season' exhibit a strong positive correlation.
- 'temp' and 'atemp' are highly correlated.
- The columns 'registered', 'cnt', and 'casual' show a high positive correlation with each other.
- The variables 'casual', 'registered', and 'cnt' demonstrate a notably strong right-skewed distribution.
- On average, the number of bikes rented by casual users is lower than that of registered users over the two years.
- There is a noticeable increase in the number of registered bike rentals from 2011 to 2012, while the increase in casual rentals during the same period is relatively small.
- During the spring and summer seasons, the average number of bike rentals is higher for both casual and registered users compared to the winter and fall seasons.
- The average number of rental bikes during the first and last months of the year is lower compared to the other months for both casual and registered users.
- The average number of rental bikes for registered users surpasses that of casual users in general.
- At the beginning and end of the week, the average number of rentals is higher compared to the middle of the week. However, this pattern is opposite for registered users.
- For casual users, the average number of rentals is lower on working days than on non-working days. Conversely, this behavior is opposite for registered users.
- The mean number of rentals for both casual and registered users, as well as the 'cnt' variable, shows a decreasing trend as the values of weather situations increase.
- All the columns are significantly correlated with the three types of rental bikes (casual/registered/cnt).
These insights will guide our subsequent modeling and analysis efforts, helping us make informed decisions based on the patterns and relationships identified during the EDA process.

## Modeling
This section will be addressed in future analyses.
## Conclusion
This section will be addressed in future analyses.
