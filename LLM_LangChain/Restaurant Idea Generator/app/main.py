import streamlit as st
import json
from utils import get_cuisine_and_items


st.set_page_config('Restaurant Idea Generator',layout='wide')

st.title('Restaurant Idea Generator')
cuisine = st.sidebar.selectbox('Choose a Cuisine', options=sorted(['Arabic','Italian','Mexican','Nigerian','Kenyan','American','German','French','Thai','Chinese','Japanese']))

data = get_cuisine_and_items(cuisine)
name = data['restaurant_name'].strip()
menu = data['menu_items']
st.header(name) 
st.write('***Menu Items***')
for item in menu.strip().split(', '):
    x = f'- {item}'
    st.write(x)