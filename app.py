import streamlit as st
import pickle
import json
import numpy as np

# Load model
with open("artifacts/banglore_home_prices_model.pickle", "rb") as f:
    model = pickle.load(f)

# Load columns
with open("artifacts/columns.json", "r") as f:
    data_columns = json.load(f)["data_columns"]

locations = data_columns[3:]

st.title("🏠 Bangalore House Price Prediction")

total_sqft = st.number_input("Total Square Feet", min_value=100.0)
bhk = st.number_input("BHK", min_value=1, step=1)
bath = st.number_input("Bathrooms", min_value=1, step=1)

location = st.selectbox("Location", locations)

if st.button("Predict Price"):

    x = np.zeros(len(data_columns))
    x[0] = total_sqft
    x[1] = bath
    x[2] = bhk

    if location in data_columns:
        loc_index = data_columns.index(location)
        x[loc_index] = 1

    prediction = model.predict([x])[0]

    st.success(f"Estimated Price: ₹ {prediction:.2f} Lakhs")