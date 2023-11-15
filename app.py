# packages import
import os
import pandas as pd
import streamlit as st
import plotly.express as px
from dotenv import load_dotenv
from sqlalchemy import create_engine

# code imports
from frontend import (
    raw_data,
    about,
    graphs
)

# load environment
load_dotenv()

# CREDENTIALS
user = os.environ.get('USER')
password = os.environ.get('PASSWORD')
database = os.environ.get('DATABASE')
host = os.environ.get('HOST')
port = os.environ.get('PORT')

# DB engine
engine = create_engine(f"postgresql://{user}:{password}@{host}:{port}/{database}")

# App page configuration
st.set_page_config(
    page_title="Covid Analysis",
    page_icon="🦠",
    layout="wide",
    menu_items={
        'Report a bug': "https://github.com/Mega-Barrel/dbt-covid-streamlit/issues/new",
        'About': "# dbt + streamlit app. This is an *extremely* cool app!"
    }
)

# App title
st.title('dbt-Covid 🦠 Analysis')

# Streamlit Tabs
about, analysis, data = st.tabs([
    'About',
    'Analysis',
    'Raw Data'
])

with analysis:
    st.write('Analysis page')
    fig= graphs.generate_fct_monthly_plot(engine, pd, px)
    st.plotly_chart(fig, use_container_width=True, config = {'displayModeBar': False})

    fig= graphs.generate_fct_monthly_death_rate(engine, pd, px)
    st.plotly_chart(fig, use_container_width=True, config = {'displayModeBar': False})


with about:
    st.write('About page')

with data:
    # Get data from DB
    with st.chat_message("user"):
        st.write("Raw Data 📖")
        raw_data.raw_table(st, engine, pd)
    
    with st.chat_message("user"):
        st.write("Staging Tables 💻")
        raw_data.staging_table(st, engine, pd)
    
    with st.chat_message("user"):
        st.write("Marts Tables 💻")
        raw_data.mart_table(st, engine, pd)
