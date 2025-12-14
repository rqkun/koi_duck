import streamlit as st
from component.function import images

def show():
    st.space("large")
    with st.container(border=False, vertical_alignment="center", horizontal_alignment="center", height="stretch", gap="large"):
            
        left, right = st.columns(2, vertical_alignment="center")
        
        left.markdown(images.load_img_html("static/logo.png"), unsafe_allow_html=True)
        
        right.markdown("# ラン")
        right.markdown(""":violet-badge[かわいい] :primary-badge[愛らしい] :red-badge[恋]""")
        if right.button(key="unlock", label="**Unlock**", type="primary", width="content", icon=":material/key:"):
            st.login()