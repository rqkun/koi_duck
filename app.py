import streamlit as st
from PIL import Image
import logging
from component.function import navigation, toast
from component.widget import login

st.set_page_config(
    page_title="Koiduck",
    layout="wide",
    page_icon=Image.open("static/logo.png")
)

st.html("component/style/app.html")
logging.basicConfig(level=st.secrets["logging"]["INFO"], format='%(asctime)s - %(levelname)s - %(message)s')

if not st.user.is_logged_in:
    login.show()
else: 
    _, mid, _ = st.columns([1,6,1], gap="large")
    
    with mid:
        navigation.register_page()
    
    st.markdown("<div class='footer'>🍀 Made with love.</div>", unsafe_allow_html=True)
    toast.run()
