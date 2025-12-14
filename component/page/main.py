import streamlit as st
from component.card import horizontal, vertical
from component.dialog import cooking
from component.function import navigation
from component.widget import anniversary, error

def show():
    email_list = st.secrets['verified']['gmail']
    if st.user.get("email") not in email_list:
        error.unauthorized()
        st.stop()
    
    anniversary.show()
    
    with st.container(border=False,vertical_alignment="center",horizontal_alignment="center", horizontal=True, gap="large"):
        
        with st.container(border=True,vertical_alignment="center",horizontal_alignment="center"):
            vertical.show("static/love.png",None,None)
            if st.button("Love", key="nav_to_confession", use_container_width=True, type="primary", icon=":material/heart_plus:"):
                navigation.navto("confession")
                
        with st.container(border=True,vertical_alignment="center",horizontal_alignment="center"):
            vertical.show("static/cook.png",None,None)
            if st.button("Cook", key="nav_to_cook", use_container_width=True, type="primary", icon=":material/fork_spoon:"):
                cooking.show()
                
        with st.container(border=True,vertical_alignment="center",horizontal_alignment="center"):
            vertical.show("static/xmas.png",None,None)
            if st.button("Xmas", key="nav_to_xmas", use_container_width=True, type="primary", icon=":material/featured_seasonal_and_gifts:"):
                navigation.navto("xmas")
        
        with st.container(border=True,vertical_alignment="center",horizontal_alignment="center"):
            vertical.show("static/cook.png",None, None)
            st.button("Soon", key="soon", disabled=True,use_container_width=True, type="primary", icon=":material/construction:")

show()