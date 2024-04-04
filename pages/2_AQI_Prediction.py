import streamlit as st
import pandas as pd
import numpy as np
import os
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# set page config
st.set_page_config(page_title="AQI Prediction",
                   page_icon=":wind_blowing_face:",
                   layout='wide',
                   initial_sidebar_state="auto")

st.title('Welcome to the AQI Prediction App! ')
st.text('')
col1, col2, col3 = st.columns([1,1,1])
col2.header(':wind_blowing_face: :cityscape: :seedling: ')

# Get the absolute path of the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path of the CSV file
csv_file = os.path.join(script_dir, 'Tropo_AQI_dataset.csv')

# Load data
@st.cache_data  # This line will cache the data loading
def load_data():
    try:
        data = pd.read_csv(csv_file)
        return data
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()

data = load_data()

if not data.empty:
    # Preparing the data for Linear Regression
    X_lr = data.drop(columns=['AQI'])
    y_lr = data['AQI']

    # Splitting the dataset into training and testing sets for Linear Regression
    X_train_lr, X_test_lr, y_train_lr, y_test_lr = train_test_split(X_lr, y_lr, test_size=0.2, random_state=42)

    # Initializing the Linear Regression model
    model_lr = LinearRegression()

    # Training the Linear Regression model
    model_lr.fit(X_train_lr, y_train_lr)

    # Making predictions with the Linear Regression model
    y_pred_lr = model_lr.predict(X_test_lr)

    st.text('')

    # Create a sidebar for user inputs
    st.header('Adjust the Sliders to See AQI Predictions :point_down:')
    st.write('')

    def user_input_features():
        col1, col2, col3, col4, col5 = st.columns([1, 0.2, 1, 0.2, 1])
        CO = col1.slider('Tropospheric CO', min_value=-34.430, max_value=5.710, value=0.032, step = 0.0001, format = '%f', 
                         help = '(Units mol/m^2) Tropospheric CO is a key atmospheric pollutant produced mainly from fossil fuel combustion and natural processes like wildfires. It contributes to air pollution and global warming.')
        NO2 = col3.slider('Tropospheric NO2', min_value=-0.00051, max_value=0.0192, value=0.00027, step = 0.00001, format = '%f',
                         help = '(Units mol/m^2) Tropospheric NO2, primarily from industrial and auto emissions, contributes to air pollution and climate change. Its monitoring is vital for health and the environment.')
        O3 = col5.slider('Tropospheric O3', min_value=0.0250, max_value=0.3048, value=0.1200, step = 0.0001, format = '%f',
                         help = '(Units mol/m^2) Tropospheric O3, formed from reactions between NOx gases and volatile organic compounds in sunlight, is a key air pollutant and greenhouse gas. Monitoring its levels is crucial due to its impact on health and the environment.')
        
        st.text('')
        col1, col2, col3, col4, col5, col6, col7 = st.columns([1, 0.1, 1, 0.1, 1, 0.1, 1])
        CO_AQI = col1.slider('CO AQI', min_value=0, max_value=500, value=9,
                             help = 'The CO AQI measures air quality based on CO concentration over 8 hours. Lower values mean better air quality. High CO levels can lead to health issues.')
        NO2_AQI = col3.slider('NO2 AQI', min_value=0, max_value=500, value=30,
                              help = 'The NO2 AQI measures air quality based on NO2 concentration. High levels can cause respiratory problems and contribute to the formation of other pollutants.')
        O3_AQI = col5.slider('O3 AQI', min_value=0, max_value=500, value=21,
                             help = 'The O3 AQI represents air quality based on O3 levels. High ozone levels can cause respiratory issues and other health problems.')
        PM25_AQI = col7.slider('PM2.5 AQI', min_value=0, max_value=500, value=30,
                               help = 'The PM2.5 AQI indicates air quality based on PM2.5 particles. These small particles can penetrate deep into the lungs and cause health issues.')
        st.write('')
        st.write('')
        data = {'CO': CO,
                'NO2': NO2,
                'O3': O3,
                'CO AQI': CO_AQI,
                'NO2 AQI': NO2_AQI,
                'O3 AQI': O3_AQI,
                'PM2.5 AQI': PM25_AQI}
        features = pd.DataFrame(data, index=[0])

        return features

    st.write('')
    st.write('')
    
    df = user_input_features()

    col1, col2, col3 = st.columns([0.5, 0.7, 0.5])
    col2.subheader('Input Parameters')
    col1, col2, col3 = st.columns([0.2, 1, 0.2])
    col2.dataframe(df, hide_index = True)

    # Make prediction using the trained model
    predicted_output = model_lr.predict(df)

    predicted_output = model_lr.predict(df)
    if np.isscalar(predicted_output):
        predicted_output = max(0, predicted_output)
    else:
        predicted_output = max(0, predicted_output[0])
        predicted_output = round(predicted_output)

    st.divider()
    col1, col2, col3 = st.columns([1, 0.8, 0.8])
    col1.subheader('Predicted AQI:')
    col2.title(predicted_output, help = 'The lowest AQI value is 0. :eyes:')
    
    if predicted_output <= 50:
        col3.subheader(':blush: Air Quality is Good!')
    elif 100 >= predicted_output > 50:
        col3.subheader(':neutral_face: Air Quality is Moderate.')
    elif 150 >= predicted_output > 100:
        col3.subheader(':mask: Air Quality is Unhealthy for Sensitive Groups.')
    elif 200 >= predicted_output > 150:
        col3.subheader(':worried: Air Quality is Unhealthy.')
    elif 300 >= predicted_output > 200:
        col3.subheader(':face_with_spiral_eyes: Air Quality is Very Unhealthy.')
    elif predicted_output > 300:
        col3.subheader(':dizzy_face: Air Quality is Hazardous.')
    else:
        col3.subheader('')


else:
    st.error("No data available for prediction.") 

st.divider()
st.write('')

st.subheader('AQI Basics for Ozone and Particle Pollution')
st.markdown("""
<table>
<tr>
    <th>Levels of Concern</th>
    <th>Values of Index</th>
    <th>Description of Air Quality</th>
</tr>
<tr style='background-color:Green; color:White'>
    <td>Good</td>
    <td>0 to 50</td>
    <td>Air quality is satisfactory, and air pollution poses little or no risk.</td>
</tr>
<tr style='background-color:Yellow; color:Black'>
    <td>Moderate</td>
    <td>51 to 100</td>
    <td>Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution.</td>
</tr>
<tr style='background-color:Orange; color:Black'>
    <td>Unhealthy for Sensitive Groups</td>
    <td>101 to 150</td>
    <td>Members of sensitive groups may experience health effects. The general public is less likely to be affected.</td>
</tr>
<tr style='background-color:Red; color:White'>
    <td>Unhealthy</td>
    <td>151 to 200</td>
    <td>Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects.</td>
</tr>
<tr style='background-color:Purple; color:White'>
    <td>Very Unhealthy</td>
    <td>201 to 300</td>
    <td>Health alert: The risk of health effects is increased for everyone.</td>
</tr>
<tr style='background-color:Maroon; color:White'>
    <td>Hazardous</td>
    <td>301 and higher</td>
    <td>Health warning of emergency conditions: everyone is more likely to be affected.</td>
</tr>
</table>
""", unsafe_allow_html=True)

url = "https://www.airnow.gov/aqi/aqi-basics/"
st.caption("Adapted from the EPA's [U.S. Air Quality Index (AQI)](%s)" % url)
