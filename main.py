import numpy as np
import pandas as pd
import streamlit as st
from location_mapper import location_map
from california_housing_price.california_pricing_model import CaliforniaPricingModel
import time

@st.cache(allow_output_mutation=True,suppress_st_warning=True)
def load_ml_model():
    model = CaliforniaPricingModel()
    return model


def main():
    st.title("California housing prediction app")

    average_house_age = st.slider('Average age of the house in years', min_value=0.0, max_value=200.0)
    median_income = st.number_input('Median income in million', min_value=0.00, max_value=20.00)
    population_area = st.slider('Population in the vicinity in million', min_value=50.00, max_value=20000.00)
    households = st.slider('No. of households', min_value=0, max_value=7000)
    room_area = st.slider('Area of all rooms including bedroom', max_value=50000, min_value=0)
    bedroom_area = st.slider('Area of bedrooms', min_value=0, max_value=50000)
    lat = st.number_input("Enter the latitude of the location", min_value=32.5121, max_value=42.0126, value=37.3, step=0.1  )
    long = st.number_input("Enter the longitude", min_value=-124.6509, max_value=-114.1315, value=-122.37)
    if isinstance(lat, float) and isinstance(long, float):
        location_map(lat, long)


    house_features = [long, lat, average_house_age, room_area, bedroom_area,
                      population_area, households, median_income]


    price_estimate_bool = st.button('Estimate price')
    if price_estimate_bool:
        with st.spinner("Calculating the best price for the house"):
            model = load_ml_model()
            predicted_price = model.price_prediction(*house_features)
            time.sleep(1.5)
        st.header('The house is probably worth near about {}'.format(np.float(predicted_price[0])))


if __name__ == '__main__':
    main()




