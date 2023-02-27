import streamlit as st
import pandas as pd
from matplotlib import image
import plotly.express as px
import os

# FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# dir_of_interest = os.path.join(PARENT_DIR, "resources")
# IMAGE_PATH = os.path.join(dir_of_interest, "pages", "house.jpg")
# DATA_PATH = os.path.join(dir_of_interest, "data", "iris.csv")
st.title("Dashboard - house Data")
# img=image.imread(IMAGE_PATH)
# st.image(img)
data=pd.read_csv("C:/Users/gauta/house.csv")
st.dataframe(data)
prices=st.selectbox("Select the price of house:", data['bedrooms'].unique())
col1,col2=st.columns(2)
fig1=px.histogram(data[data['bedrooms']==prices], x='bathrooms')
col1.plotly_chart(fig1,use_container_width=True)
fig2 = px.box(data[data['floors'] == prices], y="bathrooms")
col2.plotly_chart(fig2, use_container_width=True)