import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

st.title("⚡ Electricity Consumption Prediction")

# Load dataset
df = pd.read_csv("electricity_consumption_dataset.csv")

# Prepare data
target = "Electricity_Consumption_kWh"
X = df.drop(columns=[target])
y = df[target]

# Handle missing values
data = pd.concat([X, y], axis=1)
data = data.dropna()
X = data.drop(columns=[target])
y = data[target]

# Train model
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Model evaluation
predictions = model.predict(X_test)

# User input
st.subheader("Predict Electricity Consumption")

temperature = st.number_input("Temperature (°C)", 0.0, 50.0, 30.0)
humidity = st.number_input("Humidity (%)", 0.0, 100.0, 60.0)
occupants = st.number_input("Number of Occupants", 1, 20, 4)
ac = st.number_input("AC Usage (hours)", 0.0, 24.0, 5.0)
fan = st.number_input("Fan Usage (hours)", 0.0, 24.0, 8.0)
fridge = st.number_input("Fridge Usage (hours)", 0.0, 24.0, 20.0)
tv = st.number_input("TV Usage (hours)", 0.0, 24.0, 3.0)
washing = st.number_input("Washing Machine Usage (hours)", 0.0, 24.0, 1.0)
laptop = st.number_input("Laptop Usage (hours)", 0.0, 24.0, 4.0)
lights = st.number_input("Lights Usage (hours)", 0.0, 24.0, 6.0)

if st.button("Predict Consumption"):
    new_house = pd.DataFrame([{
        "Temperature": temperature,
        "Humidity": humidity,
        "Occupants": occupants,
        "AC_Hours": ac,
        "Fan_Hours": fan,
        "Fridge_Hours": fridge,
        "TV_Hours": tv,
        "WashingMachine_Hours": washing,
        "Laptop_Hours": laptop,
        "Lights_Hours": lights
    }])

    result = model.predict(new_house)[0]
    st.success(f"Predicted Electricity Consumption: {result:.2f} kWh")