import streamlit as st
import plotly.express as px
from backend import data
from datetime import date, timedelta

st.title('Weather Forcaste')

place = st.text_input('Place:')

days = st.slider("Forcast Days", min_value=1,max_value=5,help="Select the number of days for which you want the forecast.")

option = st.selectbox("select data to view", ('Tempterature','Sky'))


if place:
    st.subheader(f'{option} for the Next {days} days in {place}')
    filter_data = data(place,days)
    try:
        if option == 'Tempterature':
            temp = [dict['main']['temp']/10 for dict in filter_data]
            dates = [dict['dt_txt'] for dict in filter_data]

            figure = px.line(x=dates ,y=temp , labels={'x':'Date','y':'Temperature (c)'})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {'Clear':'images/clear.png','Clouds':'images/clouds.png','Rain':'images/rain.png','Snow':'snow/clear.png'}
            sky_condition = [dict['weather'][0]['main'] for dict in filter_data]
            img = [images[sky] for sky in sky_condition]
            st.image(img, width=115, caption= [dict['dt_txt'] for dict in filter_data])
    except :
        st.info('OOPS!! You have entered non-existing place')
else:
    st.subheader('Welcome!!!')