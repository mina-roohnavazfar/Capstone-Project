# Capstone Project: Demand Forecasting in Bike Shring Systems
=============================================================
## Introduction
=============================================================

Bike sharing systems have emerged as a new generation of transportation services, offering convenient and automated rental processes. These systems allow users to easily rent bikes from one location and return them to another, providing flexibility and accessibility for urban commuters and tourists alike. Bike-sharing rental process is highly correlated to the environmental and seasonal settings. For instance, weather conditions, precipitation, day of week, season, hour of the day, etc. can affect the rental behaviors. 
These systems have gained immense popularity due to their convenience and accessibility. With the entire process, from membership to rental and return, being automated, users can effortlessly rent bikes from one location and return them at another. Currently, there are more than 500 bike-sharing programs worldwide, featuring over 500,000 bicycles. These systems have become crucial players in addressing traffic, environmental, and health concerns.

My project aims to forecast the number of bike rentals for the years 2011 and 2012 in Washington D.C., USA. The avaiable dataset also includes crucial weather and seasonal information, as these factors play a significant role in bike-sharing rental behaviors. Weather information for the dataset is sourced from https://www.freemeteo.com , ensuring that relevant environmental conditions are taken into account during the analysis.

The dataset comprises 17 columns and 17379 records, providing valuable information for analysis. Among the columns, we have independent variables such as 'dteday', 'season', 'yr', 'mnth', 'hr', 'holiday', 'weekday', 'workingday', 'weathersit', 'temp', 'atemp', 'hum', and 'windspeed'. Additionally, there are three target variables: 'cnt', 'casual', and 'registered'. The 'cnt' variable represents the total sum of bike rentals for both 'casual' and 'registered' users.

To model the dataset, we adopt two distinct approaches. The first approach treats 'cnt' as the target variable and endeavors to predict its value based on the other independent variables. Here, 'cnt' serves as the comprehensive outcome we aim to forecast.

Alternatively, the second approach involves developing two separate models, each associated with 'casual' and 'registered' users. We then aggregate the predictions from these models to compute the 'cnt' variable. This method grants us deeper insights into the dataset, allowing us to comprehend the respective contributions of 'casual' and 'registered' users to the overall 'cnt' variable.

The solution we propose benefits multiple stakeholders. Urban planners and policymakers can optimize bike-sharing resources, addressing traffic congestion and promoting eco-friendly transport. Bike-sharing operators can enhance user experience by ensuring bike availability during peak times. Commuters and tourists enjoy improved convenience and access to transportation. Overall, the project aligns with the interests of city planners, bike-sharing providers, and the community at large.

=============================================================
## Project Organization
=============================================================
    
    ├── README.md                     <- The main README document for developers utilizing this project.
    |
    ├── data (https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset)   
    |
    ├── Presentation1_EDA.pdf         <- Initial presentation of the project including EDA
    ├── Presentation2_Modeling.pdf    <- Second presentation of the project including Modeling
    |
    ├── notebooks
    |   ├── sprint1_EDA.ipynb        <- Project notebook 1 - data preparation and exploration
    |   ├── sprint2_Modeling.ipynb   <- Project notebook 2 - data modeling
 

=============================================================
## Table of contents
=============================================================

- Bike Sharing Dataset 
- Exploratory Data Analysis (EDA)
- Modelling
- Conclusions

=============================================================
## Bike Sharing Dataset
=============================================================

	- instant: record index
	- dteday : date
	- season : season (1:springer, 2:summer, 3:fall, 4:winter)
	- yr : year (0: 2011, 1:2012)
	- mnth : month ( 1 to 12)
	- hr : hour (0 to 23)
	- holiday : whether day is holiday or not (extracted from http://dchr.dc.gov/page/holiday-schedule)
	- weekday : day of the week
	- workingday : if day is neither weekend nor holiday is 1, otherwise is 0.
	+ weathersit : 
		- 1: Clear, Few clouds, Partly cloudy, Partly cloudy
		- 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
		- 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
		- 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
	- temp : Normalized temperature in Celsius. The values are divided to 41 (max)
	- atemp: Normalized feeling temperature in Celsius. The values are divided to 50 (max)
	- hum: Normalized humidity. The values are divided to 100 (max)
	- windspeed: Normalized wind speed. The values are divided to 67 (max)
	- casual: count of casual users
	- registered: count of registered users
	- cnt: count of total rental bikes including both casual and registered

=============================================================
## Data Download, Cleaning & Exploratory Data Analysis
=============================================================

Our exploratory data analysis (EDA) process consists of three main steps. Firstly, we download the dataset from the UCI Machine Learning Repository (https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset). Secondly, we examine the dataset's structure and contents, checking for duplicated rows, columns, and missing values. In the third step, we analyze and visualize the data to gain insights into its distribution and identify correlations between variables and the target variables ('cnt', 'casual', and 'registered'). 

Here are some key observations from the EDA:

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

=============================================================
## Modeling
=============================================================

Considering the dataset's characteristics, we are planning to employ Linear and Non Linear Regression, Neural Network, and Decision Tree models for predicting our target variables.

Our project involves two distinct approaches for data modeling: 

First Approach: we treat 'cnt' as the target variable and endeavor to predict its value based on the other independent variables. Here, 'cnt' serves as the comprehensive outcome we aim to forecast.
Second Approach: It involves developing two separate models, each associated with 'casual' and 'registered' users. We then aggregate the predictions from these models to compute the 'cnt' variable. This method grants us deeper insights into the dataset, allowing us to comprehend the respective contributions of 'casual' and 'registered' users to the overall 'cnt' variable.

Here are some key insights from the Data Modeling:

- In summary, our findings indicate that the Neural Network consistently excels across the three target variables, exhibiting the lowest PMAE and PRMSE values, as well as the highest R-squared and Adjusted R-squared values. The Non Linear Regression model is a strong contender, often ranking second in terms of performance. The Decision Tree and Linear Regression models showcases competitive results, although it tends to be outperformed by the Neural Network and Non Linear Regression models.
- Taking into account the evaluation metrics, it appears that the performance of the models in predicting the Combined (Casual + Registered) Rentals is not as strong. This is evident from the fact that the PMAE and PRMSE values for all four models are higher when compared to the models predicting the total count target variable directly.
- Values of R-squared and Adjusted R-squared across models and target variables stay very close, which indicates we do not have overfitting in terms of model complexity. These metrics reflect how well the models fit the data, and the similarity between the R-squared and Adjusted R-squared values suggests that the models are not capturing noise or random variations in the training data. This is a positive indication that the models are not overly complex and are generalizing well to unseen data.
- PMAE and PRMSE values for test and train datasets exhibit a remarkable similarity for almost all models and target variables. However, in a certain case, applying Neural Network model to predict Casual rentals, the PMAE and PRMSE values for the train dataset are noticeably lower than those for the test dataset. This discrepancy suggests overfitting.

=============================================================
## Conclusion
=============================================================

This section will be addressed in future analyses.
