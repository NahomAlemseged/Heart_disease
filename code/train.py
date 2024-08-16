import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from functions import *
from sklearn.metrics import classification_report
# from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier
import pickle


df = pd.read_csv('../data/heart_wrangles')
df.drop(columns='Unnamed: 0', inplace=True)

x = df.drop('HeartDisease', axis = 1)
y = df['HeartDisease']

x_train, x_test, y_train,y_test = train_test_split(x,y, random_state=42, test_size=0.3)

# Initialize and fit the Random Forest classifier
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(x_train, y_train)

# Extract feature importances
importances = rf.feature_importances_
feature_names = x.columns

# Create a DataFrame for feature importances
feature_importances_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances})

# Sort the DataFrame by importance
feature_importances_df = feature_importances_df.sort_values(by='Importance', ascending=False)

# Plot feature importances
plt.figure(figsize=(10, 6))
plt.barh(feature_importances_df['Feature'], feature_importances_df['Importance'], height=0.3, color = 'gray')
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.title('Feature Importances from Random Forest')
plt.gca().invert_yaxis()  # Invert y-axis to have the most important feature at the top
plt.savefig("../../assets/feature_plots")

# save the model to disk
import pickle
filename = 'model.pkl'
pickle.dump(rf, open(filename, 'wb'))