
from component.widget import xmas_tree
import streamlit as st

left, right = st.columns([2,3], vertical_alignment="center")

PASSWORD = st.secrets["variable"].xmas_2025
GIFT_LINK = st.secrets["variable"].xmas_2025_gift

if "xmas_unlocked" not in st.session_state:
    st.session_state["xmas_unlocked"] = False

with left:
    xmas_tree.show()
with right.container(horizontal_alignment="center",border=True):
    if st.session_state["xmas_unlocked"] == False:
        form = st.form("xmas_unlock_form", clear_on_submit=False, border=False)
        form.title("Christmas Gift", text_alignment="center")
        text = form.text_input(label_visibility="collapsed", type="password", label="Enter the passkey", placeholder="Enter the passkey")
        submit = form.form_submit_button("Unlock",icon=":material/key:", type="primary", use_container_width=True, key="xmas_unlock")
        form.space("medium")
        
        if submit:
            if text.lower() == PASSWORD:
                st.session_state["xmas_unlocked"] = True
                st.rerun()
            else:
                st.toast("Incorrect passkey! Try again.",icon=":material/error:",duration=2)
    else:
        left__, right__ = st.columns([50,52], vertical_alignment="top")
        st.toast("Key accepted! 🎉", icon=":material/cake:", duration=2)
        st.balloons()
        with left__.container(vertical_alignment="top"):
            st.markdown("##### Merry Christmas! 🎉")
            st.markdown("<p style='color:#555;'>Hope you like the gift from the racoon! This was thought as something you need~</p>", unsafe_allow_html=True)

        right__.image(GIFT_LINK)
    
        