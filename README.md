### sakunyan.github.io
# Welcome to Sakunyann's Data Science Portfolio! 🎉

Hello there! I'm Sakunyann, a data science enthusiast. This repository showcases my data science work in a Streamlit app. The project you'll find here is an AQI Prediction App, a testament to my passion for leveraging data to solve real-world problems. I hope you find it insightful and inspiring. Enjoy exploring!

<br>

# AQI Prediction App

## Project Description
This is a data science project that predicts the Air Quality Index (AQI) using tropospheric pollutants (CO, NO2, and O3) and AQI indices for CO, NO2, O3, and PM 2.5 values. The model was trained on data from the Google Earth Engine API Sentinel S5P satellite and the US Environmental Protection Agency (EPA) for Los Angeles, CA from December 2018 to December 2023.

## Methods
Throughout the data analysis process, two datasets containing atmospheric measurements and air quality indices were merged and cleaned. Missing values were addressed through imputation and removal of rows with insufficient data or specific dates. New columns were added to categorize the AQI values for PM2.5, Ozone, Carbon Monoxide, and Nitrogen Dioxide into standard air quality categories, which helps in understanding the air quality levels more intuitively. The correlation matrix revealed notable relationships between pollutants and AQI values, suggesting that higher concentrations of certain pollutants are associated with poorer air quality. The visualizations provided insights into the distribution of main pollutants and the breakdown of AQI values into different categories, highlighting the prevalence of air quality levels over time. 

The model was trained using a linear regression model. The performance of the model was evaluated using the following metrics:
- Mean Squared Error: 54.786985034934524
- R^2 Score: 0.8947579516610602
- Mean Absolute Error: 5.099757167185006

The dataset is now ready for further analysis to uncover trends and insights into air quality over time, which could inform environmental studies and public health policy-making.

<br>

## Disclaimer
This project is for portfolio purposes only. It was trained on a limited dataset and should not be used for making real-world decisions without further validation.
