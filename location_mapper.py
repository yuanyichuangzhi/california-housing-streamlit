
import streamlit as st
from streamlit_folium import folium_static
import folium


def location_map(lat, long):
    m = folium.Map(location=[lat, long], zoom_start=10)

    # add marker for Liberty Bell
    tooltip = "House"
    folium.Marker(
        [lat, long], popup="Housing", tooltip=tooltip
    ).add_to(m)

    # call to render Folium map in Streamlit
    folium_static(m)