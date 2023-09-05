### CODING AN APP IN STREAMLIT

### import libraries
import pandas as pd
import numpy as np
import streamlit as st
import joblib

#from sklearn.ensemble import GradientBoostingRegressor

#####################################################################################################################################
### Create a title
st.title("Bike Rentals Prediction")

st.write('Welcome to the Bike Rentals Prediction App! Use this interactive tool to predict the total number of bike rentals based on factors like temperature, humidity, and windspeed. Simply adjust the sliders on the sidebar to input your values and see the model''s predictions in real-time. Explore the power of our Gradient Boosting model for rental forecasting.')


#######################################################################################################################################
### LAUNCHING THE APP ON THE LOCAL MACHINE
### 1. Save your *.py file (the file and the dataset should be in the same folder)
### 2. Open git bash (Windows) or Terminal (MAC) and navigate (cd) to the folder containing the *.py and *.csv files
### 3. Execute... streamlit run <name_of_file.py>
### 4. The app will launch in your browser. A 'Rerun' button will appear every time you SAVE an update in the *.py file


######################################################################################################################################
# Press R in the app to refresh after changing the code and saving here

### You can try each method by uncommenting each of the lines of code in this section in turn and rerunning the app

### You can also use markdown syntax.
#st.write('# Our last morning kick off :sob:')

### To position text and color, you can use html syntax
#st.markdown("<h1 style='text-align: center; color: blue;'>Our last morning kick off</h1>", unsafe_allow_html=True)


#######################################################################################################################################
# Create a header
st.subheader("Data")

# DATA LOADING
df = pd.read_csv('C:/Users/HP/Desktop/brainstation/projects/Capstone/Sprint 3/data.csv')

# remove redundant column `instant`
df = df.drop(['instant'], axis=1)

### C. Display the dataframe in the app
st.dataframe(df.head(6))

#######################################################################################################################################
# Add a line chart of daily average of total rentals
# Create a header
st.subheader("Daily Average Bike Rentals")

# average of cnt over dteday
dteday_cnt = df.groupby('dteday')['cnt'].mean()  

# create a line chart
st.line_chart(data=dteday_cnt, use_container_width=True)

#######################################################################################################################################
### MODEL INFERENCE: we use Gradient Boosting model for prediction

# Create a header
st.subheader("Users Input")

# Load the model using joblib
model = joblib.load('C:/Users/HP/Desktop/brainstation/projects/Capstone/Sprint 3/GB.pkl')

# Create a header
st.sidebar.header("User Input")

### create sliders for the features

# hour #############################################################################
hour = st.sidebar.slider("Hour", min_value=1, max_value=24, step=1)

# Month #############################################################################
month = st.sidebar.selectbox("Select Month", ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])

# Map the selected month to a numerical value (1 to 12)
month_mapping = {
    "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
    "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12
}
month_encoded = month_mapping[month]

# year #############################################################################
year = st.sidebar.selectbox("Select year", ["2011", "2012"])

# Map the selected year to a numerical value (1 to 2)
year_mapping = {
    "2011": 1,
    "2012": 2
}
year_encoded = year_mapping[year]

# Weekday #############################################################################
weekday = st.sidebar.selectbox("Select Weekday", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
# Map the selected weekday to a numerical value (0 to 6)
weekday_mapping = {
    "Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6
}
weekday_encoded = weekday_mapping[weekday]

# Season #############################################################################
month_to_season = {
    "December": "Winter",
    "January": "Winter",
    "February": "Winter",
    "March": "Spring",
    "April": "Spring",
    "May": "Spring",
    "June": "Summer",
    "July": "Summer",
    "August": "Summer",
    "September": "Fall",
    "October": "Fall",
    "November": "Fall",
}

season = month_to_season.get(month, "Unknown")

# Map the selected season to a numerical value (1 to 4)
season_mapping = {
    "Spring": 1,
    "Summer": 2,
    "Fall": 3,
    "Winter": 4
}
season_encoded = season_mapping[season]

# holiday #############################################################################
holiday = st.sidebar.checkbox("Is it a Holiday?")
# Convert 'holiday' to 0 or 1
holiday_encoded = 1 if holiday else 0

# temperature #############################################################################
temperature = st.sidebar.slider("Temperature (Celsius)", min_value=0.02, max_value=1.0, step=0.01)

# feeling_temperature #############################################################################
feeling_temperature = st.sidebar.slider("F_Temperature (Celsius)", min_value=0.0, max_value=1.0, step=0.01)

# humidity #############################################################################
humidity = st.sidebar.slider("Humidity", min_value=0.0, max_value=1.0, step=0.01)

# windspeed #############################################################################
windspeed = st.sidebar.slider("Windspeed (km/h)", min_value=0.0, max_value=0.85, step=0.01)

# weather_situation #############################################################################
weather_situation = st.sidebar.selectbox("Select Weather Situation",
    ["Clear, Few clouds, Partly cloudy, Partly cloudy", "Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist", "Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds", "Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog"])

# Map the selected weather situation to a numerical value (1 to 4)
weather_mapping = {
    "Clear, Few clouds, Partly cloudy, Partly cloudy": 1,
    "Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist": 2,
    "Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds": 3,
    "Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog": 4
}
weather_situation_encoded = weather_mapping[weather_situation]

##########################################################################################################################
# Make a prediction based on user input
input_data = pd.DataFrame({'hour':[hour],
                           'month':[month],
                           'year':[year],
                           'weekday':[weekday],
                           'Holiday':[holiday],
                           'Season':[season],
                           'Temperature': [temperature],
                           'F_Temperature': [feeling_temperature], 
                           'Humidity': [humidity], 
                           'Windspeed': [windspeed], 
                           'weather_situation':[weather_situation_encoded]})

# display user input
st.dataframe(input_data)

# create a subheader
st.subheader("Predict Total Retals using GB Model")

# processed input_data (change the order of features to be properly used in our Gradient Boosting model)
pro_input_data = pd.DataFrame({'season':[season_encoded],
                               'yr':[year_encoded],
                               'mnth':[month_encoded],
                               'hr':[hour-1],
                               'holiday':[holiday_encoded],
                               'weekday':[weekday_encoded],
                               'weathersit':[weather_situation_encoded],
                               'temp': [temperature],
                               'atemp': [feeling_temperature],
                              'hum': [humidity], 
                              'windspeed': [windspeed]})

# predict the pro_input_data
prediction = model.predict(pro_input_data)

# round the prediction value
rounded_prediction= int(np.round(prediction))

# create a box and display the rounded prediction value inside that
st.markdown(
    f'<div style="display: flex; justify-content: center; align-items: center; width: 60px; height: 30px; border: 2px solid blue; border-radius: 5px;">'
    f'<span style="color: blue; font-weight: bold; font-size: 28px ;">{rounded_prediction}</span>'
    f'</div>',
    unsafe_allow_html=True
)


