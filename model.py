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

# Evaluating the Linear Regression model
#mse_lr = mean_squared_error(y_test_lr, y_pred_lr)
#r2_lr = r2_score(y_test_lr, y_pred_lr)
#mae_lr = mean_absolute_error(y_test_lr, y_pred_lr)

# Displaying the performance metrics for the Linear Regression model
#print(f"Linear Regression - Mean Squared Error: {mse_lr}")
#print(f"Linear Regression - R^2 Score: {r2_lr}")
#print(f"Linear Regression - Mean Absolute Error: {mae_lr}")