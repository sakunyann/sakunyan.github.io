import pickle

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.linear_model import LinearRegression

# Load data
df = pd.read_csv('Tropo_AQI_dataset.csv')

# Preparing the data for Linear Regression
X_lr = df.drop(columns=['AQI'])
y_lr = df['AQI']

# Splitting the dataset into training and testing sets for Linear Regression
X_train_lr, X_test_lr, y_train_lr, y_test_lr = train_test_split(X_lr, y_lr, test_size=0.2, random_state=42)

# Initializing the Linear Regression model
model_lr = LinearRegression()

# Training the Linear Regression model
model_lr.fit(X_train_lr, y_train_lr)

# Making predictions with the Linear Regression model
y_pred_lr = model_lr.predict(X_test_lr)

# Save the trained model to a file
with open('model_lr.pkl', 'wb') as file:
    pickle.dump(model_lr, file)
