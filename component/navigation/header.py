import streamlit as st

def show():
    pages = {
        "Toolbar": [
            st.Page("component/page/home.py", title="Home", icon=":material/home:"),
            st.Page("component/page/confession.py", title="Confession", icon=":material/heart_plus:"),
            st.Page("component/page/cooking.py", title="Cooking", icon=":material/fork_spoon:"),
            st.Page("component/page/logout.py", title="Logout", icon=":material/logout:")
        ]
    }
    pg = st.navigation(pages, position="top")
    pg.run()


def unauthorized():
    pages = {
        "Unauthorized": [
            st.Page("component/page/unauthorized.py", title="Home", icon=":material/home:"),
            st.Page("component/page/logout.py", title="Logout", icon=":material/logout:")
        ]
    }
    pg = st.navigation(pages, position="top")
    pg.run()