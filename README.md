# Capstone Project: Demand Forecasting in a Bike Sharing Rental System in Washington, D.C.
=============================================================
## Introduction
=============================================================

Bike sharing systems have emerged as a new generation of transportation services, offering convenient and automated rental processes. These systems allow users to easily rent bikes from one location and return them to another, providing flexibility and accessibility for urban commuters and tourists alike. Bike-sharing rental process is highly correlated to the environmental and seasonal settings. For instance, weather conditions, precipitation, day of week, season, hour of the day, etc. can affect the rental behaviors. 
These systems have gained immense popularity due to their convenience and accessibility. With the entire process, from membership to rental and return, being automated, users can effortlessly rent bikes from one location and return them at another. Currently, there are more than 500 bike-sharing programs worldwide, featuring over 500,000 bicycles. These systems have become crucial players in addressing traffic, environmental, and health concerns.

My project aims to forecast the number of bike rentals for the years 2011 and 2012 in Washington D.C., USA. The avaiable dataset also includes crucial weather and seasonal information, as these factors play a significant role in bike-sharing rental behaviors. Weather information for the dataset is sourced from https://www.freemeteo.com , ensuring that relevant environmental conditions are taken into account during the analysis.

The dataset comprises 17 columns and 17379 records, providing valuable information for analysis. Among the columns, we have independent variables such as 'dteday', 'season', 'yr', 'mnth', 'hr', 'holiday', 'weekday', 'workingday', 'weathersit', 'temp', 'atemp', 'hum', and 'windspeed'. Additionally, there are three target variables: 'cnt', 'casual', and 'registered'. The 'cnt' variable represents the total sum of bike rentals for both 'casual' and 'registered' users.

To model the dataset, we adopt two distinct approaches. The first approach treats total rentals ('cnt') as the target variable and endeavors to predict its value based on the other independent variables. Here, 'cnt' serves as the comprehensive outcome we aim to forecast.

Alternatively, the second approach involves developing two separate models, each associated with casual rentals ('casual') and registered rentals ('registered'). We then aggregate the predictions from these models to compute the total rentals. This method grants us deeper insights into the dataset, allowing us to comprehend the respective contributions of 'casual' and 'registered' users to the overall 'cnt' variable.

The solution we propose benefits multiple stakeholders. Urban planners and policymakers can optimize bike-sharing resources, addressing traffic congestion and promoting eco-friendly transport. Bike-sharing operators can enhance user experience by ensuring bike availability during peak times. Commuters and tourists enjoy improved convenience and access to transportation. Overall, the project aligns with the interests of city planners, bike-sharing providers, and the community at large.

=============================================================
## Project Organization
=============================================================
    
    ├── README.md                           <- The main README document for developers utilizing this project.
    |
    ├── data.csv (https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset)   
    ├── data_for_modeling.csv   <- Processed data obtained from EDA
    |
    ├── Presentation_EDA.pdf                <- Initial presentation of the project including EDA
    ├── presentation_baseline_models.pdf    <- Second presentation of the project including baseline models
    ├── Presentation_final.pdf              <- Final presentation of the project 
    |
    ├── notebooks
    |   ├── EDA.ipynb                          <- Project notebook 1 - data preparation and exploration
    |   ├── baseline_models.ipynb              <- Project notebook 2 - baseline modeling
    |   ├── modeling-total-rentals.ipynb       <- Project notebook 3 - final models for total rentals
    |   ├── modeling-casual-rentals.ipynb      <- Project notebook 3 - final models for casual rentals
    |   ├── modeling-registered-rentals.ipynb  <- Project notebook 3 - final models for registered rentals
 

=============================================================
## Table of contents
=============================================================

- Bike Sharing Dataset 
- Data Download, Cleaning & EDA
- Modelling
- Conclusions

=============================================================
## Bike Sharing Dataset
=============================================================

The dataset (data.csv) includes the following fields:

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
- Features 'temp' and 'atemp' are highly correlated.
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

Given the characteristics of our dataset, our approach to predictive modeling involves using various regression techniques, including both linear and non-linear regression, neural networks, decision trees, ensemble methods, and PCA integrated models. 

Our project involves two distinct approaches for data modeling: 

First Approach: we treat total rentals ('cnt') as the target variable and endeavor to predict its value based on the other independent variables. Here, 'cnt' serves as the comprehensive outcome we aim to forecast.

Second Approach: It involves developing two separate models, each associated with casual rentals ('casual') and registered rentals ('registered'). We then aggregate the predictions from these models to compute the total rentals. This method grants us deeper insights into the dataset, allowing us to comprehend the respective contributions of 'casual' and 'registered' users to the overall 'cnt' variable.

As we proceed with the development of our baseline models, we establish a robust model evaluation framework that aligns with the practical application of our models. This framework will enable us to assess the performance of our models accurately and make informed decisions regarding their robustness for the real-world scenarios. To achieve this, we will consider different evaluation metrics as Percentage Mean Absolute Error (PMAE), R-squared, and adj-R-squared which help us identify which approaches offer superior predictive capabilities in modeling total count bike rentals.

Here are the key insights from the Data Modeling:

- Our findings highlight that the integrated PCA-Gradient Boosting pipeline, Gradient Boosting, Bagging, and Neural Network models emerge as the top performers in predicting all the three target variables 'Total Rentals', 'registered rentals', and 'casual rentals', as evidenced by their favorable results in terms of PMAE, R-squared, and Adjusted R-squared values.
- By contrasting the PMAE values for the aggregated prediction (casual rentals + registered rentals) with those pertaining to the total count target variable, it becomes evident that the method involving separate models for forecasting casual and registered users, followed by summation, results in inferior performance when compared to directly predicting the total count.

=============================================================
## Conclusion
=============================================================

In this project, our primary objective was to predict three key rental metrics: total rentals, casual rentals, and registered rentals. To achieve this, we followed a structured approach that encompassed exploratory data analysis (EDA) and the application of various predictive models. Our model evaluations were based on key performance metrics such as Percentage Mean Absolute Error (PMAE), R-squared (R²), and adjusted R-squared (adj R²).

Among the models we experimented with, including the innovative PCA-Gradient Boosting pipeline, Gradient Boosting emerged as the top-performing algorithm. It demonstrated the highest accuracy and the lowest PMAE when predicting the target variables. Particularly, our models excelled in predicting total rentals and registered rentals, providing reliable forecasts for these metrics.

However, it's worth noting that predicting casual rentals proved to be somewhat more challenging. While the models exhibited strong performance in other areas, there was room for improvement in predicting casual rentals.

In terms of the best approach for predicting total rentals, our findings suggest that a direct prediction model outperforms the use of separate models for forecasting casual and registered users, followed by aggregating the results. This streamlined approach not only enhances accuracy but also simplifies the modeling process.

Overall, this project offers valuable insights into rental prediction models, highlighting the importance of model selection and the potential benefits of integrating PCA into Gradient Boosting. The outcomes and observations provided here will inform future iterations of rental forecasting and contribute to more effective decision-making in the domain of bike-sharing rentals.
