import streamlit as st
import time
import pandas as pd
import numpy as np

def get_dialog(key, value):
    return st.secrets[key][value]

def stream_data(text):
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.05)