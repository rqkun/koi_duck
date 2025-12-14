import streamlit_antd_components as sac

def unauthorized():
    sac.result(label='404 UNAUTHORIZED', description="Looks like you don't have access to this site.", status='error')