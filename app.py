# packages import
import os
import pandas as pd
import streamlit as st
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

st.title('dbt-Covid 🦠 Analysis')

# Streamlit Tabs
about, analysis, raw_data = st.tabs([
    'About',
    'Analysis',
    'Raw Data'
])

with analysis:
    st.write('Analysis page')

with about:
    st.write('About page')

with raw_data:
    # Get data from DB
    with st.chat_message("user"):
        dataframe = pd.read_sql_table('covid_data', con=engine, schema='public')
        st.write("Raw Data 📖")
        st.dataframe(dataframe)