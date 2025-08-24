import streamlit as st
from component.function import images
from component.navigation import header
from PIL import Image
import logging
import streamlit_antd_components as sac

st.set_page_config(
    page_title="Koi",
    layout="centered",
    page_icon=Image.open("static/logo.png")
)

st.html("component/style/hide-anchor.html")

logging.basicConfig(level=st.secrets["logging"]["INFO"], format='%(asctime)s - %(levelname)s - %(message)s')

if not st.user.is_logged_in:
    with st.container(border=False, vertical_alignment="center", horizontal_alignment="center", height=300, gap="large"):
        
        left, right = st.columns(2, vertical_alignment="center")
        
        left.markdown(images.load_img_html("static/logo.png"), unsafe_allow_html=True)
        
        right.markdown("# ラン")
        right.markdown(""":violet-badge[かわいい] :primary-badge[愛らしい] :red-badge[恋]""")
        if right.button(key="unlock", label="**Unlock**", type="primary", width="content", icon=":material/key:",use_container_width=True):
            st.login()
else:
    email_list = st.secrets['verified']['gmail']
    if st.user.get("email") not in email_list:
        header.unauthorized()
    else: 
        header.show()