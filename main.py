#Importing relevant libraries
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

#Reading the excel file into a pandas data frame
df = pd.read_excel('log5_python.xlsx')

#print(df.columns)

#Dropping rows with missing values 
df = df.dropna(subset=['ThrottlePercent', 'MotorSpeedLeft', 'MotorSpeedRight'])

#Converting the excel columns to numpy arrays
throttle_percent = df['ThrottlePercent'].to_numpy()
motor_left = df['MotorSpeedLeft'] .to_numpy()
motor_right = df['MotorSpeedRight'].to_numpy()

#Reshaping the data so that it can fit a linear regression model
x = throttle_percent.reshape(-1, 1)
y_left = motor_left.reshape(-1, 1)
y_right = motor_right.reshape(-1, 1)

model_left = LinearRegression()
model_left.fit(x, y_left)

model_right = LinearRegression()
model_right.fit(x, y_right)


#Calculating the slops/coefficient and intercepts for both models
coefficients_left = model_left.coef_[0][0]
intercept_left = model_left.intercept_[0]

coefficients_right = model_right.coef_[0][0]
intercept_right = model_right.intercept_[0]

print(f"Motor Speed Left = {coefficients_left:.2f} * Throttle Percent + {intercept_left:.2f}")
print(f"Motor Speed Right = {coefficients_right:.2f} * Throttle Percent + {intercept_right:.2f}")
