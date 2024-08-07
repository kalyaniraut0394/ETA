import streamlit as st
import pandas as pandas
import sklearn
from sklearn.linear_model import LinearRegression
import pickle

st.image("innomatics-footer-logo.png")
st.title("Estimation of Time of Arrival")
model=pickle.load(open(r"time_estimater.pickle","rb"))

start_lat=st.number_input('enter the start lattitude:' )
start_lang=st.number_input('enter the start longitude:')
end_lat=st.number_input('enter the end lattitude:')
end_lang=st.number_input('enter the end longitude:' )
distance=st.number_input('enter the distance:')
density=st.number_input('enter the  density:')
weather=st.text_input('enter the weather:',value="rainy")
day=st.number_input('enter the day:')
hour=st.number_input('enter the hour:')


weather_numerical=(1 if weather=="rainy" else 2 if weather=="foggy" else 3)

if st.button("submit"):
    time=model.predict([[start_lat,start_lang,end_lat,end_lang,distance,density,weather_numerical,day,hour]])
    st.write("the estimated time is",time,"minutes")